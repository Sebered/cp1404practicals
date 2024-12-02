CSV_FILE = "wimbledon.csv"
COUNTRY = 1
CHAMPION = 2


def main():
    records = get_records(CSV_FILE)
    champion_count, countries = process_records(records)
    display_results(champion_count, countries)


def get_records(filename):
    records = []
    with open(filename, "r",  encoding="utf-8-sig") as file:
        file.readline()
        for line in file:
            section = line.strip().split(",")
            records.append(section)
    return records


def process_records(records):
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY])
        try:
            champion_count[record[CHAMPION]] += 1
        except KeyError:
            champion_count[record[CHAMPION]] = 1
    return champion_count, countries


def display_results(champion_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_count.items():
        print(name, count)
    print("")
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()