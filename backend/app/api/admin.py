from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..auth import require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/orders", response_model=List[schemas.OrderResponse])
def list_orders(
    status: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """List all orders (admin only)."""
    query = db.query(models.Order)

    if status:
        try:
            order_status = models.OrderStatus(status)
            query = query.filter(models.Order.status == order_status)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid status: {status}")

    total = query.count()
    offset = (page - 1) * page_size
    orders = query.order_by(models.Order.created_at.desc()).offset(offset).limit(page_size).all()

    return orders


@router.patch("/orders/{order_id}/status", response_model=schemas.OrderResponse)
def update_order_status(
    order_id: int,
    status: str,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Update order status (admin only)."""
    try:
        order_status = models.OrderStatus(status)
    except ValueError:
        valid = [s.value for s in models.OrderStatus]
        raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of: {valid}")

    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = order_status
    db.commit()
    db.refresh(order)
    return order


@router.get("/products", response_model=schemas.ProductListResponse)
def admin_list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    category: Optional[str] = None,
    search: Optional[str] = None,
    include_inactive: bool = False,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Admin product list with inactive items (admin only)."""
    from sqlalchemy import or_

    query = db.query(models.Product)

    if not include_inactive:
        query = query.filter(models.Product.is_active == True)

    if category:
        cat = db.query(models.Category).filter(models.Category.slug == category).first()
        if cat:
            query = query.filter(models.Product.category_id == cat.id)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                models.Product.name.ilike(search_term),
                models.Product.name_zh.ilike(search_term),
                models.Product.slug.ilike(search_term),
            )
        )

    total = query.count()
    offset = (page - 1) * page_size
    products = query.order_by(models.Product.sort_order.asc(), models.Product.id.asc()).offset(offset).limit(page_size).all()

    total_pages = (total + page_size - 1) // page_size

    return schemas.ProductListResponse(
        items=products,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )


@router.get("/stats")
def get_admin_stats(
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Get admin dashboard stats (admin only)."""
    from sqlalchemy import func

    total_products = db.query(func.count(models.Product.id)).filter(models.Product.is_active == True).scalar()
    total_orders = db.query(func.count(models.Order.id)).scalar()
    total_users = db.query(func.count(models.User.id)).scalar()
    total_revenue = db.query(func.coalesce(func.sum(models.Order.total), 0)).filter(
        models.Order.status.in_([models.OrderStatus.PAID, models.OrderStatus.SHIPPED, models.OrderStatus.DELIVERED])
    ).scalar()
    pending_orders = db.query(func.count(models.Order.id)).filter(
        models.Order.status == models.OrderStatus.PENDING
    ).scalar()
    wholesale_inquiries = db.query(func.count(models.WholesaleInquiry.id)).filter(
        models.WholesaleInquiry.status == "new"
    ).scalar()

    return {
        "total_products": total_products,
        "total_orders": total_orders,
        "total_users": total_users,
        "total_revenue": round(total_revenue or 0, 2),
        "pending_orders": pending_orders,
        "new_wholesale_inquiries": wholesale_inquiries,
    }
