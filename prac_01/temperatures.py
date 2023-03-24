MENU = ("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")


def main():
    print(MENU)
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
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def con_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def con_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
