from sqlalchemy import Column, Integer, Numeric, String, Boolean, Text, ForeignKey
from hw4_sqlalchemy import Base, engine
from sqlalchemy.orm import relationship


class Categories(Base):

    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(20), nullable=False)
    description = Column(Text(500), nullable=False)

    products = relationship('Product', back_populates='category')

class Product(Base):

    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String(30), nullable=False)
    price = Column(Numeric(scale=2, precision=8), nullable=False)
    in_stock = Column(Boolean, nullable=False)

    category = relationship('Categories', back_populates='products')


Base.metadata.create_all(engine)
