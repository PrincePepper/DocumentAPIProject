from sqlalchemy import Column, String, Float, MetaData, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..database import Model

metadata = MetaData()


class Document(Model):
    __tablename__ = "documents"
    __metadata__ = metadata

    id = Column('id', Integer, primary_key=True)
    number = Column('number',Integer,nullable=False)
    date = Column('date',String,nullable=False)
    comment = Column('comment',String,nullable=False)
