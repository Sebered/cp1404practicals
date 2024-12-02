from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)


def main():
    print(guitar)
    guitar.get_age()
    if guitar.is_vintage():
        vintage = "vintage"
    else:
        vintage = "not vintage"
    print(f"in 2024 the {guitar.name} is: {2024 - guitar.year} and is {vintage}")

main()