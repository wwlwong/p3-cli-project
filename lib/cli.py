from simple_term_menu import TerminalMenu
from models import Patron, Book, Request

class Cli():

    def __init__(self):
        current_patron = None

    def welcome(self):
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

    def handle_signup(self):
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




