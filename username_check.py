'''function for record the username in database(variable) and check if it's real and correct according to various criterias'''


def username_enter():

    '''user enters real name'''
    print(f"Please enter your name: ")
    username: str = input()
    if username.isalpha():
        print(f"Your name is {username}")
    else:
        print("incorrect input")


def surname_check():
    '''user enters real surname'''
    print(f"Please enter your surname: ")
    surname: str = input()
    # check for string
    if surname.isalpha():
        print(f"Your name is {surname}")
    else:
        print("incorrect input")


def main():
    username_enter()
    surname_check()
    print(f"User approved|unproved") # result of program


if __name__ == '__main__':
    main()
