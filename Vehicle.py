from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price):
        self.vehicle_id = vehicle_id
        self.model = model

        self.battery_percentage = battery_percentage
        self.maintenance_status = maintenance_status
        self.rental_price = rental_price

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            print("Invalid Battery Percentage")
            self.__battery_percentage = 0

    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, status):
        self.__maintenance_status = status

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, price):
        if price > 0:
            self.__rental_price = price
        else:
            print("Rental price must be positive")
            self.__rental_price = 0

    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass
