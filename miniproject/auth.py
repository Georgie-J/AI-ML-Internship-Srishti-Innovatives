from file_handler import *
from exceptions import *
from log import write_log

def register():

    username = input("Enter username: ")
    password = input("Enter password: ")

    if user_exists(username):
        raise UserExistsError("User already exists")

    save_user(username, password)

    write_log(f"{username} registered")

    print("Registration successful")


def login():

    attempts = 3

    while attempts > 0:

        username = input("Enter username: ")
        password = input("Enter password: ")

        if validate_user(username, password):

            write_log(f"{username} logged in")

            print("Login successful")
            return

        else:
            attempts -= 1
            print("Invalid credentials")

    raise InvalidLoginError("Too many attempts")
