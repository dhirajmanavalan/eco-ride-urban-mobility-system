from Vehicle import Vehicle
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

class EcoRideMain:

    @staticmethod
    def start():
        print("Welcome to Eco-Ride Urban Mobility System")
        
        print("1. Electric Car")
        print("2. Electric Scooter")

        choice = int(input("Choose vehicle type (1 or 2) to create a vehicle: "))

        vehicle_id = int(input("Enter Vehicle ID: "))
        model = input("Enter Vehicle Model: ")
        
        while True:
                    battery_percentage = int(input("Enter Battery Percentage: "))
                    if 0 <= battery_percentage <=100: 
                        break
                    else:
                        print("Invalid battery percentage. Please enter a value between 0 and 100.")
        
        maintenance_status = input("Enter Maintenance Status: (available / on trip / under maintenance): ").lower()
        
        while maintenance_status not in ["available", "on trip", "under maintenance"]:
            print("Invalid status. Please enter a valid status.")
            maintenance_status = input("Enter Maintenance Status: ").lower()
            
        while True:
                rental_price = float(input("Enter Rental Price: "))
                if rental_price > 0:
                    break
                else:
                    print("Invalid rental price. Please enter a value greater than 0.")
        
        if choice == 1:
            seating_capacity = int(input("Enter Seating Capacity: "))
            vehicle = ElectricCar(
            vehicle_id,
            model,
            battery_percentage,
            maintenance_status,
            rental_price,
            seating_capacity
        )
            distance = int(input("Enter distance in KM: "))
            cost = vehicle.calculate_trip_cost(distance)
        
        elif choice == 2:
            max_speed_limit = int(input("Enter maximum speed limit: "))
            vehicle = ElectricScooter(
                vehicle_id,
                model,
                battery_percentage,
                maintenance_status,
                rental_price,
                max_speed_limit
            )
            
            minutes = int(input("Enter ride time in minutes: "))
            cost = vehicle.calculate_trip_cost(minutes)

        else:
            print("Invalid choice")
            return    
        
        print("\nVehicle Created Successfully")
        print("ID:", vehicle.vehicle_id)
        print("Model:", vehicle.model)
        print("Battery:", vehicle.battery_percentage)
        print("Maintenance:", vehicle.maintenance_status)
        print("Price:", vehicle.rental_price)
        print("Trip Cost:", cost)


if __name__ == "__main__":
    EcoRideMain.start()
