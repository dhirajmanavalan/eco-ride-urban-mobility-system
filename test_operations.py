import pytest
import os

from FleetManager import FleetManager
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter



def test_invalid_battery_sets_zero():
    v = ElectricCar(1,'Tesla',-10,'available',300,4)
    assert v.battery_percentage == 0

def test_trip_cost():
    car = ElectricCar(1,'Suzuki',20,'Available',300,4)
    scooter = ElectricScooter(2,"splender",90,'Under maintenance',100,60)
    
    assert car.calculate_trip_cost(10) == 10.0
    assert scooter.calculate_trip_cost(10) == 2.5
    
@pytest.mark.fleet
def test_add_hub():
    fleet = FleetManager()
    fleet.add_hub("salem")

    assert "salem" in fleet.hubs
    
@pytest.mark.fleet
def test_add_vehicle_to_hub():
    fleet = FleetManager()
    fleet.add_hub("salem")

    car = ElectricCar(1, "Tesla", 80, "available", 300, 4)
    fleet.add_vehicle_hub("salem", car)

    assert len(fleet.hubs["salem"]) == 1

@pytest.mark.fleet
def test_duplicate_vehicle_id_not_allowed():
    fleet = FleetManager()
    fleet.add_hub("salem")

    v1 = ElectricCar(1, "Tesla", 80, "available", 300, 4)
    v2 = ElectricCar(1, "BMW", 70, "available", 400, 4)

    fleet.add_vehicle_hub("salem", v1)
    fleet.add_vehicle_hub("salem", v2)

    assert len(fleet.hubs["salem"]) == 1
    
@pytest.mark.search
def test_search_battery_above_80():
    fleet = FleetManager()
    fleet.add_hub("salem")

    v1 = ElectricCar(1, "Tesla", 90, "available", 300, 4)
    v2 = ElectricCar(2, "BMW", 60, "available", 300, 4)

    fleet.add_vehicle_hub("salem", v1)
    fleet.add_vehicle_hub("salem", v2)

    high_battery = [v for v in fleet.hubs["salem"] if v.battery_percentage > 80]
    assert len(high_battery) == 1

@pytest.mark.analytics
def test_fleet_analytics_counts():
    fleet = FleetManager()
    fleet.add_hub("salem")

    fleet.add_vehicle_hub("salem", ElectricCar(1, "A", 80, "available", 100, 4))
    fleet.add_vehicle_hub("salem", ElectricCar(2, "B", 70, "on trip", 100, 4))
    fleet.add_vehicle_hub("salem", ElectricCar(3, "C", 60, "under maintenance", 100, 4))

    summary = {"available": 0, "on trip": 0, "under maintenance": 0}

    for v in fleet.hubs["salem"]:
        summary[v.maintenance_status] += 1

    assert summary["available"] == 1
    assert summary["on trip"] == 1
    assert summary["under maintenance"] == 1
    
@pytest.mark.sort
def test_sort_by_model():
    fleet = FleetManager()
    fleet.add_hub("salem")

    fleet.add_vehicle_hub("salem", ElectricCar(1, "Tesla", 80, "available", 300, 4))
    fleet.add_vehicle_hub("salem", ElectricCar(2, "BMW", 80, "available", 300, 4))

    fleet.sort_vehicles_by_model("salem")

    assert fleet.hubs["salem"][0].model == "BMW"
    
@pytest.mark.sort
def test_sort_by_battery_desc():
    fleet = FleetManager()
    fleet.add_hub("salem")

    fleet.add_vehicle_hub("salem", ElectricCar(1, "A", 50, "available", 300, 4))
    fleet.add_vehicle_hub("salem", ElectricCar(2, "B", 90, "available", 300, 4))

    sorted_list = sorted(fleet.hubs["salem"], key=lambda v: v.battery_percentage, reverse=True)

    assert sorted_list[0].battery_percentage == 90
    
# @pytest.mark.fileio
# def test_save_csv_creates_file():
#     fleet = FleetManager()
#     fleet.add_hub("salem")

#     fleet.save_to_csv("test_fleet.csv")
#     assert os.path.exists("test_fleet.csv")

#     os.remove("test_fleet.csv")
