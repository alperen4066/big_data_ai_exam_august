from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from ..db import Base

class Article(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    date = Column(DateTime)

    author_id = Column(Integer, ForeignKey('authors.id'))
    submitter_id = Column(Integer, ForeignKey('submitters.id'))
    lead_paragraph = Column(Text)
    paragraph = Column(Text)

    author = relationship("Author", back_populates="articles")
    submitter = relationship("Submitter", back_populates="articles", uselist=False)
