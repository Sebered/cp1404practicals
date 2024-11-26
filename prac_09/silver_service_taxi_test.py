from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Prius", 100, 2)
taxi2 = SilverServiceTaxi("Hummer", 250, 4)

taxi.drive(18)
taxi2.drive(120)

print(taxi)
print(taxi.get_fare())

print(taxi2)
print(taxi2.get_fare())

taxi2.start_fare()

taxi2.drive(50)

print(taxi2.get_fare())