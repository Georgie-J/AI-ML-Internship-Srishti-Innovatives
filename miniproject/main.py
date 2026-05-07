from auth import register, login
from exceptions import *
from utils import line

while True:
    line()
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")

    except UserExistsError as e:
        print("Error:", e)

    except InvalidLoginError as e:
        print("Error:", e)
