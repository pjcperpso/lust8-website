import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])


def _get_or_create_session_id(session_id: Optional[str] = None) -> str:
    if not session_id:
        return f"guest_{uuid.uuid4().hex}"
    return session_id


def _get_cart_owner(
    current_user: Optional[models.User],
    session_id: Optional[str],
):
    """Return (user_id, session_id) tuple identifying the cart owner."""
    if current_user:
        return current_user.id, None
    return None, session_id


def _build_cart_response(items, db: Session, lang: str = "en"):
    """Build cart response with calculated totals."""
    cart_items = []
    total_price = 0
    total_items = 0

    for item in items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            continue
        subtotal = product.price * item.quantity
        total_price += subtotal
        total_items += item.quantity

        name_field = product.name if lang == "en" else product.name_zh
        cart_items.append(
            schemas.CartItemResponse(
                id=item.id,
                product_id=product.id,
                product_name=name_field,
                product_name_zh=product.name_zh,
                quantity=item.quantity,
                selected_color=item.selected_color,
                price=product.price,
                subtotal=subtotal,
                added_at=item.added_at,
            )
        )

    return schemas.CartResponse(
        items=cart_items,
        total_items=total_items,
        total_price=round(total_price, 2),
    )


@router.get("", response_model=schemas.CartResponse)
def get_cart(
    session_id: Optional[str] = Cookie(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    lang: str = "en",
    db: Session = Depends(get_db),
):
    """Get current cart (user or guest)."""
    user_id, sess_id = _get_cart_owner(current_user, session_id)

    if user_id:
        items = (
            db.query(models.CartItem)
            .filter(models.CartItem.user_id == user_id)
            .order_by(models.CartItem.added_at.desc())
            .all()
        )
    else:
        items = (
            db.query(models.CartItem)
            .filter(models.CartItem.session_id == sess_id)
            .order_by(models.CartItem.added_at.desc())
            .all()
        )

    return _build_cart_response(items, db, lang)


@router.post("", response_model=schemas.CartResponse)
def add_to_cart(
    item_data: schemas.CartItemCreate,
    response: Response,
    session_id: Optional[str] = Cookie(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    lang: str = "en",
    db: Session = Depends(get_db),
):
    """Add item to cart."""
    # Validate product
    product = db.query(models.Product).filter(
        models.Product.id == item_data.product_id,
        models.Product.is_active == True,
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    user_id, sess_id = _get_cart_owner(current_user, session_id)

    # Set session cookie for guest
    if not user_id and not session_id:
        sess_id = _get_or_create_session_id(None)
        response.set_cookie(
            "session_id", sess_id,
            max_age=60 * 60 * 24 * 30,  # 30 days
            httponly=True,
            samesite="lax",
        )

    # Check if item already in cart
    existing = None
    if user_id:
        existing = (
            db.query(models.CartItem)
            .filter(
                models.CartItem.user_id == user_id,
                models.CartItem.product_id == item_data.product_id,
                models.CartItem.selected_color == item_data.selected_color,
            )
            .first()
        )
    else:
        existing = (
            db.query(models.CartItem)
            .filter(
                models.CartItem.session_id == sess_id,
                models.CartItem.product_id == item_data.product_id,
                models.CartItem.selected_color == item_data.selected_color,
            )
            .first()
        )

    if existing:
        existing.quantity += item_data.quantity
        db.commit()
    else:
        cart_item = models.CartItem(
            user_id=user_id,
            session_id=sess_id if not user_id else None,
            product_id=item_data.product_id,
            quantity=item_data.quantity,
            selected_color=item_data.selected_color,
        )
        db.add(cart_item)
        db.commit()

    # Return updated cart
    if user_id:
        items = db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()
    else:
        items = db.query(models.CartItem).filter(models.CartItem.session_id == sess_id).all()

    return _build_cart_response(items, db, lang)


@router.put("/{item_id}", response_model=schemas.CartResponse)
def update_cart_item(
    item_id: int,
    update_data: schemas.CartItemUpdate,
    session_id: Optional[str] = Cookie(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    lang: str = "en",
    db: Session = Depends(get_db),
):
    """Update cart item quantity."""
    user_id, sess_id = _get_cart_owner(current_user, session_id)

    query = db.query(models.CartItem).filter(models.CartItem.id == item_id)
    if user_id:
        query = query.filter(models.CartItem.user_id == user_id)
    else:
        query = query.filter(models.CartItem.session_id == sess_id)

    item = query.first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.quantity = update_data.quantity
    db.commit()

    # Return updated cart
    if user_id:
        items = db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()
    else:
        items = db.query(models.CartItem).filter(models.CartItem.session_id == sess_id).all()

    return _build_cart_response(items, db, lang)


@router.delete("/{item_id}", response_model=schemas.CartResponse)
def remove_cart_item(
    item_id: int,
    session_id: Optional[str] = Cookie(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    lang: str = "en",
    db: Session = Depends(get_db),
):
    """Remove item from cart."""
    user_id, sess_id = _get_cart_owner(current_user, session_id)

    query = db.query(models.CartItem).filter(models.CartItem.id == item_id)
    if user_id:
        query = query.filter(models.CartItem.user_id == user_id)
    else:
        query = query.filter(models.CartItem.session_id == sess_id)

    item = query.first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()

    # Return updated cart
    if user_id:
        items = db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()
    else:
        items = db.query(models.CartItem).filter(models.CartItem.session_id == sess_id).all()

    return _build_cart_response(items, db, lang)


@router.delete("", response_model=schemas.MessageResponse)
def clear_cart(
    session_id: Optional[str] = Cookie(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Clear entire cart."""
    user_id, sess_id = _get_cart_owner(current_user, session_id)

    if user_id:
        db.query(models.CartItem).filter(models.CartItem.user_id == user_id).delete()
    else:
        db.query(models.CartItem).filter(models.CartItem.session_id == sess_id).delete()

    db.commit()
    return schemas.MessageResponse(message="Cart cleared successfully")
