import csv
import json

INPUT_CSV = "fleet_data.csv"
OUTPUT_JSON = "battery_filtered_data.json"

battery_0_60 = []
battery_60_70 = []
battery_70_100 = []

with open(INPUT_CSV, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        battery = int(row["battery"])

        vehicle_data = {
            "vehicle_id": row["vehicle_id"],
            "model": row["model"],
            "battery": battery,
            "status": row["status"],
            "hub": row["hub"],
            "vehicle_type": row["vehicle_type"]
        }

        if 0 <= battery < 60:
            battery_0_60.append(vehicle_data)
            
        elif 60 <= battery < 70:
            battery_60_70.append(vehicle_data)
            
        elif 70 <= battery <= 100:
            battery_70_100.append(vehicle_data)


final_data = {
    "battery_0_60": battery_0_60,
    "battery_60_70": battery_60_70,
    "battery_70_100": battery_70_100
}

with open(OUTPUT_JSON, "w") as json_file:
    json.dump(final_data, json_file, indent=4)

