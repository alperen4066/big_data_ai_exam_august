from datetime import datetime
from sqlalchemy.orm import Session

from ..actions.base import BaseActions
from ..models import Article, Author, Submitter
from ..schemas import ArticleCreate, ArticleUpdate


class ArticleActions(BaseActions[Article, ArticleCreate, ArticleUpdate]):
    """Article actions with basic CRUD operations"""

    def seed_articles(self, db_session: Session, articles_data: dict):
        for article_data in articles_data:
            author_data = article_data['author']
            submitter_data = article_data.get('submitter', {})  # Get submitter data with default empty dictionary if not present
            submitter_name = submitter_data.get('name', '')  # Get submitter name with default empty string if not present
            submitter_id = submitter_data.get('id', '')  # Get submitter ID with default empty string if not present
            
            # Check if author exists, if not, create new
            author = db_session.query(Author).filter(Author.name.ilike(author_data['name'])).first()
            if not author:
                author = Author(name=author_data['name'], function=author_data['function'])
                db_session.add(author)
                db_session.commit()

            # Check if submitter exists, if not, create new
            if submitter_name:  # Check if submitter name is not empty
                submitter = db_session.query(Submitter).filter(Submitter.name.ilike(submitter_name)).first()
                if not submitter:
                    submitter = Submitter(name=submitter_name)
                    db_session.add(submitter)
                    db_session.commit()
            else:
                submitter = None  # Set submitter to None if submitter name is empty

            # Create the article
            article = Article(
                title=article_data['title'],
                date=datetime.fromtimestamp(article_data['date']),
                author_id=author.id,
                submitter_id=submitter.id if submitter else None,  # Use submitter ID if submitter exists, otherwise None
                lead_paragraph=article_data['lead_paragraph'],
                paragraph='\n'.join(article_data['additional_paragraphs'])
            )
            db_session.add(article)

        db_session.commit()
        print("Articles seeded successfully!")

# Initialize ArticleActions instance
article = ArticleActions(Article)
