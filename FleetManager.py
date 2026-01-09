from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from Vehicle import Vehicle
from EcoRideMain import EcoRideMain

import csv
import os

class FleetManager:
    def __init__(self):
        self.hubs = {}
    
    def add_hub(self,hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name]= []
            print(f" Hub '{hub_name}' added successfully")
        else:
            print(f"Hub '{hub_name}' already Exists")
    
    def add_vehicle_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        
        existing_id = [v.vehicle_id for v in self.hubs[hub_name]]
        
        if vehicle.vehicle_id in existing_id:
            print(f"Duplicate Vehicle ID {vehicle.vehicle_id} not allowed in hub '{hub_name}'")
            return
        
        self.hubs[hub_name].append(vehicle)
        print(f"Vehicle added to '{hub_name}'")

            
        
    def show_hub(self):
        for hub,vehicles in self.hubs.items():
            print(f"Hub : {hub}")
            for v in vehicles:
                print(v.model)
                
    def search_by_hub(self, hub_name):
        if hub_name in self.hubs:
            print(f"Vehicles in hub '{hub_name}':")
            for v in self.hubs[hub_name]:
                print(f"{v.vehicle_id} - {v.model} ({v.battery_percentage}%)")
        else:
            print("Hub not found")
            
    def search_by_battery(self):
        print("Vehicles with battery > 80%:")
        
        all_vehicles = []
        
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)
            
        high_battery_vehicles = filter(lambda v : v.battery_percentage > 80, all_vehicles)
        
        found = False
        
        for v in high_battery_vehicles:
            print(f"{v.vehicle_id} - {v.model} ({v.battery_percentage}%)")
        found = True

        if not found:
            print("No vehicles found with battery > 80%")
        
    def show_vehicles_by_type(self):
        categorized = {
            "cars" : [],
            "bikes" : []
        }
        
        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    categorized["cars"].append(v)
                elif isinstance(v, ElectricScooter):
                    categorized["bikes"].append(v)
        
        
        print("\n--- Vehicles Grouped by Type ---")

        print("\nCars:")
        if categorized["cars"]:
            for v in categorized["cars"]:
                print(f"{v.vehicle_id} - {v.model}")
                
        else:
            print("No cars available")
            

        print("\nScooters:")
        if categorized["bikes"]:
            for v in categorized["bikes"]:
                print(f"{v.vehicle_id} - {v.model}")
        else:
            print("No scooters available")

    def fleet_analytics(self):
        summary = {
            "available" : 0,
            "on trip" : 0,
            "under maintenance" : 0
        }
        
        for vehicles in self.hubs.values():
            for v in vehicles:
                status = v.maintenance_status.lower()
                
                if status == "available":
                    summary["available"] += 1
                elif status == "on trip":
                    summary["on trip"] += 1
                elif status == "under maintenance":
                    summary["under maintenance"] += 1
                    
        print("\n--- Fleet Status Summary ---")
        print(f"Available           : {summary['available']}")
        print(f"On Trip             : {summary['on trip']}")
        print(f"Under Maintenance   : {summary['under maintenance']}")
                    
            
    def sort_vehicles_by_model(self, hub_name):
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        self.hubs[hub_name].sort(key = lambda v : v.model)
        
        print(f"\n--- Vehicles in '{hub_name}' sorted by Model ---")
        for v in self.hubs[hub_name]:
            print(v)
            
    def sort_by_vehicle_battery(self, hub_name):
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        sorted_vehicle = sorted(self.hubs[hub_name], key=lambda v : v.battery_percentage, reverse=True)
        
        print(f"Vehicles in '{hub_name}' sorted by Battery (High → Low)")
        
        for v in sorted_vehicle:
            print(v)
            
    def sort_by_fare(self,hub_name):
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        fare = sorted(self.hubs[hub_name],key=lambda v : v.rental_price, reverse=True)
        
        print(f" Vehicles in '{hub_name}' sorted by Fare (High → Low)")
        
        for v in fare:
            print(v)
        
    
    def save_to_csv(self, filename = "fleet_data.csv"):
        with open("fleet_data.csv","w", newline="") as file:
            writer = csv.writer(file)
            
            writer.writerow(["vehicle_id", "model", "battery", "status", "rental_price", "vehicle_type", "seating_capacity/max_speed", "hub"])
            
            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    if isinstance(v, ElectricCar):
                        writer.writerow([v.vehicle_id , v.model , v.battery_percentage , v.maintenance_status , v.rental_price , "CAR" , v.seating_capacity , hub])
                        
                    elif isinstance(v, ElectricScooter):
                        writer.writerow([v.vehicle_id , v.model , v.battery_percentage , v.maintenance_status , v.rental_price , "SCOOTER" , v.max_speed_limit , hub ])
                        
        
        print("Fleet data save to CSV file successfully")
        
    
    def load_from_csv(self, filename = "fleet_data.csv"):
        if not os.path.exists(filename):
            return
        
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                hub = row["hub"]
                
                if hub not in self.hubs:
                    self.hubs[hub] = []
                    
                vehicle_id = int(row["vehicle_id"])
                model = row["model"]
                battery = int(row["battery"])
                status = row["status"]
                price = float(row["rental_price"])

                if row["vehicle_type"].upper()=="CAR":
                    seating = int(row["seating_capacity/max_speed"])
                    
                    vehicle = ElectricCar(vehicle_id , model , battery, status, price, seating)
                
                else:
                    speed = int(row["seating_capacity/max_speed"])
                    vehicle = ElectricScooter(vehicle_id, model, battery, status, price, speed)
                    
                self.hubs[hub].append(vehicle)

        print("Fleet data loaded from CSV successfully")
            
    