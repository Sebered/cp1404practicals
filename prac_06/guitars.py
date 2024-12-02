from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar_to_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        guitar_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = ""
            if guitar.is_vintage():
                vintage = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


main()