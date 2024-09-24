# actions/author_actions.py
from sqlalchemy.orm import Session
from app.models import Author
from app.schemas import AuthorCreate, AuthorUpdate
from ..actions.base import BaseActions

class AuthorActions(BaseActions[Author, AuthorCreate, AuthorUpdate]):
    """Author actions with basic CRUD operations"""

    # Define additional methods for author-related operations here


author = AuthorActions(Author)