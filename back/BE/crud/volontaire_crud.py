from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.demande import Demande
from models.user_models import Association, Volontaire
from models.tache import Tache





def get_all_associations(db):
    return db.query(Association).all()

def get_demandes_par_association(db):
    return db.query(Demande).filter(Demande.association_id != None).all()

def assign_tache_to_volontaire(demande_id: int, db, current_user):
    if current_user.get("role") != "volontaire":
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    volontaire = db.query(Volontaire).filter(Volontaire.user_id == current_user.get("id")).first()
    if not volontaire:
        raise HTTPException(status_code=404, detail="Volontaire introuvable")

    demande = db.query(Demande).filter(Demande.id == demande_id).first()
    if not demande:
        raise HTTPException(status_code=404, detail="Demande introuvable")

    tache_existante = db.query(Tache).filter(Tache.demande_id == demande_id, Tache.volontaire_id == volontaire.id).first()
    if tache_existante:
        raise HTTPException(status_code=400, detail="Vous avez déjà pris en charge cette demande")

    tache = Tache(
        titre=f"Aide pour {demande.type_aide}",
        description=demande.description,
        volontaire_id=volontaire.id,
        demande_id=demande.id
    )
    db.add(tache)
    db.commit()
    db.refresh(tache)
    return tache

def get_taches_by_volontaire(db, current_user):
    if current_user.get("role") != "volontaire":
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    volontaire = db.query(Volontaire).filter(Volontaire.user_id == current_user.get("id")).first()
    if not volontaire:
        raise HTTPException(status_code=404, detail="Volontaire introuvable")

    return db.query(Tache).filter(Tache.volontaire_id == volontaire.id).all()
