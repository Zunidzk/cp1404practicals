for i in range(0, 110, 10):
    print(i, end=' ')
print()

n = 20
while n > 0:
    print(n, end=' ')
    n = n - 1

s = 0
while s != 6:
    s = int(input("Guess the numbers of stars:"))

    if s != 6:
        print("Guess Again")

print("******")

x = int(input("Enter a number for rows: "))
for y in range(0, x + 1):
        print("*" * y)

print(" ")
