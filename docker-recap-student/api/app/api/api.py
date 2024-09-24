from fastapi import APIRouter

from .auth import auth_router
from .cat import cat_router
from .joke import joke_router
from .prime import prime_router
from .user import user_router
from .author import author_router
from .article import article_router
from .submitter import submitter_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["login"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(cat_router, prefix="/cats", tags=["cat"])
api_router.include_router(prime_router, prefix="/primes", tags=["primes"])
api_router.include_router(joke_router, prefix="/jokes", tags=["joke"])
api_router.include_router(author_router, prefix="/authors", tags=["authors"])
api_router.include_router(article_router, prefix="/articles", tags=["articles"])
api_router.include_router(submitter_router, prefix="/submitters", tags=["submitters"])
