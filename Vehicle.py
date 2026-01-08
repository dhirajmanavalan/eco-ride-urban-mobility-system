from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = 0
        self.__maintenance_status = maintenance_status
        self.__rental_price = 0

        self.battery_percentage = battery_percentage
        self.rental_price = rental_price
        self.maintenance_status = maintenance_status

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            print(f"Battery percentage must be between 0 and 100. Given: {value}")
            self.__battery_percentage = 0

    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, value):
        allowed_status = ["available", "on trip", "under maintenance"]
        
        if value.lower() in allowed_status:            
            self.__maintenance_status = value.lower()
        else:
            print("Invalid status! Setting status to 'available'")
            self.__maintenance_status = "available"

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, value):
        if value > 0:
            self.__rental_price = value
        else:
            print(f"Rental price must be positive. Given: {value}")
            self.__rental_price = 0
    
    @abstractmethod        
    def calculate_trip_cost(self,distance):
        pass
    
    def __eq__(self, other):
        if isinstance(other , Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False

