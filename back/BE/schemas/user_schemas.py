from pydantic import BaseModel, EmailStr
from typing import List, Optional
from schemas.demande import DemandeOut
from schemas.shared_schemas import AssociationOut 

class UserCreate(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    password: str
    role: str 
    association_nom: Optional[str] = None 
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ShowUser(BaseModel):
    id: int
    nom: str
    prenom: str
    email: EmailStr
    # role: str

    class Config:
        orm_mode = True
        # from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class SinistreOut(BaseModel):
    id: int
    user_id: int
    demandes: List[DemandeOut]

    class Config:
        # orm_mode = True
        from_attributes = True    
class AssociationOut(BaseModel):
    id: int
    nom: str
    location: Optional[str]
    # user:ShowUser
    email: str 
    latitude: Optional[float]
    longitude: Optional[float]

    class Config:
        from_attributes = True