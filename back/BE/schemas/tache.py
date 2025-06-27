from pydantic import BaseModel

class TacheCreate(BaseModel):
    volontaire_id: int
    demande_id: int

class TacheUpdate(BaseModel):
    status: str

class TacheOut(BaseModel):
    id: int
    status: str
    volontaire_id: int
    demande_id: int

    class Config:
        from_attributes = True
