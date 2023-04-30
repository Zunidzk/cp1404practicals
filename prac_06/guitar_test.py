from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1923, 16035.40)
another_one = Guitar("Another guitar", 2014, 15000.50)

print(f"Expected {2023 - gibson.year:<5} Got {gibson.get_age()}")
print(f"Expected {2023 - another_one.year:<5} Got {another_one.get_age()}")

print("Expected True.  Got", gibson.is_vintage())
print("Expected False. Got", another_one.is_vintage())
