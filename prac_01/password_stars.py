# this is main function for password to print stars
def main():
    length = get_password_length()
    while length < 12:
        print("Password too short!")
        length = get_password_length()
    print('*' * length)


def get_password_length():
    # this is getting passwords length
    password = input("Enter Your Password: ")
    length = len(password)
    return length


main()
