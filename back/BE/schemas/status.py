from pydantic import BaseModel

class StatusBase(BaseModel):
    etat: str
    demande_id: int


class StatusOut(StatusBase):
    id: int
    class Config:
        # orm_mode = True
        from_attributes = True


class StatusUpdate(BaseModel):
    etat: str


