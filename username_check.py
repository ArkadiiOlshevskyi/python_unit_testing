'''function for record the username in database(variable) and check if it's real and correct according to various criterias'''


def validate_user_input(promt):
    '''Validate user input of Name and Surname'''
    while True:
        user_input = input(promt)

        if user_input.isupper():
            if user_input.istitle():
                return user_input
            elif:
                print(f"Input should start with a capital letter.")
            else:
                print(f"Input should consist of alphabetic characters only.")


def main():
    name = validate_user_input("Please enter your name: ")
    print(f"Your name is {name}")
    surname = validate_user_input("Please enter your surname: ")
    print(f"Your surname is {surname}")


if __name__ == '__main__':
    main()
