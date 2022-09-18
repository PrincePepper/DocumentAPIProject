from pydantic import BaseModel


# Основная схема
class ContentBase(BaseModel):
    name: str
    amount: int
    price: float
    sum: float

    class Config:
        schema_extra = {
            "example": {
                "name": "яблоко",
                "amount": 1,
                "price": 12.1,
                "sum": 12.1,
            }
        }


# default schema to return on a response
class Content(ContentBase):
    number: int

    class Config:
        orm_mode = True  # помогает связать модель со схемой

        schema_extra = {
            "example": {
                **ContentBase.Config.schema_extra.get("example"),
                "number": 12,
            }
        }
