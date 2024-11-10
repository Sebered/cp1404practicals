from prac_07.guitar import Guitar


def main():
    guitars = []

    file = open('guitars.csv', 'r')
    file.readline()

    for line in file:
        parts = line.strip().split(',')

        guitar = Guitar(str(parts[0]), int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    file.close()

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = ""
            if guitar.is_vintage():
                vintage = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


main()
