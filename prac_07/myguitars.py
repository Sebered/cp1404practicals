from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = []

    file = open(FILENAME, "r")
    file.readline()

    for line in file:
        parts = line.strip().split(",")

        guitar = Guitar(str(parts[0]), int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    file.close()


    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar_to_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        guitar_name = input("Name: ")


    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = ""
            if guitar.is_vintage():
                vintage = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


    with open(FILENAME, "w") as file:
        for guitar in guitars:
            line = f"{guitar.name},{guitar.year},{guitar.cost}"
            file.write(line + "\n")


main()
