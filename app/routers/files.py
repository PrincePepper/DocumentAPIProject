import json

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import File

from ..document_class import DocumentClass
from ..repositories.contents import ContentsRepository
from ..repositories.documents import DocumentsRepository
from ..schemas.contents import Content
from ..schemas.documents import Document

router = APIRouter(prefix="/files", tags=["files"])


@router.post("/")
async def add_file(file: bytes = File(...),
                   documents: DocumentsRepository = Depends(),
                   contents: ContentsRepository = Depends()):
    doc = DocumentClass()
    doc.serializeDocumentString(file.decode("utf-8").replace('\r\n', ','))
    doc_json = doc.getDocument()
    header = doc_json[0]
    header['number'] = int(header['number'])
    temp_doc = Document(**header)
    documents.create(temp_doc)
    for i in doc_json[1]:
        temp_content = Content(name=i['name'], amount=int(i['amount']), price=float(i['price']),
                               sum=float(i['sum']),
                               number=int(header['number']))
        contents.create(temp_content)
    return doc_json


@router.get("/{file_id}")
async def get_file(file_number: int,
                   documents: DocumentsRepository = Depends(),
                   contents: ContentsRepository = Depends()):
    db_documents = documents.find(file_number)
    if db_documents is None:
        raise HTTPException(
            status_code=404,
            detail=f'Document {file_number} not found'
        )

    db_contents = contents.find(file_number)
    header = Document.from_orm(db_documents)
    aaa = []
    for i in db_contents:
        aaa.append(Content.from_orm(i).dict())
    ccc = header.dict()
    bbb = [ccc, aaa]
    doc = DocumentClass()
    doc.json = json.dumps(bbb)
    doc.deserializeDocument('test.json')
    return bbb
