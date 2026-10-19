from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import get_db
from .. import models, schemas
from ..auth import require_admin

router = APIRouter(prefix="/newsletter", tags=["Newsletter"])


@router.post("/subscribe", response_model=schemas.NewsletterResponse)
def subscribe_newsletter(
    sub_data: schemas.NewsletterSubscribe,
    db: Session = Depends(get_db),
):
    """Subscribe to the newsletter."""
    # Check if already subscribed
    existing = db.query(models.NewsletterSubscriber).filter(
        models.NewsletterSubscriber.email == sub_data.email
    ).first()

    if existing:
        if existing.is_active:
            raise HTTPException(
                status_code=400,
                detail="This email is already subscribed",
            )
        # Reactivate
        existing.is_active = True
        existing.subscribed_at = __import__('datetime').datetime.utcnow()
        db.commit()
        db.refresh(existing)
        return existing

    try:
        subscriber = models.NewsletterSubscriber(email=sub_data.email)
        db.add(subscriber)
        db.commit()
        db.refresh(subscriber)
        return subscriber
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Subscription failed")


@router.post("/unsubscribe")
def unsubscribe_newsletter(
    sub_data: schemas.NewsletterSubscribe,
    db: Session = Depends(get_db),
):
    """Unsubscribe from the newsletter."""
    subscriber = db.query(models.NewsletterSubscriber).filter(
        models.NewsletterSubscriber.email == sub_data.email
    ).first()

    if not subscriber:
        raise HTTPException(status_code=404, detail="Email not found in subscription list")

    subscriber.is_active = False
    db.commit()
    return {"message": "Successfully unsubscribed", "success": True}


@router.get("/subscribers")
def list_subscribers(
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """List all newsletter subscribers (admin only)."""
    subscribers = (
        db.query(models.NewsletterSubscriber)
        .order_by(models.NewsletterSubscriber.subscribed_at.desc())
        .all()
    )
    return subscribers
