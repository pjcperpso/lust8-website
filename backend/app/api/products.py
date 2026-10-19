from typing import Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from ..database import get_db
from .. import models, schemas
from ..config import settings
from ..auth import require_admin

router = APIRouter(prefix="/products", tags=["Products"])


def _get_product_lang_field(lang: str, field: str) -> str:
    """Get the language-specific field name."""
    if lang == "zh":
        return f"{field}_zh"
    return field


@router.get("", response_model=schemas.ProductListResponse)
def get_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE),
    category: Optional[str] = None,
    sort: str = Query("featured", pattern="^(featured|price-asc|price-desc|name|newest)$"),
    search: Optional[str] = None,
    featured_only: bool = False,
    lang: str = Query("en", pattern="^(en|zh)$"),
    db: Session = Depends(get_db),
):
    """Get paginated product list with filters and sorting."""
    query = db.query(models.Product).filter(models.Product.is_active == True)

    # Category filter
    if category:
        cat = db.query(models.Category).filter(models.Category.slug == category).first()
        if not cat:
            raise HTTPException(status_code=404, detail="Category not found")
        query = query.filter(models.Product.category_id == cat.id)

    # Search
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                models.Product.name.ilike(search_term),
                models.Product.name_zh.ilike(search_term),
                models.Product.tagline.ilike(search_term),
                models.Product.tagline_zh.ilike(search_term),
            )
        )

    # Featured only
    if featured_only:
        query = query.filter(models.Product.is_featured == True)

    # Total count
    total = query.count()

    # Sort
    if sort == "featured":
        query = query.order_by(models.Product.is_featured.desc(), models.Product.sort_order.asc(), models.Product.id.asc())
    elif sort == "price-asc":
        query = query.order_by(models.Product.price.asc())
    elif sort == "price-desc":
        query = query.order_by(models.Product.price.desc())
    elif sort == "name":
        name_field = models.Product.name if lang == "en" else models.Product.name_zh
        query = query.order_by(name_field.asc())
    elif sort == "newest":
        query = query.order_by(models.Product.created_at.desc())

    # Pagination
    offset = (page - 1) * page_size
    products = query.offset(offset).limit(page_size).all()

    total_pages = (total + page_size - 1) // page_size

    return schemas.ProductListResponse(
        items=products,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )


@router.get("/featured", response_model=list[schemas.ProductListItem])
def get_featured_products(
    limit: int = Query(6, ge=1, le=20),
    lang: str = Query("en", pattern="^(en|zh)$"),
    db: Session = Depends(get_db),
):
    """Get featured products."""
    products = (
        db.query(models.Product)
        .filter(models.Product.is_active == True, models.Product.is_featured == True)
        .order_by(models.Product.sort_order.asc(), models.Product.id.asc())
        .limit(limit)
        .all()
    )
    return products


@router.get("/categories", response_model=list[schemas.CategoryResponse])
def get_categories(
    lang: str = Query("en", pattern="^(en|zh)$"),
    db: Session = Depends(get_db),
):
    """Get all product categories with product counts."""
    categories = (
        db.query(models.Category)
        .filter(models.Category.is_active == True)
        .order_by(models.Category.sort_order.asc(), models.Category.id.asc())
        .all()
    )

    result = []
    for cat in categories:
        product_count = (
            db.query(func.count(models.Product.id))
            .filter(
                models.Product.category_id == cat.id,
                models.Product.is_active == True,
            )
            .scalar()
        )
        cat_dict = schemas.CategoryResponse.model_validate(cat).model_dump()
        cat_dict["product_count"] = product_count
        result.append(cat_dict)

    return result


@router.get("/{product_id_or_slug}", response_model=schemas.ProductResponse)
def get_product(
    product_id_or_slug: str,
    lang: str = Query("en", pattern="^(en|zh)$"),
    db: Session = Depends(get_db),
):
    """Get product by ID or slug."""
    # Try by slug first
    product = db.query(models.Product).filter(models.Product.slug == product_id_or_slug).first()
    if not product:
        # Try by ID
        if product_id_or_slug.isdigit():
            product = db.query(models.Product).filter(
                models.Product.id == int(product_id_or_slug),
                models.Product.is_active == True,
            ).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product


@router.post("", response_model=schemas.ProductResponse, status_code=201)
def create_product(
    product: schemas.ProductBase,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Create a new product (admin only)."""
    # Check slug uniqueness
    existing = db.query(models.Product).filter(models.Product.slug == product.slug).first()
    if existing:
        raise HTTPException(status_code=400, detail="Product slug already exists")

    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    product_data: schemas.ProductBase,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Update a product (admin only)."""
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product_data.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete("/{product_id}", response_model=schemas.MessageResponse)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Soft delete a product (admin only)."""
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.is_active = False
    db.commit()
    return schemas.MessageResponse(message="Product deleted successfully")
