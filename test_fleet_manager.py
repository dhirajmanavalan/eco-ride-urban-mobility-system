from FleetManager import FleetManager
from Vehicle import Vehicle
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

fleet = FleetManager()

while True:
    print("\n--- MAIN MENU ---")
    print("1. Add Hubs and Vehicles")
    print("2. Search Vehicles")
    print("3. View Vehicles by Type")
    print("4. Fleet Analytics")
    print("5. Sort Vehicles by Model")
    print("6. Exit")

    main_choice = int(input("Enter your choice: "))
    
    if main_choice == 1:   

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
            maintenance_status = input("Enter Maintenance Status: (available / on trip / under maintenance): ").lower()
            
            while maintenance_status not in ["available", "on trip", "under maintenance"]:
                print("Invalid status. Please enter a valid status.")
                maintenance_status = input("Enter Maintenance Status: ").lower()
            
            price = float(input("Enter Rental Price: "))
            hub_name = input("Enter Hub Name to assign vehicle: ")

            if choice == 1:
                seating_capacity = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(
                    vehicle_id,
                    model,
                    battery,
                    maintenance_status,
                    price,
                    seating_capacity
                )

            elif choice == 2:
                max_speed = int(input("Enter Max Speed Limit: "))
                vehicle = ElectricScooter(
                    vehicle_id,
                    model,
                    battery,
                    maintenance_status,
                    price,
                    max_speed
                )

            else:
                print("Invalid vehicle type")
                continue

            fleet.add_vehicle_hub(hub_name, vehicle)

        print("Hub Details")
        fleet.show_hub()

    elif main_choice == 2:
            if not fleet.hubs:
                print("No hubs available. Please add vehicles first.")
                continue
            
            while True:
                print("\n--- SEARCH MENU (UC8) ---")
                print("1. Search vehicles by Hub")
                print("2. Search vehicles with Battery > 80%")
                print("3. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    hub_name = input("Enter hub name to search: ")
                    fleet.search_by_hub(hub_name)

                elif choice == 2:
                    fleet.search_by_battery()

                elif choice == 3:
                    print("Exiting search")
                    break

                else:
                    print("Invalid choice")
    
    elif main_choice == 3:
        fleet.show_vehicles_by_type()
        
    elif main_choice == 4:
        fleet.fleet_analytics()
    
    elif main_choice == 5:
        hub_name = input("Enter hub name to sort vehicles: ")
        fleet.sort_vehicles_by_model(hub_name)

                    
    elif main_choice == 6:
        print("Exiting program")
        break
    
    else:
        print("Invalid option")

