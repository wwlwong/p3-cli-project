from simple_term_menu import TerminalMenu
from models import Patron, Book, Request
from sqlalchemy import update, delete
from session import session
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine('sqlite:///lib/db/library.db')
#Session = sessionmaker(bind=engine)
#session = Session()


class Cli():

    def __init__(self):
        current_patron = None
        current_book = None

    def welcome(self):
        self.clear_screen()
        print('Choose from the following options')
        options = ['Login', 'Sign-up', 'Exit']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Login":
            self.handle_login()
        elif options[menu_entry_index] == "Sign-up":
            self.handle_signup()
        else:
            self.exit()

    def exit(self):
        print('Thank you for using the library')
        self.current_patron = None

    def handle_signup(self):
        self.clear_screen()
        first_name = input('Please enter your first name: ')
        last_name = input('Please enter your last name: ')
        phone = input('Please enter your 10 digit phone number in this format xxxxxxxxxx: ')
        patron = Patron.create_patron(first_name, last_name, int(phone))
        self.current_patron = patron
        print(f'Welcome to the library {patron.first_name}')
        print(f'Your library card number is {patron.card_num}')
        self.main_menu()
        

    def handle_login(self):
        self.clear_screen()
        card_num = int(input("Please enter your library card number: "))
        patron = Patron.find_by(session, card_num=card_num)
        if patron:
            phone = input("Please enter the last 4 digits of your phone number: ")
            if phone == str(patron.phone)[-4:]:
                print(f'Welcome to the library, {patron.first_name}')
                self.current_patron = patron
                self.main_menu()
            else:
                print ('The number entered is incorrect, please login again ')
                self.welcome()
        else:
            print('The library card number was not found. Please try again ')
            self.welcome()
            
    def clear_screen(self):
        print('\n' * 20)

    def main_menu(self):
        time.sleep(1)
        self.clear_screen()
        patron = session.query(Patron).filter(Patron.id == self.current_patron.id)
        request = session.query(Request).filter(Request.patron_id == self.current_patron.id)
        options = []
        print('Choose from the following options')
        if request.count() != 0:
            options.extend(['Search', 'Update Info', 'View requests', 'Exit'])
        else:
            options.extend(['Search', 'Update Info', 'Exit'])
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == 'Search':
            self.search()
        elif options[menu_entry_index] == "Update Info":
            self.patron_update()
        elif options[menu_entry_index] == 'View requests':
            self.render_request()
        else:
            self.exit()

    def patron_update(self):
        self.clear_screen()
        print('Which would you like to update?')
        options = ['First name', 'Last name', 'Phone']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == 'First name':
            first_name = input('Please enter new first name: ')
            self.current_patron.update_info(session, self.current_patron.id, 'first_name', first_name)
        elif options[menu_entry_index] == 'Last name':
            last_name = input('Please enter new last name: ')
            self.current_patron.update_info(session, self.current_patron.id, 'last_name', last_name)
        else:
            phone = int(input('Please enter new phone number: '))
            self.current_patron.update_info(session, self.current_patron.id, 'phone', phone)
        
        self.main_menu()

        

    def search(self):
        self.clear_screen()
        print('How would you like to search by? ')
        options = ['Title', 'Genre', 'Author', 'ISBN-10', 'Return to main menu']
        selection = self.render_options(options)

        if selection == 'Return to main menu':
            self.main_menu()
        elif selection == "Title":
            title_input = input('Please enter book title: ')
            queries = session.query(Book).filter(Book.title.ilike(title_input))
            #queries = Book.query_by(session, 'title', title_input)
        elif selection == "Genre":
            genre_input = input('Please enter book genre: ')
            queries = session.query(Book).filter(Book.genre.ilike(genre_input))
            #queries = Book.query_by(session, 'genre', genre_input)
        elif selection == 'Author':
            author_input = input('Please enter author name: ')
            queries = session.query(Book).filter(Book.author_name.ilike(author_input))
            #queries = Book.query_by(session, 'author_name', author_input)
        elif selection == 'ISBN-10':
            ISBN_input = input('Please enter ISBN-10 number: ')
            queries = session.query(Book).filter(Book.ISBN.ilike(ISBN_input))
            #queries = Book.query_by(session, 'ISBN', ISBN_input)
        
        time.sleep(2)
        if queries.count() == 0:
            print ('Sorry, there is no record in the library')
            self.main_menu()
        else:
            self.render_queries(queries)

    def render_queries(self, queries):
        self.clear_screen()
        book_queries = [f'{query.id} - {query.title} - {query.author_name}' for query in queries]
        book_queries.append("Back")
        selection = self.render_options(book_queries)

        if selection == "Back":
            self.search()
        else:
            selection_id = int(selection.split('-')[0].strip())
            book = session.query(Book).get(selection_id)
            self.current_book = book
            self.render_book_option(book, queries)
    
    def render_book_option(self, book, queries):
        self.clear_screen()
        book_info = session.query(Book).get(book.id)
        print(book_info)
        options = ['Request book', 'Search results']
        selection = self.render_options(options)

        if selection == 'Search results':
            self.render_queries(queries)
            self.current_book = None
        else:
            book_id = book.id
            existing_requests = session.query(Request).filter(Request.book_id == book.id)
            new_request = Request.create_request(self.current_patron.id, self.current_book.id, existing_requests.count())
            session.add(new_request)
            session.commit()
            self.render_queries(queries)


    def handle_request(self):
        request_queue = session.query(Request).filter(Request.book_id == self.current_book.id)
        request = Request.create_request(self.current_patron.id, self.current_book.id, request_queue.count())
        print ("Book requested")
        time.sleep(2)
        self.main_menu()

    
    def render_options(self, options):
        menu = TerminalMenu(options)
        selection = menu.show()
        return options[selection]
    
    def render_request(self):
        self.clear_screen()
        patron_requests = [f'{request.id} - {request.book.title}' for request in self.current_patron.requests]
        patron_requests.append("Main menu")
        selection = self.render_options(patron_requests)

        if selection == "Main menu":
            self.main_menu()
        else:
            selection_id = int(selection.split('-')[0].strip())
            self.render_request_option(session.query(Request).get(selection_id))

    def render_request_option(self, request):
        self.clear_screen()
        book_info = session.query(Book).get(request.book_id)
        print(book_info)
        options = ['Delete', 'Previous menu']
        selection = self.render_options(options)

        if selection == 'Previous menu':
            self.render_request()
        else:
            book_id = request.book_id
            session.delete(request)
            for book_request in session.query(Request).filter(Request.book_id == book_id):
                book_request.queue -= 1
            session.commit()
            self.main_menu()
        






app = Cli()
app.welcome()



