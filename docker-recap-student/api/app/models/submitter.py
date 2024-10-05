from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base

class Submitter(Base):
    __tablename__ = 'submitters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    articles = relationship("Article", back_populates="submitter")
