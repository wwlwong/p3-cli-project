from simple_term_menu import TerminalMenu
from models import Patron, Book, Request
from sqlalchemy import update, delete

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
        first_name = input('Please enter your first name')
        last_name = input('Please enter your last name')
        phone = input('Please enter your 10 digit phone number in this format xxxxxxxxxx')
        if isinstance(first_name, str) & isinstance(last_name, str) & isinstance(phone, int):
            patron = Patron.create_patron(first_name, last_name, phone)

            self.current_patron = patron

            print(f'Welcome to the library {patron.first_name}')
            print(f'Your library card number is {patron.card_num}')
        else:
            print('One or more of you inputs is not the correct format, please try again.')
            self.welcome()

    def handle_login(self):
        self.clear_screen()
        card_num = input("Please enter your library card number")
        patron = Patron.find_by(card_num=card_num)
        if patron:
            phone = input("Please enter the last 4 digits of your phone number")
            if str(phone) == str(patron.phone)[-4:]:
                print(f'Welcome to the library, {patron.first_name}')
                self.current_patron = patron
                self.main_menu()
            else:
                print ('The number entered is incorrect, please login again')
                self.welcome()
        else:
            print('The library card number was not found. Please try again')
            self.welcome()
            
    def clear_screen(self):
        print('\n' * 20)

    def main_menu(self):
        self.clear_screen()
        options = []
        print('Choose from the following options')
        if self.current_patron.requests:
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
        patron = session.Query(Patron)
        self.clear_screen()
        print('Which would you like to update?')
        options = ['First name', 'Last name', 'Phone']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == 'First name':
            first_name = input('Please enter new first name')
        elif options[menu_entry_index] == 'Last name':
            last_name = input('Please enter new last name')
        else:
            phone = input('Please enter new phone number')

        self.current_patron.update




