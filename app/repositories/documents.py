from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.document import Document


class DocumentsRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db  # произойдет внедрение зависимостей

    def find(self, uuid: int):
        query = self.db.query(Document)
        return query.filter(Document.number == uuid).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Document]:
        query = self.db.query(Document)
        return query.offset(skip).limit(max).all()

    def create(self, document: Document) -> Document:
        db_document = Document(**document.dict())

        self.db.add(db_document)
        self.db.commit()
        self.db.refresh(db_document)

        return db_document
