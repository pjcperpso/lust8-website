from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..auth import require_admin

router = APIRouter(prefix="/wholesale", tags=["Wholesale"])


@router.post("/inquiry", response_model=schemas.WholesaleInquiryResponse, status_code=201)
def create_wholesale_inquiry(
    inquiry_data: schemas.WholesaleInquiryCreate,
    db: Session = Depends(get_db),
):
    """Submit a wholesale/B2B inquiry."""
    inquiry = models.WholesaleInquiry(**inquiry_data.model_dump())
    db.add(inquiry)
    db.commit()
    db.refresh(inquiry)
    return inquiry


@router.get("/inquiries", response_model=list[schemas.WholesaleInquiryResponse])
def list_wholesale_inquiries(
    status: str = None,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """List all wholesale inquiries (admin only)."""
    query = db.query(models.WholesaleInquiry)
    if status:
        query = query.filter(models.WholesaleInquiry.status == status)
    inquiries = query.order_by(models.WholesaleInquiry.created_at.desc()).all()
    return inquiries


@router.get("/inquiries/{inquiry_id}")
def get_wholesale_inquiry(
    inquiry_id: int,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Get a single wholesale inquiry detail (admin only)."""
    inquiry = db.query(models.WholesaleInquiry).filter(
        models.WholesaleInquiry.id == inquiry_id
    ).first()
    if not inquiry:
        raise HTTPException(status_code=404, detail="Inquiry not found")
    return inquiry


@router.patch("/inquiries/{inquiry_id}/status")
def update_wholesale_status(
    inquiry_id: int,
    status: str,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin),
):
    """Update inquiry status (admin only)."""
    valid_statuses = ["new", "contacted", "quoted", "closed"]
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of: {valid_statuses}")

    inquiry = db.query(models.WholesaleInquiry).filter(
        models.WholesaleInquiry.id == inquiry_id
    ).first()
    if not inquiry:
        raise HTTPException(status_code=404, detail="Inquiry not found")

    inquiry.status = status
    db.commit()
    db.refresh(inquiry)
    return {"message": "Status updated", "status": inquiry.status}
