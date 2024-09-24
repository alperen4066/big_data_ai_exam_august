from typing import Optional
from pydantic import BaseModel
from .author import Author
from .submitter import Submitter
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    date: datetime
    author_id: int
    submitter_id: Optional[int]
    lead_paragraph: str
    paragraph: str


class ArticleCreate(ArticleBase):
    submitter_id: Optional[int] = None

class ArticleUpdate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        from_attributes = True
