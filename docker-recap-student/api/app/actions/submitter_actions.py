# actions/submitter_actions.py
from sqlalchemy.orm import Session
from app.models import Submitter
from app.schemas import SubmitterCreate, SubmitterUpdate
from ..actions.base import BaseActions

class SubmitterActions(BaseActions[Submitter, SubmitterCreate, SubmitterUpdate]):
    """Submitter actions with basic CRUD operations"""

    # Define additional methods for submitter-related operations here


submitter = SubmitterActions(Submitter)