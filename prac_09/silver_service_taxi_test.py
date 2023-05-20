from prac_09.silver_service_taxi import SilverServiceTaxi


silver_taxi = SilverServiceTaxi(fanciness=2, name="Hummer", fuel=200)
silver_taxi.drive(115)
print(f"Taxi detail: {silver_taxi}, Current fare: ${silver_taxi.get_fare()}")
