from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.demande import DemandeCreate, DemandeOut
from crud import demande as demande_crud
from models.demande import Demande
from auth.middleware import get_current_user
from typing import List


import traceback

router = APIRouter(prefix="/demandes", tags=["Demandes"])

@router.post("/", response_model=DemandeOut)
def create(demande: DemandeCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    print(" Route create_demande")
    try:
        traceback.print_exc() 
        return demande_crud.create_demande(db, demande, current_user)
    except Exception as e:
        print("Erreur interne:", e)
        raise HTTPException(status_code=500, detail="Erreur ")


@router.get("/", response_model=List[DemandeOut])
def read_all(db: Session = Depends(get_db)):
    return demande_crud.get_all_demandes(db)

# @router.get("/{demande_id}", response_model=DemandeOut)
# def read_by_id(demande_id: int, db: Session = Depends(get_db)):
#     demande = demande_crud.get_demande_by_id(db, demande_id)
#     if not demande:
#         raise HTTPException(status_code=404, detail="Demande non trouvee")
#     return demande

@router.delete("/{demande_id}")
def delete(demande_id: int, db: Session = Depends(get_db)):
    deleted = demande_crud.delete_demande(db, demande_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Demande non trouvee")
    return {"msg": "Demande supprimee"}


@router.get("/suivi/{sinistre_id}", response_model=List[DemandeOut])
def suivre_demandes_par_sinistre(sinistre_id: int, db: Session = Depends(get_db)):
    demandes = db.query(Demande).filter(Demande.sinistre_id == sinistre_id).all()
    return demandes

# ici ->je recupere les demande de l'association
# @router.get("/associations/{association_id}/demandes", response_model=List[DemandeOut])
# def get_demandes_by_association(association_id: int, db: Session = Depends(get_db)):
#     return db.query(Demande).filter(Demande.association_id == association_id).all()





