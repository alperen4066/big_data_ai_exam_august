from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Index
from sqlalchemy.orm import relationship
from ..db import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    date = Column(DateTime, index=True)  # Index for date-based queries

    author_id = Column(Integer, ForeignKey('authors.id'), index=True)  # Index for join operations
    submitter_id = Column(Integer, ForeignKey('submitters.id'), index=True)  # Index for join operations

    lead_paragraph = Column(Text)
    paragraph = Column(Text)

    author = relationship("Author", back_populates="articles")
    submitter = relationship("Submitter", back_populates="articles", uselist=False)

    # Optionally create a composite index (example):
    __table_args__ = (
        Index('ix_articles_date_author', 'date', 'author_id'),
    )
