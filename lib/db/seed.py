from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Patron, Book, Library, Request

fake = Faker()

if __name__ == '__main__':

    engine = create_engine('sqlite:///library.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    