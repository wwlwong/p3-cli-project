from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///library.db')

Base = declarative_base()

class Patron(Base):
    __tablename__ = 'patrons'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    phone = Column(Integer())
    card_num = Column(Integer())
    home_branch = (String())


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    subject = Column(String())
    author_first_name = Column(String())
    author_last_name = Column(String())
    ISBN = Column(Integer())
    branch = (String())

