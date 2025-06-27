from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.status import Status
from schemas.status import StatusUpdate, StatusOut

router = APIRouter(
    prefix="/status",
    tags=["Status"]
)

@router.put("/{demande_id}", response_model=StatusOut)
def update_status(demande_id: int, new_status: StatusUpdate, db: Session = Depends(get_db)):
    status = db.query(Status).filter(Status.demande_id == demande_id).first()
    
    if not status:
        raise HTTPException(status_code=404, detail="Status non trouve")
    status.etat = new_status.etat
    db.commit()
    db.refresh(status)
    return status