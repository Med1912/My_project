from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schemas import UserCreate, ShowUser,UserLogin
from db.database import SessionLocal
from models import user_models as models
from crud import user_crud
from auth.hash import verify_password, create_access_token




router = APIRouter(prefix="/users", tags=["Users"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=ShowUser)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.create_user(db, user)
    return db_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if db_user is None or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": db_user.email, "role": db_user.role})


    role = db_user.role.lower()
    if role == "association":
        redirect_url = "/dashboard/association"
    elif role == "volontaire":
        redirect_url = "/dashboard/volontaire"
    elif role == "sinistre":
        redirect_url = "/dashboard/sinistre"
    else:
        redirect_url = "/"

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "nom": db_user.nom,
            "prenom": db_user.prenom,
            "email": db_user.email,
            "role": db_user.role
        },
        "redirect_url": redirect_url
    }

# router = APIRouter(
#     prefix="/associations",
#     tags=["Associations"]
# )

# @router.get("/", response_model=List[AssociationOut])
# def get_all_associations(db: Session = Depends(get_db)):
#     return db.query(Association).all()

# @router.get("/dashboard/association")
# def dashboard_association(current_user: dict = Depends(get_current_user)):
#     if current_user["role"].lower() != "association":
#         raise HTTPException(status_code=403, detail="Acces refuse")
#     return {"message": f"Bienvenue au tableau de bord de l'association {current_user['email']}"}




# @router.get("/dashboard/volontaire")
# def dashboard_volontaire(current_user: dict = Depends(get_current_user)):
#     if current_user["role"].lower() != "volontaire":
#         raise HTTPException(status_code=403, detail="Accès refusé")
#     return {"message": f"Bienvenue au dashboad volontaire {current_user['email']}"}

# @router.get("/dashboard/sinistre")
# def dashboard_sinistre(current_user: dict = Depends(get_current_user)):
#     if current_user["role"].lower() != "sinistre":
#         raise HTTPException(status_code=403, detail="Accès refusé")
#     return {"message": f"Bienvenue au dashboard sinistre {current_user['email']}"}
# ===== Association Router =====
