from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    current_taxi = None
    bill_to_date = 0
    print("Let's drive!")
    user_input = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while user_input != "q":
        if user_input == "c":
            current_taxi = choose_taxi()
        elif user_input == "d":
            if current_taxi is not None:
                cost = drive(current_taxi)
                bill_to_date += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        bill(bill_to_date)
        user_input = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    i = 1
    print("Taxis are now: ")
    for taxi in taxis:
        print(f"{i} - {taxi}")
        i += 1


def choose_taxi():
    i = 1
    print("Taxis available: ")
    for taxi in taxis:
        print(f"{i} - {taxi}")
        i += 1

    user_input = int(input(">>> "))
    if 0 <= user_input <= len(taxis):
        selected_taxi = taxis[user_input-1]
        print(selected_taxi)
        return selected_taxi
    else:
        print("Invalid taxi choice")


def drive(selected_taxi):
    user_input = int(input("Drive how far? "))
    selected_taxi.start_fare()
    selected_taxi.drive(user_input)
    print(f"Your {selected_taxi.name} trip cost you ${selected_taxi.get_fare():.2f}")
    return selected_taxi.get_fare()


def bill(bill_to_date):
    print(f"Bill to date: ${bill_to_date:.2f}")


main()