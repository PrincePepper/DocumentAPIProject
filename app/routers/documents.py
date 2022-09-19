from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as

from ..repositories.documents import DocumentsRepository
from ..schemas.documents import Document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/", response_model=List[Document])
def list_document(skip: int = 0, max: int = 10, documents: DocumentsRepository = Depends()):
    db_documents = documents.all(skip=skip, max=max)
    return parse_obj_as(List[Document], db_documents)


@router.post("/", response_model=Document, status_code=status.HTTP_201_CREATED)
def store_document(document: Document, documents: DocumentsRepository = Depends()):

    db_documents = documents.create(document)
    return Document.from_orm(db_documents)


@router.get("/{document_id}", response_model=Document)
def get_document(document_number: int, documents: DocumentsRepository = Depends()):
    db_documents = documents.find(document_number)
    if db_documents is None:
        raise HTTPException(
            status_code=404,
            detail=f'Document {document_number} not found'
        )

    return Document.from_orm(db_documents)