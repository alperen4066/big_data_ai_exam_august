from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED
from typing import Any, List
import json

from .dependencies import get_db, get_current_user
from .. import actions
from ..schemas import ArticleCreate, HTTPError, Article
from ..actions import article as article_actions

article_router = APIRouter()

@article_router.get("/", response_model=List[Article], tags=["articles"])
def list_articles(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),  # Require authentication
    skip: int = 0,
    limit: int = 100
) -> Any:
    articles = article_actions.get_all(db=db, skip=skip, limit=limit)
    return articles

@article_router.post("/create", response_model=Article, status_code=HTTP_201_CREATED, tags=["articles"])
def create_article(
    *,
    db: Session = Depends(get_db),
    article_in: ArticleCreate,
    current_user: Any = Depends(get_current_user)  # Require authentication
) -> Any:
    article = article_actions.create(db=db, obj_in=article_in)
    return article

@article_router.post("/upload", status_code=201)
async def upload_articles(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user)  # Require authentication
):
    try:
        content = await file.read()  # Read bytes from the file
        content_str = content.decode('utf-8')  # Decode bytes to string
        articles_data = json.loads(content_str)  # Convert string to dictionary

        # Ensure articles_data is a list of dictionaries
        if not isinstance(articles_data, list) or not all(isinstance(article, dict) for article in articles_data):
            raise HTTPException(status_code=400, detail="Invalid data format. Expected a list of dictionaries.")

        # Call seed_articles with the loaded articles_data
        article_actions.seed_articles(db, articles_data)

        return {"message": "Articles uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
