# this is main function asking for user choice
def main():
    user = input("Enter name: ")
    menu = """(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            # this is function asking for user score
            score = float(input("Enter score: "))
            while 0 > score or score > 100:
                print("Invalid score")
                score = float(input("Enter score: "))
        elif choice == "P":
            score = score
            # this is function import from score.py
            from score import score_print
            result = score_print(score)
            print(result, user, end='\n')
        elif choice == "S":
            # this is the part where it produces as many stars as score
            score = int(score)
            print('*' * score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    # this is farewell message
    print("Thank you {}. Come Again.".format(user))


main()
