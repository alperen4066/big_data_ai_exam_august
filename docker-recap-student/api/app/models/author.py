from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    function = Column(String(255), index=True)  # Index for role-based queries

    articles = relationship("Article", back_populates="author")
