from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from .dependencies import get_db, get_current_user
from .. import actions
from ..schemas import Author, AuthorCreate, HTTPError

author_router = APIRouter()


@author_router.get("/", response_model=List[Author], tags=["authors"])
def list_authors(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),  # Require authentication
    skip: int = 0,
    limit: int = 100
) -> Any:
    authors = actions.author.get_all(db=db, skip=skip, limit=limit)
    return authors


@author_router.post(
    "/create", response_model=Author, status_code=HTTP_201_CREATED, tags=["authors"]
)
def create_author(
    *,
    db: Session = Depends(get_db),
    author_in: AuthorCreate,
    current_user: Any = Depends(get_current_user)  # Require authentication
) -> Any:
    author = actions.author.create(db=db, obj_in=author_in)
    return author
