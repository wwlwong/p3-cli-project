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
        #if isinstance(first_name, str) & isinstance(last_name, str) & isinstance(phone, int):
        patron = Patron.create_patron(first_name, last_name, int(phone))
        #session.add(patron)
        #session.commit()
        self.current_patron = patron

        print(f'Welcome to the library {patron.first_name}')
        print(f'Your library card number is {patron.card_num}')
        self.main_menu()
        #else:
            #print('One or more of you inputs is not the correct format, please try again.')
            #self.welcome()

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
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == "Title":
            title_input = input('Please enter book title: ')

        elif menu_entry_index == "Genre":
            genre_input = input('Please enter book genre: ')

        elif menu_entry_index == 'Author':
            author_input = input('Please enter author name: ')

        elif menu_entry_index == 'ISBN-10':
            ISBN_input = input('Please enter ISBN-10 number: ')
        
        else:
            self.main_menu()

    def render_queries(self)


    
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



