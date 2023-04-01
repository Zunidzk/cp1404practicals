import random


def main():
    """random exercise"""
    print(random.randint(5, 20))  # line 1 (20)
    print(random.randrange(3, 10, 2))  # line 2 (smallest 3, largest 9, there is no 4 output)
    print(random.uniform(2.5, 5.5))  # line 3 (smallest 2.50000000000001, largest 5.49999999999999)
    random_number()


def random_number():
    """Give random number from 1 to 100"""
    first_number = random.randint(1, 100)
    print("randint from 1 to 100:", first_number)
    second_number = random.randrange(1, 100)
    print("randrange from 1 to 100:", second_number)
    third_number = random.uniform(1, 100)
    print("uniform from 1 to 100:", third_number)


main()
