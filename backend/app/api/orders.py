import uuid
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Cookie, Query
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user, require_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])


def _generate_order_number() -> str:
    """Generate a unique order number."""
    return f"LUST8-{uuid.uuid4().hex[:8].upper()}"


@router.post("", response_model=schemas.OrderResponse, status_code=201)
def create_order(
    order_data: schemas.OrderCreate,
    session_id: Optional[str] = Cookie(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new order."""
    if not order_data.items:
        raise HTTPException(status_code=400, detail="Order must have at least one item")

    # Calculate totals
    subtotal = 0
    order_items = []

    for item in order_data.items:
        product = db.query(models.Product).filter(
            models.Product.id == item.product_id,
            models.Product.is_active == True,
        ).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Product {product.name} is out of stock (only {product.stock} left)",
            )

        item_subtotal = product.price * item.quantity
        subtotal += item_subtotal

        order_items.append(
            models.OrderItem(
                product_id=product.id,
                product_name=product.name,
                quantity=item.quantity,
                price=product.price,
                color=item.color,
            )
        )

        # Deduct stock
        product.stock -= item.quantity

    # Simple shipping calc (free over $100)
    shipping = 0 if subtotal >= 100 else 9.99
    tax = round(subtotal * 0.08, 2)  # 8% tax placeholder
    discount = 0
    total = round(subtotal + shipping + tax - discount, 2)

    # Create order
    order = models.Order(
        order_number=_generate_order_number(),
        user_id=current_user.id if current_user else None,
        status=models.OrderStatus.PENDING,
        subtotal=round(subtotal, 2),
        shipping=shipping,
        tax=tax,
        discount=discount,
        total=total,
        customer_name=order_data.customer_name,
        customer_email=order_data.customer_email,
        customer_phone=order_data.customer_phone,
        shipping_address=order_data.shipping_address,
        shipping_city=order_data.shipping_city,
        shipping_country=order_data.shipping_country,
        shipping_zip=order_data.shipping_zip,
        payment_method=order_data.payment_method,
        notes=order_data.notes,
        items=order_items,
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    # Clear cart if user is logged in or has session
    if current_user:
        db.query(models.CartItem).filter(models.CartItem.user_id == current_user.id).delete()
    elif session_id:
        db.query(models.CartItem).filter(models.CartItem.session_id == session_id).delete()
    db.commit()

    return order


@router.get("", response_model=List[schemas.OrderResponse])
def get_my_orders(
    current_user: models.User = Depends(require_current_user),
    db: Session = Depends(get_db),
):
    """Get orders for current user."""
    orders = (
        db.query(models.Order)
        .filter(models.Order.user_id == current_user.id)
        .order_by(models.Order.created_at.desc())
        .all()
    )
    return orders


@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(
    order_id: int,
    order_number: Optional[str] = Query(None),
    current_user: Optional[models.User] = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get order by ID or order number."""
    query = db.query(models.Order)

    if order_number:
        query = query.filter(models.Order.order_number == order_number)
    else:
        query = query.filter(models.Order.id == order_id)

    order = query.first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Authorization: user can only see their own orders unless admin
    if current_user:
        if order.user_id != current_user.id and current_user.role != models.UserRole.ADMIN:
            raise HTTPException(status_code=403, detail="Not authorized to view this order")
    # Guest users can view via order_number (no auth check needed)
    elif not order_number:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return order
