def version_1():
    MIN_LENGTH = 5
    MAX_LENGTH = 15
    password = input("Enter a password with a minimum of 5 and a maximum of 15: ")
    while len(password) < MIN_LENGTH:
        password = input("Password is too short, please try again: ")
        while len(password) > MAX_LENGTH:
            password = input("Password is too long, please try again: ")

    print('*' * len(password))


version_1()

def main():
    MIN_LENGTH = 5
    MAX_LENGTH = 15
    get_password(MAX_LENGTH, MIN_LENGTH)


def get_password(MAX_LENGTH, MIN_LENGTH):
    password = input("Enter a password with a minimum of 5 and a maximum of 15: ")
    while len(password) < MIN_LENGTH:
        password = input("Password is too short, please try again: ")
        while len(password) > MAX_LENGTH:
            password = input("Password is too long, please try again: ")
    print_password(password)


def print_password(password):
    print('*' * len(password))


main()
