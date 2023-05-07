import csv
from prac_06.guitar import Guitar


def main():
    guitars = load_guitars()
    print(guitars)
    print("Complete first part of Guitars exercise")
    choice = input("Do you want to add a new guitar? (y/n): ").lower()
    while choice != "n":
        if choice == "y":
            name = input("Name: ")
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:.2f} added.")
        else:
            print("Invalid Choice")
        choice = input("Do you want to add a new guitar? (y/n): ").lower()
    print("Thanks")
    save_guitars(guitars)


def load_guitars():
    guitars = []
    with open("guitar.csv", "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name = row[0]
            year = row[1]
            cost = row[2]
            guitars.append(Guitar(name, int(year), float(cost)))
    return sorted(guitars)


def save_guitars(guitars):
    with open('guitar.csv', "w", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
