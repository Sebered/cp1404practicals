from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

selected_taxi = False

def main():
    print("Let's drive!")
    user_input = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while user_input != "q":
        if user_input == "c":
            choose_taxi()
        elif user_input == "d":
            if selected_taxi:
                drive()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        bill()
        user_input = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print("Quit")

def choose_taxi():
    True


def drive():
    True


def bill():
    False


main()