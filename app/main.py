from fastapi import FastAPI, File, UploadFile

from app.database import engine, Model
from app.database import get_db
from app.document_class import Document
from app.routers import documents, contents

Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(documents.router)
app.include_router(contents.router)


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    doc=Document()
    doc.serializeDocumentString(file.decode("utf-8").replace('\r\n', ','))
    doc_json=doc.getDocument()
    return {"file_size": type(doc_json)}


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    print(get_db)
