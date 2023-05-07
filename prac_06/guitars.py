from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")

guitar_length = len(guitars[0].name)
for guitar in guitars:
    if len(guitar.name) > guitar_length:
        length = len(guitar.name)

# List all the guitars that is inputted
print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {i}: {guitar.name:>{guitar_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
