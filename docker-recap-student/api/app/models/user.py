from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import CHAR
from ..db import Base


# SQLAlchemy model
class User(Base):
    id = Column(CHAR(36), primary_key=True, index=True, default=str(uuid4()))
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(255), unique=True, nullable=False, index=True)
