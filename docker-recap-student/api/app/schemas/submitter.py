from typing import Optional
from pydantic import BaseModel

class SubmitterBase(BaseModel):
    name: str

class SubmitterCreate(SubmitterBase):
    pass

class SubmitterUpdate(SubmitterBase):
    pass

class Submitter(SubmitterBase):
    id: int

    class Config:
        from_attributes = True
