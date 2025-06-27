
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from auth.middleware import get_current_user
from typing import List
from schemas.demande import DemandeOut
from schemas.tache import TacheOut

from crud.volontaire_crud import (
    get_all_associations,
    get_demandes_par_association,
    assign_tache_to_volontaire,
    get_taches_by_volontaire
)

router = APIRouter(prefix="/volontaires", tags=["Volontaires"])

@router.get("/associations")
def read_associations(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_all_associations(db)

@router.get("/demandes", response_model=List[DemandeOut])
def read_demandes(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_demandes_par_association(db)

@router.post("/taches/{demande_id}")
def post_tache_volontaire(demande_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return assign_tache_to_volontaire(demande_id, db, current_user)

@router.get("/mes-taches", response_model=List[TacheOut])
def read_taches_volontaire(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_taches_by_volontaire(db, current_user)
