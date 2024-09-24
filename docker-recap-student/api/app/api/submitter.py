from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from .dependencies import get_db, get_current_user
from .. import actions
from ..schemas import Submitter, SubmitterCreate, HTTPError

submitter_router = APIRouter()


@submitter_router.get("/", response_model=List[Submitter], tags=["submitters"])
def list_submitters(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),  # Require authentication
    skip: int = 0,
    limit: int = 100
) -> Any:
    submitters = actions.submitter.get_all(db=db, skip=skip, limit=limit)
    return submitters


@submitter_router.post(
    "/create", response_model=Submitter, status_code=HTTP_201_CREATED, tags=["submitters"]
)
def create_submitter(
    *,
    db: Session = Depends(get_db),
    submitter_in: SubmitterCreate,
    current_user: Any = Depends(get_current_user)  # Require authentication
) -> Any:
    submitter = actions.submitter.create(db=db, obj_in=submitter_in)
    return submitter
