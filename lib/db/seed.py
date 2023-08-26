from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Patron, Book, Request

import uuid

fake = Faker()

#if __name__ == '__main__':

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Patron).delete()
session.query(Book).delete()
session.query(Request).delete()

# list of genres
genres = ['Ficton', 'Romance', 'History', 'Autobiography', 'Crime fiction', 'Fantasy',
           'Thriller', 'Mystery', 'Science fiction', 'Graphic', 'Suspense', 'Fairy tale', 'Humor', 'Western']

libraries = ['Fairview', 'Centennial', 'Hillcrest', 'Cedarbrae', 'Ethennonnhawahstihnen']

patrons = [
    Patron(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        phone = int(fake.msisdn()[:10]),
        card_num = int(str(uuid.uuid4().int)[:10])
    #home_branch_id = 1
    )
    for i in range(10)]

session.add_all(patrons)
session.commit()

books = [
    Book(
        title = fake.sentence(nb_words=6),
        genre = random.choice(genres),
        author_first_name = fake.first_name(),
        author_last_name = fake.last_name(),
        ISBN = fake.isbn13(),
        library = random.choice(libraries)
    )
    for i in range(99)]

session.add_all(books)
session.commit()

requests = Request(
    patron_id = random.randint(0,9),
    book_id = random.randint(0,98),
    #branch_id = 1,
    queue = 0
)

session.add_all(requests)
session.commit()

import ipdb; ipdb.set_trace()
