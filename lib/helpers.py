from simple_term_menu import TerminalMenu

def login():
    print('Choose from the following options')
    options = ['login', 'sign-up', 'exit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f'You have selected {options[menu_entry_index]}')