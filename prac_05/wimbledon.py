def main():
    """take data from file to calculate winners and their total of trophies as well as their countries and print it"""
    lines = read_file()
    winners = number_winners(lines)
    countries = number_countries(lines)
    print(lines)
    print(winners)
    print("Wimbledon Champions:")
    for name, count in winners.items():
        print(f"{name:<20} {count:}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_file():
    """take data from file"""
    with open('wimbledon.csv', 'r') as infile:
        lines = infile.readlines()
        lines = [line.strip('\n') for line in lines]
        lines = [line.split(',') for line in lines]
        return lines


def number_winners(lines):
    """covert data from lines to calculate winners by using dictionary"""
    winners = {}
    for line in lines[1:]:
        if line[2] in winners:
            winners[line[2]] += 1
        else:
            winners[line[2]] = 1
    return winners


def number_countries(lines):
    """take data from list of lines and put name of country into set to print winner countries"""
    countries = set()
    for line in lines[1:]:
        countries.add(line[1])

    return sorted(list(countries))


main()
