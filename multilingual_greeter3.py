from typing import Dict
from random import randrange

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = { 1 : 'English', 2 : 'Castellano', 3 : 'Deutsch'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = { 1 : 'What is your name?', 2 : 'Como te llamas?', 3 : 'Wie heissen Sie?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = { 
    1 : ['Hello', 'How you doing?', 'Good Day'], 
    2 : ['Hola', 'Buenos Dias', 'Other Spanish'], 
    3 : ["Hallo", "Guten Tag", "Wie gehts"]
}

# Use these for state variables if get time to make class and objects
program_mode = 0
function_mode = 0

# Use these and loop through options to print to user, by...
# Replacing the existing prints in choose_program_mode and get_admin_mode_functions
program_modes = { 1: 'Admin', 2: 'User'
}
amdin_functions = { 1: 'Add a language', 2: 'Modify a greeting'}

def choose_program_mode() -> int:
    """
    Prompt the user to select the mode to run the program:  user or admin
    Return an integer
    """
    print('Choose the mode to run the program: 1 for Admin, 2 for User\nAdmin mode allows new languages and greetings to be added\nUser mode geets a user in a selected language')
    while True:
        try:
            program_mode = int(input("Enter 1 or 2 for desired mode: "))
            break
        except:
            print("Not a valid selection. Enter 1 or 2.")
    
    return program_mode

def choose_admin_function() -> int:
    """
    Prompt the user to select the admin mode function
    Return an integer representing selection
    """
    print('Choose an admin function to do:')
    print('1 to add a new language, its greeting and name promp')
    print('2 to modify an existing language')
    while True:
        try:
            function_mode = int(input("Enter 1 or 2 for desired function: "))
            break
        except:
            print("Not a valid selection. Enter 1 or 2.")   
    return function_mode

def get_language_from_user():
    """
    Get a new language to add to the dictionary from an admin
    """
    while True:
        try:
            lang_to_add = str(input("Enter the language to add: "))
        except:
            print("Not a string, languages must be strings [start a-z or A-Z]")

        try:
            does_lang_exist = False
            does_lang_exist == check_language_in_dict(lang_to_add)
            break
        except:
            print("Language already exists, choose a different one")  
            
    return lang_to_add

def check_language_in_dict(lang_add: str) -> bool:
    exists = False
    for i in lang_dict:
        if lang_dict[i] == lang_add:
            exists = True
    return exists
    
def get_greeting_from_user():
    while True:
        try:
            greeting_to_add = str(input("Enter the greeting to add: "))
        except:
            print("Not a string, greetings must be strings [start a-z or A-Z]")

        try:
            does_greeting_exist = False
            does_greeting_exist == check_greeting_in_dict(greeting_to_add)
            break
        except:
            print("Greeting already exists, choose a different one")  
    
    return greeting_to_add

def check_greeting_in_dict(greet_add: str) -> bool:
    exists = False
    for i in greetings_dict:
        if greetings_dict[i] == greet_add:
            exists = True
    return exists

def get_name_prompt_from_user():
    while True:
        try:
            name_prompt_to_add = str(input("Enter the name prompt to add: "))
        except:
            print("Not a string, name prompts must be strings [start a-z or A-Z]")

        try:
            does_name_prompt_exist = False
            does_name_prompt_exist == check_name_prompt_in_dict(name_prompt_to_add)
            break
        except:
            print("Name prompt already exists, choose a different one")  
    
    return name_prompt_to_add 

def check_name_prompt_in_dict(name_prompt_add: str) -> bool:
    exists = False
    for i in name_prompt_dict:
        if name_prompt_dict[i] == name_prompt_add:
            exists = True
    return exists

    
def add_language(lang_add: str, greet_add: str, name_prompt: str) -> None:
    """
    Given a language to add, greeting in that language, and name prompt in that language 
    When method called
    Then add lang to lang_dict, add greeting to greetings_dict, and add name prompt to name_prompt_dict
    """   
    # Just get it working first, then add features to it
    add_language_to_dict(lang_add)
    add_greeting_to_dict(greet_add)
    add_name_prompt_to_dict(name_prompt)
    return None


def add_language_to_dict(lang_add: str):  
    index = len(lang_dict) + 1
    lang_dict[index] = lang_add

def add_greeting_to_dict(greet_add: str):
    index = len(greetings_dict) + 1
    greetings_dict[index] = greet_add

def add_name_prompt_to_dict(name_prompt_add: str):
    index = len(name_prompt_dict) + 1
    name_prompt_dict[index] = name_prompt_add

def choose_greeting_to_modify() -> int:
    print(greetings_dict)
    while True:
        try:
            greeting_to_modify = int(input('Enter the number of the greeting to modify: '))
            break
        except:
            print("Not a valid selection. Enter a number.")
    
    return greeting_to_modify

def get_modified_greeting_from_user() -> str:
    while True:
        try:
            greeting_to_add = str(input("Enter the modified greeting: "))
        except:
            print("Not a string, greetings must be strings [start a-z or A-Z]")

        try:
            does_greeting_exist = False
            does_greeting_exist == check_greeting_in_dict(greeting_to_add)
            break
        except:
            print("Greeting already exists, choose a different one")  
    
    return greeting_to_add


def update_greeting(greetings_dict_index: int, greet_add: str):
    greetings_dict[greetings_dict_index] = greet_add

def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose a language: ')
    for key in lang_options:
        print(f'{key}: {lang_options[key]}') 
    return None

    # remove pass statement and implement me


def select_language() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    keyToVerify = int(input("Enter the number of the langauge you want: "))
    for key in lang_dict:
        if key == int(keyToVerify):
            return key

    # remove pass statement and implement me


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    lang_options_length = len(lang_options)

    if (type(lang_choice) != type(2)):
        return False
    elif (lang_choice > lang_options_length):
        return False
    elif (lang_choice == None):
        return False
    else:
        return True


    # remove pass statement and implement me


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options[lang_choice]
    # remove pass statement and implement me


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    name = input(name_prompt)
    return name
    # remove pass statement and implement me


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    greeting_list = greetings_options[lang_choice]
    random_greeting = get_random_greeting(greeting_list)
    greeting = f"{random_greeting} {name}"
    print(greeting)
      # remove pass statement and implement me

# Function added to get the greeting from the languages greeting list randomly
def get_random_greeting(greetings_options: list) -> str:
    rand_max = len(greetings_options)-1
    random_number = randrange(0, rand_max)
    greeting = greetings_options[random_number]
    return greeting


if __name__ == '__main__':

    # Get the users to select if they want admin or user mode
    continue_program = True
    while(continue_program == True):
    
        program_choice = choose_program_mode()

        # Execute either admin (1) or user (2) mode
        # 1 - Execute Admin mode
        if program_choice == 1:

            #Get the user to select if which admin function they want
            admin_function = choose_admin_function()

            # Execute the selected admin function
            # 1 - add a new language (language name, greeting, name to prompt)
            if admin_function == 1:
                lang_to_add = get_language_from_user()
                greet_to_add = get_greeting_from_user()
                name_prompt_to_add = get_name_prompt_from_user()
                add_language(lang_to_add, greet_to_add, name_prompt_to_add)
                print(f'The {lang_to_add} was added with {greet_to_add} as the greeting and {name_prompt_to_add} as the name.')
            # 2 - modify an existing greeting (greeting to modify, new greeting)
            else:
                greeting_to_modify = choose_greeting_to_modify()
                greet_to_add = get_modified_greeting_from_user()
                update_greeting(greeting_to_modify, greet_to_add)
                print(f'Greeting updated: {greeting_to_modify}: {greet_to_add}')
        # 2 - Execture user mode
        else:
            # Get user to select language for greeting
            print_language_options(lang_dict)
            chosen_lang = select_language()

            # If invalid selection, make them get it right
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = select_language()
            
            # Prompt in selected language user for their name
            selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            
            # Greet user in the selected language using their name
            chosen_name = name_input(selected_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)

        # Prompt user if they want to do more (admin mode changes only exist while program running)
        keep_going = input("Want to do something else? Enter Y/N: ")
        if keep_going == 'Y' or keep_going == 'y':
            continue_program = True
        else:
            continue_program = False
    
    print('Bon Voyage')

