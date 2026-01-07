from FleetManager import FleetManager
from Vehicle import Vehicle
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

fleet = FleetManager()

hub_count = int(input("How many hubs do you want to add? "))

for _ in range(hub_count):
    hub_name = input("Enter hub name: ")
    fleet.add_hub(hub_name)
    
vehicle_count = int(input("\nHow many vehicles do you want to add? "))

for _ in range(vehicle_count):
    print("\n1. Electric Car")
    print("2. Electric Scooter")

    choice = int(input("Choose vehicle type (1 or 2): "))

    vehicle_id = int(input("Enter Vehicle ID: "))
    model = input("Enter Vehicle Model: ")
    battery = int(input("Enter Battery Percentage: "))
    status = input("Enter Maintenance Status: ")
    price = float(input("Enter Rental Price: "))
    hub_name = input("Enter Hub Name to assign vehicle: ")

    if choice == 1:
        seating_capacity = int(input("Enter Seating Capacity: "))
        vehicle = ElectricCar(
            vehicle_id,
            model,
            battery,
            status,
            price,
            seating_capacity
        )

    elif choice == 2:
        max_speed = int(input("Enter Max Speed Limit: "))
        vehicle = ElectricScooter(
            vehicle_id,
            model,
            battery,
            status,
            price,
            max_speed
        )

    else:
        print("Invalid vehicle type")
        continue

    fleet.add_vehicle_hub(hub_name, vehicle)

print("Hub Details")
fleet.show_hub()
