from Vehicle import Vehicle

class EcoRideMain:

    @staticmethod
    def start():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicle_id = int(input("Enter Vehicle ID: "))
        model = input("Enter Vehicle Model: ")
        battery_percentage = int(input("Enter Battery Percentage: "))
        maintenance_status = input("Enter Maintenance Status: ")
        rental_price = float(input("Enter Rental Price: "))

        vehicle = Vehicle(
            vehicle_id,
            model,
            battery_percentage,
            maintenance_status,
            rental_price
        )

        print("\nVehicle Created Successfully")
        print("ID:", vehicle.vehicle_id)
        print("Model:", vehicle.model)
        print("Battery:", vehicle.battery_percentage)
        print("Maintenance:", vehicle.maintenance_status)
        print("Price:", vehicle.rental_price)


if __name__ == "__main__":
    EcoRideMain.start()
