
from pydantic import BaseModel
class UserOut(BaseModel):
    nom: str
    prenom: str

    class Config:
        from_attributes = True
