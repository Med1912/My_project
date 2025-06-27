from pydantic import BaseModel

class AssociationOut(BaseModel):
    id: int
    nom: str
    email: str

    class Config:
        from_attributes = True
