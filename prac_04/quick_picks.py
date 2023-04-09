import random


quick_picks = int(input("Number of quick picks : "))
for i in range(quick_picks):
    lines = []
    while len(lines) < 6:
        numbers = random.randint(1, 45)
        if numbers not in lines:
            lines.append(numbers)
    lines.sort()
    print("{:3} {:3} {:3} {:3} {:3} {:3}".format(*lines))
