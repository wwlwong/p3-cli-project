from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Patron, Book, Library, Request

import uuid

fake = Faker()

#if __name__ == '__main__':

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

# list of genres
genres = ['Ficton', 'Romance', 'History', 'Autobiography', 'Crime fiction', 'Fantasy',
           'Thriller', 'Mystery', 'Science fiction', 'Graphic', 'Suspense', 'Fairy tale', 'Humor', 'Western']

patron1 = Patron(
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    phone = int(fake.msisdn()[:10]),
    card_num = int(str(uuid.uuid4().int)[:10]),
    home_branch_id = 1
)

book1 = Book(
    title = fake.sentence(nb_words=6),
    genre = random.choice(genres),
    author_first_name = fake.first_name(),
    author_last_name = fake.last_name(),
    ISBN = fake.isbn13(),
    branch_id = 1
)


