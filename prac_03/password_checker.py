"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("Password >> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Password >> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    password_len = len(password)
    if password_len < MIN_LENGTH or password_len > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isnumeric():
            count_digit = count_digit + 1
            continue
        if char.isupper():
            count_upper = count_upper + 1
            continue
        if char.islower():
            count_lower = count_lower + 1
            continue
        else:
            count_special = count_special + 1
    print(count_upper, count_lower, count_digit, count_special)
    if count_upper and count_lower == 0:
        return False

    return True


main()
