"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when input is not integer
2. When will a ZeroDivisionError occur? when denominator input is zero "0"
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
by asking input for denominator as an integer with a loop that ask for input unless it is valid integer
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")