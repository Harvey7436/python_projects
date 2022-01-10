from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_car = SilverServiceTaxi("Hummer", 100, 2)

    silver_car.drive(18)
    print(silver_car)
    print(silver_car.get_fare())


main()
