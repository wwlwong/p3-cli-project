from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///library.db')

Base = declarative_base()

class Patron(Base):
    __tablename__ = 'patrons'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    phone = Column(Integer(), unique=True)
    card_num = Column(Integer(), unique=True)
    #library_id = (Integer(), ForeignKey('libraries.id'))

    #library = relationship("Library", back_populates = 'patrons')
    requests = relationship("Request", backref='patron')
    books = association_proxy('requests', 'book', 
                              creator=lambda bk: Request(book=bk))

    def __repr__(self):

        return f'Patron(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name}, ' + \
            f'card_num={self.card_num})'
    



class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    author_first_name = Column(String())
    author_last_name = Column(String())
    ISBN = Column(String(), unique=True)
    library = (String())

    requests = relationship('Request', backref='book')
    patrons = association_proxy('requests', 'patron',
                                creator=lambda pt: Request(patron=pt))

    def __repr__(self):

        return f'Book(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'genre={self.genre}, ' + \
            f'author_last_name={self.author_last_name}, ' + \
            f'library={self.library}, ' + \
            f'ISBN={self.ISBN})'

#class Library(Base):
#    __tablename__ = 'libraries'

#    id = Column(Integer(), primary_key=True)
#    branch = (String())
#    address = (String())

#    patrons = relationship('Patron', backref='library')
#    books = relationship('Book', backref='library')

#    def __repr__(self):

 #       return f'Library(id={self.id}, ' + \
 #           f'branch={self.branch}, ' + \
 #           f'address={self.address})'

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer(), primary_key=True)
    patron_id = Column(Integer(), ForeignKey('patrons.id'))
    book_id = Column(Integer(), ForeignKey('books.id'))
    #library_id = Column(Integer(), ForeignKey('libraries.id'))
    queue = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())

    def __repr__(self):

        return f'Request(id={self.id}, ' + \
            f'patron_id={self.patron_id}, ' + \
            f'book_id={self.book_id}, ' + \
            f'queue_id={self.queue})'


