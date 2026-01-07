class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = 0
        self.__maintenance_status = maintenance_status
        self.__rental_price = 0

        self.battery_percentage = battery_percentage
        self.rental_price = rental_price

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
        self.__maintenance_status = value

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
