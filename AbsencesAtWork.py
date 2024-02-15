# Constants
DAYS_IN_YEAR = 365

# Function to calculate average absence


def calculate_average(absences):
    total_absence = sum(absences)
    return total_absence / len(absences)

# Function to find the person with the most days absent


def find_most_absent(names, absences):
    max_index = absences.index(max(absences))
    return names[max_index]

# Function to find people not absent at all


def find_not_absent(names, absences):
    not_absent = [name for name, days in zip(names, absences) if days == 0]
    return not_absent

# Function to find people absent above average


def find_above_average(names, absences, average):
    above_average = [f"{name} {days}" for name, days in zip(names, absences) if days > average]
    return above_average

# Main program


def main():
    # Lists to store names and absences
    names = []
    absences = []

    # Input loop
    while True:
        input_data = input("Please enter the employee data (or $ to finish): ").strip()

        if input_data == "$":
            break

        try:
            name, days_str = input_data.rsplit(" ", 1)
            days = int(days_str)
            names.append(name)
            absences.append(days)
        except ValueError:
            print("Invalid input. Please enter the data in the format: 'Name Days'.")

    # Calculate results
    average_absence = calculate_average(absences)
    most_absent_person = find_most_absent(names, absences)
    not_absent_list = find_not_absent(names, absences)
    above_average_list = find_above_average(names, absences, average_absence)

    # Print results
    print("\nResults:")
    print(f"Average number of days staff were absent: {average_absence:.2f}")
    print(f"Person with most days absent: {most_absent_person} with {max(absences)} days")
    print("List of people not absent at all:")
    for person in not_absent_list:
        print(person)
    print("List of people absent above average:")
    for person in above_average_list:
        print(person)

# Run the program


if __name__ == "__main__":
    main()
