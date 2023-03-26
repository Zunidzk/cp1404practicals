# this is main function
def main():
    score = float(input("Enter score: "))
    while 0 > score or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = score_print(score)
    print(result)
    print("This part is random")
    r_score = random_score()
    result = score_print(r_score)
    print(result)


def score_print(outcome):
    # this function is to decide whether result is good or bad
    if outcome >= 90:
        result = "Excellent"
    elif outcome >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


def random_score():
    # this is extra function that generate random number and star
    import random
    r_score = random.randrange(0, 100)
    return r_score


main()
