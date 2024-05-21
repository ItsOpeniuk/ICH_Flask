from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine(url='mysql+pymysql://root:24329611Aa@localhost:3306/alchemy_db')
