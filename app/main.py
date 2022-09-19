from fastapi import FastAPI

from app.database import engine, Model
from app.database import get_db
from app.routers import documents, contents, files

Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(documents.router)
app.include_router(contents.router)
app.include_router(files.router)

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    print(get_db)
