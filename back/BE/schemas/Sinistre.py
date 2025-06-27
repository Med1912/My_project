from pydantic import BaseModel
from schemas.user_out import UserOut

class SinistreSimpleOut(BaseModel):
    user: UserOut

    class Config:
        from_attributes = True
