LENGTH = 6


def main():
    password = get_valid_password()
    password_length = len(password)
    print_asterix(password_length)


def get_valid_password():
    password = input("Enter a password: ")
    while len(password) < LENGTH:
        print("Password is too short.")
        password = input("Enter a password: ")
    return password


def print_asterix(length):
    for i in range(length):
        print("*", end="")


main()
