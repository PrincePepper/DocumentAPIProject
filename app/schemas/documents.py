from uuid import UUID

from pydantic import BaseModel


# Основная схема
class DocumentBase(BaseModel):
    number: int
    date: str
    comment: str

    class Config:
        schema_extra = {
            "example": {
                "number": 12,
                "date": '10.11.2001',
                "comment": "ку ку",
            }
        }



# default schema to return on a response
class Document(DocumentBase):
    class Config:
        orm_mode = True  # TL;DR; помогает связать модель со схемой

        schema_extra = {
            "example": {
                **DocumentBase.Config.schema_extra.get("example"),
            }
        }
