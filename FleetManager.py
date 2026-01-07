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
            
        