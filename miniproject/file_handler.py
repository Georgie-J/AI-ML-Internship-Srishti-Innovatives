FILE_NAME = "users.txt"


def save_user(username, password):

    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")


def user_exists(username):

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:

                u, p = line.strip().split(",")

                if u == username:
                    return True

    except FileNotFoundError:
        return False

    return False


def validate_user(username, password):

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:

                u, p = line.strip().split(",")

                if u == username and p == password:
                    return True

    except FileNotFoundError:
        return False

    return False
