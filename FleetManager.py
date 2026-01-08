from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from Vehicle import Vehicle
from EcoRideMain import EcoRideMain

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
                    
            
        