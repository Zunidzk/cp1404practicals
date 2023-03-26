# this is main function asking for user which they want to convert
def main():
    menu = ("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = con_celsius()
            print(fahrenheit)
        elif choice == "F":
            celsius = con_fahrenheit()
            print(celsius)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def con_celsius():
    # this function is to convert Celsius to Fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def con_fahrenheit():
    # this function is to convert Fahrenheit to Celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
