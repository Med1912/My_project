from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schemas import  AssociationOut
from crud import user_crud
from auth.middleware import get_current_user
from models.user_models import Association, User
from typing import List
from db.database import get_db
from schemas.user_schemas import AssociationOut
from models.demande import Demande
from schemas.demande import DemandeOut
from crud.demande import confirmer_demande_by_association
from schemas.status import StatusUpdate
from crud.demande import delete_demande_by_association



association_router = APIRouter(prefix="/associations", tags=["Associations"])

@association_router.get("/", response_model=List[AssociationOut])
def get_all_associations(db: Session = Depends(get_db)):
    return db.query(Association).all()

@association_router.get("/dashboard/association")
def dashboard_association(current_user: dict = Depends(get_current_user)):
    if current_user["role"].lower() != "association":
        raise HTTPException(status_code=403, detail="Acces refuse")
    return {"message": f"Bienvenue au tableau de bord de l'association {current_user['email']}"}

@association_router.get("/dashboard/volontaire")
def dashboard_volontaire(current_user: dict = Depends(get_current_user)):
    if current_user["role"].lower() != "volontaire":
        raise HTTPException(status_code=403, detail="Acces refusee!!")
    return {"message": f"Bienvenue au dashboad volontaire {current_user['email']}"}




# @association_router.get("/dashboard/sinistre")
# def dashboard_sinistre(current_user: dict = Depends(get_current_user)):
#     if current_user["role"].lower() != "sinistre":
#         raise HTTPException(status_code=403, detail="Acces refuse")
#     return {"message": f"Bienvenue au dashboard sinistre {current_user['email']}"}


# # ici -> je recupere les demandes de l'association courante
@association_router.get("/demandes", response_model=List[DemandeOut])
def get_demandes_by_association(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "association":
        raise HTTPException(status_code=403, detail="Acces non autorise")
    
    association = db.query(Association).filter(Association.user_id == current_user["id"]).first()
    
    if not association:
        raise HTTPException(status_code=404, detail="Association introuvable")
    
    return db.query(Demande).filter(Demande.association_id == association.id).all()

# modifier le statut d'une demande par l'association
@association_router.patch("/demandes/{id}/confirmer")
def confirmer_demande(id: int, status_data: StatusUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return confirmer_demande_by_association(id, status_data, db, current_user)


# Supprimer une demande par l'association
@association_router.delete("/demandes/{id}")
def remove_demande_association(id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return delete_demande_by_association(id, db, current_user)