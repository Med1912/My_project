from sqlalchemy.orm import Session 
from models.demande import Demande
from models.status import Status
from fastapi import  HTTPException
from schemas.demande import DemandeCreate
from models.user_models import Sinistre ,Association




def create_demande(
    db: Session, demande: DemandeCreate, current_user: dict
):
    print(" entre !!!") 
    try:
        print(" current_user:", current_user)
        if not current_user or "role" not in current_user or "id" not in current_user:
            raise HTTPException(status_code=400, detail="Utilisateur invalide (token incomplet)")

        if current_user["role"] != "sinistre":
            raise HTTPException(status_code=403, detail="Seuls les sinistrés peuvent créer une demande")
        sinistre = db.query(Sinistre).filter(Sinistre.user_id == current_user["id"]).first()
        print("==> sinistre found:", sinistre)

        if not sinistre:
            raise HTTPException(status_code=404, detail="Sinistre non trouve pour cet utilisateur")
        if not demande.type_aide or not demande.description or not demande.association_id:
            raise HTTPException(status_code=400, detail="Champs de la demande incomplets")

        new_demande = Demande(
            type_aide=demande.type_aide,
            description=demande.description,
            association_id=demande.association_id,
            sinistre_id=sinistre.id
        )
        print(" creating demande:", new_demande)
        db.add(new_demande)
        db.commit()
        db.refresh(new_demande)
        print("new_demande created:", new_demande)

        new_status = Status(
            etat="en attente",
            demande_id=new_demande.id
        )
        print("==> creating status:", new_status)
        db.add(new_status)
        db.commit()
        db.refresh(new_status)
        print("==> status added:", new_status)

        return new_demande

    except HTTPException as http_err:
        print("http err!!:", str(http_err.detail))
        raise http_err

    except Exception as e:
        print("!! UNEXPECTED ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Erreur interne du serveur.")




def get_all_demandes(db:Session):
    return db.query(Demande).all()


def get_demande_by_id(db:Session, demande_id: int):
    return db.query(Demande).filter(Demande.id == demande_id).first()


# ---------------------------------------------------------------'''
def delete_demande_by_sinistre(id: int, db, current_user):
    if current_user.get("role") != "sinistre":
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    sinistre = db.query(Sinistre).filter(Sinistre.user_id == current_user.get("id")).first()
    if not sinistre:
        raise HTTPException(status_code=404, detail="Sinistre non trouvé pour cet utilisateur")

    demande = db.query(Demande).filter(Demande.id == id).first()
    if not demande:
        raise HTTPException(status_code=404, detail="Demande non trouvée")

    if demande.status and demande.status.etat != "en attente":
        raise HTTPException(status_code=403, detail="Vous ne pouvez supprimer que les demandes en attente")

    db.delete(demande)
    db.commit()
    return {"message": "Demande supprimée avec succès"}

# -------------------------------------------------------------

# modifier le statut d'une demande par l'association
def confirmer_demande_by_association(id: int, status_data, db, current_user):
    if current_user.get("role") != "association":
        raise HTTPException(status_code=403, detail="Accès non autorisé")
    demande = db.query(Demande).filter(Demande.id == id).first()
    if not demande:
        raise HTTPException(status_code=404, detail="Demande non trouvée")

    association = db.query(Association).filter(Association.user_id == current_user.get("id")).first()
    if not association or demande.association_id != association.id:
        raise HTTPException(status_code=403, detail="Accès refusé")
    status = db.query(Status).filter(Status.demande_id == id).first()
    if not status:
        raise HTTPException(status_code=404, detail="Status introuvable ")
    status.etat = status_data.etat
    db.commit()
    return {"message": "Statut de la demande modifié avec succes"}


# # Supprimer une demande par l'association

def delete_demande_by_association(id: int, db: Session, current_user: dict):
    if current_user.get("role") != "association":
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    association = db.query(Association).filter(Association.user_id == current_user.get("id")).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association introuvable")

    demande = db.query(Demande).filter(Demande.id == id).first()
    if not demande:
        raise HTTPException(status_code=404, detail="Demande non trouvée")

    
    if demande.association_id != association.id:
        raise HTTPException(status_code=403, detail="Vous ne pouvez supprimer que les demandes liées à votre association")

    if demande.status and demande.status.etat != "en attente":
        raise HTTPException(status_code=403, detail="Vous ne pouvez supprimer que les demandes en attente")

    db.delete(demande)
    db.commit()
    return {"message": "Demande supprimée avec succès"}
