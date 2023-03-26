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


def score_print(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


def random_score():
    import random
    r_score = random.randrange(0, 100)
    return r_score


main()
