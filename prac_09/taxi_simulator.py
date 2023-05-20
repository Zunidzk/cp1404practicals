from prac_09.silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive!")
    print(MENU)
    current_taxi = None
    user_choice = input().lower()
    total_fare = 0.00
    while user_choice != "q":
        if user_choice == "c":
            display_taxis(taxis)
            taxi_choice = choose_taxi(taxis)
            if taxi_choice is not False:
                current_taxi = taxis[taxi_choice]

        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                drive_input = int(input("Drive how far? "))
                current_taxi.drive(drive_input)
                trip_fare = current_taxi.get_fare()
                print(f"Your Prius trip cost you ${trip_fare}")
                total_fare += trip_fare

        else:
            print("Invalid Option")

        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        user_choice = input().lower()


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    while True:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxi_choice
        else:
            print("Invalid taxi choice")


if __name__ == '__main__':
    main()
