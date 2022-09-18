from uuid import uuid4

from sqlalchemy import Column, String, Float, MetaData, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..database import Model

metadata = MetaData()


class Content(Model):
    __tablename__ = "content"
    __metadata__ = metadata

    id = Column('id', Integer, primary_key=True)
    document_number = Column('number', Integer, ForeignKey('document.number'), nullable=False)
    name = Column('name', String, nullable=False)
    amount = Column('amount', Integer, nullable=False)
    price = Column('price', Float, nullable=False)
    sum = Column('sum', Float, nullable=False)
