from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('mysql+pymysql://root:24329611Aa@localhost:3306/alchemy_db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Product(Base):

    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(scale=5, precision=5), nullable=False)
    in_stock = Column(Boolean, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Category(Base):

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text(255), nullable=True)


Base.metadata.create_all(engine)
session.close()
