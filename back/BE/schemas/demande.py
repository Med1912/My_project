from pydantic import BaseModel
from typing import Optional
from schemas.status import StatusOut
from schemas.shared_schemas import AssociationOut 
from schemas.Sinistre import SinistreSimpleOut 


class DemandeBase(BaseModel):
    type_aide: str
    description: str

class DemandeCreate(DemandeBase):
    type_aide: str
    description: str
    association_id: int

class DemandeOut(DemandeBase):
    id: int
    type_aide: str
    description: str
    sinistre_id: int
    association_id: Optional[int]
    status: Optional[StatusOut]
    association: Optional[AssociationOut]
    sinistre: Optional[SinistreSimpleOut]  


    class Config:
       from_attributes = True
