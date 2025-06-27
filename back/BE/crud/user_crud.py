from sqlalchemy.orm import Session
from models import user_models as models
from schemas.user_schemas import UserCreate
from auth.hash import hash_password

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        nom=user.nom,
        prenom=user.prenom,
        email=user.email,
        password=hashed_password,
        role=user.role,
        association_nom=user.association_nom,
        latitude=user.latitude,
        longitude=user.longitude
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    if user.role.lower() == "association":
        association_name = user.association_nom if user.association_nom else user.nom
        db_asso = models.Association(
            nom=association_name,
            location="non defini",
            user_id=db_user.id,
          
        )
        db.add(db_asso)

    elif user.role.lower() == "volontaire":
        db.add(models.Volontaire(user_id=db_user.id))

    elif user.role.lower() == "sinistre":
        db.add(models.Sinistre(user_id=db_user.id))
    db.commit()
    return db_user
