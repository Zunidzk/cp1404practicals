from prac_09.taxi import Taxi

my_taxi = Taxi("Prius", 100)
my_taxi.drive(40)
print(f"Taxi detail: {my_taxi}, Current fare: ${my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Taxi detail: {my_taxi}, Current fare: ${my_taxi.get_fare()}")
