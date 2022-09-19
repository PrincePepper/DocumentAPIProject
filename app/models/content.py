from sqlalchemy import Column, String, Float, MetaData, Integer

from ..database import Model

metadata = MetaData()


class Content(Model):
    __tablename__ = "content"
    __metadata__ = metadata

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    amount = Column('amount', Integer, nullable=False)
    price = Column('price', Float, nullable=False)
    sum = Column('sum', Float, nullable=False)
    number = Column('number', Integer, nullable=False)  # ForeignKey('document.number')
