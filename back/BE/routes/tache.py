from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.tache import Tache
from schemas.tache import TacheCreate, TacheOut, TacheUpdate
from auth.middleware import get_current_user

router = APIRouter(
    prefix="/taches",
    tags=["Taches"]
)

@router.post("/", response_model=TacheOut)
def participer_tache(tache_data: TacheCreate, db: Session = Depends(get_db)):
    existing = db.query(Tache).filter_by(
        volontaire_id=tache_data.volontaire_id,
        demande_id=tache_data.demande_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="deja inscrit a cette tache!!!")

    tache = Tache(**tache_data.dict())
    db.add(tache)
    db.commit()
    db.refresh(tache)
    return tache

@router.put("/{tache_id}", response_model=TacheOut)
def update_tache(tache_id: int, update_data: TacheUpdate, db: Session = Depends(get_db)):
    tache = db.query(Tache).filter_by(id=tache_id).first()
    if not tache:
        raise HTTPException(status_code=404, detail="tache non trouver")

    tache.status = update_data.status
    db.commit()
    db.refresh(tache)
    return tache


@router.get("/mes-taches", response_model=list[TacheOut])
def get_mes_taches(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if current_user["role"].lower() != "volontaire":
        raise HTTPException(status_code=403, detail="acces refuser")

    taches = db.query(Tache).filter(Tache.volontaire_id == current_user["id"]).all()
    return taches
