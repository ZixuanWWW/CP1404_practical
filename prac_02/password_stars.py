MINIMUM_LENGTH = 6

def get_password():
    password = input("Enter the password: ")
    while len(password) <= MINIMUM_LENGTH:
        print("Password is too short. Minimum length is", MINIMUM_LENGTH)
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

def main():
    password = get_password()
    print_asterisks(password)

main()
