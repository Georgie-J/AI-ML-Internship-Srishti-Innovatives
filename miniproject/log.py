from datetime import datetime

def write_log(message):

    with open("activity.log", "a") as file:
        file.write(f"{datetime.now()} - {message}\n")
