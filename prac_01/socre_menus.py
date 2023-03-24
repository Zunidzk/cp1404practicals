MENU = """(H)elloo
(G)oodbye
(Q)uit"""
user = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello ", end='')
        print(user)

    elif choice == "G":
        print("Goodbye ", end='')
        print(user)

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
