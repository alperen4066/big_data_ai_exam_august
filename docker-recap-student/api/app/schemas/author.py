# schemas/author.py

from typing import Optional
from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str
    function: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True
