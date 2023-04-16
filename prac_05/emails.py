def main():
    email_data = {}
    user_email = input("Email: ")
    while user_email != " ":
        name = extract_name(user_email)
        correct_name = (input(f"Is your name {name}? (Y/n) :")).upper()
        if correct_name == " " or correct_name == "Y":
            email_data[user_email] = name
        else:
            name = input("Name: ")
            email_data[user_email] = name.title()
        for user_email, name in email_data.items():
            print(f'{name} ({user_email})')
        user_email = input("Email: ")


def extract_name(user_email):
    """Extracts name from email"""
    name_email = user_email.split('@')[0]
    name = name_email.split('.')
    name = [n.title() for n in name]
    return ' '.join(name)


main()
