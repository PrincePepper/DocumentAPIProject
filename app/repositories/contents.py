from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.content import Content


class ContentsRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db  # произойдет внедрение зависимостей

    def find(self, uuid: int) -> List[Content]:
        query = self.db.query(Content)
        return query.filter(Content.number == uuid).all()

    def all(self, skip: int = 0, max: int = 100) -> List[Content]:
        query = self.db.query(Content)
        return query.offset(skip).limit(max).all()

    def create(self, document: Content) -> Content:
        db_content = Content(**document.dict())

        self.db.add(db_content)
        self.db.commit()
        self.db.refresh(db_content)

        return db_content
