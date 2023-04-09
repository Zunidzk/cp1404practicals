"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print("----------")
    for part in data:
        code = part[0]
        teacher = part[1]
        students = part[2]
        print(f"{code} is taught by {teacher:12} and has {students:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    lines = []
    input_file = open(FILENAME, 'r')
    for line in input_file:
        if line[-1] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)
        """print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip('\n')  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")"""
    input_file.close()
    parts = [line.split(',') for line in lines]
    for part in parts:
        part[2] = int(part[2])
    return parts


main()
