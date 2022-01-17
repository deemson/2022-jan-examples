from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Model(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Model):
    __tablename__ = "users"

    first_name = Column(String)
    last_name = Column(String)


class Product(Model):
    __tablename__ = "products"

    title = Column(String)
    price = Column(Float)
