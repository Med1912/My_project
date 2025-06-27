from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from auth.middleware import get_current_user
from crud.demande import delete_demande_by_sinistre 
from models.demande import Demande
from models.user_models import Sinistre 
from schemas.demande import DemandeOut
from typing import List




router = APIRouter(prefix="/sinistres", tags=["Sinistres"])

@router.delete("/demandes/{id}")
def remove_demande_sinistre(id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return delete_demande_by_sinistre(id, db, current_user)


@router.get("/mes-demandes", response_model=List[DemandeOut])
def get_mes_demandes(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "sinistre":
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    sinistre = db.query(Sinistre).filter(Sinistre.user_id == current_user["id"]).first()
    if not sinistre:
        raise HTTPException(status_code=404, detail="Sinistré introuvable")

    return db.query(Demande).filter(Demande.sinistre_id == sinistre.id).all()