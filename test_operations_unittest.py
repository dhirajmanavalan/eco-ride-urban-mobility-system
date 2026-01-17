import unittest

from FleetManager import FleetManager
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter


class TestFleetManagement(unittest.TestCase):
    
    def test_invalid_battery_sets_zero(self):
        v = ElectricCar(1, "Tesla", -10, "available", 300, 4)
        self.assertEqual(v.battery_percentage, 0)


    def test_trip_cost(self):
        car = ElectricCar(1, "Suzuki", 20, "available", 300, 4)
        scooter = ElectricScooter(2, "Splender", 90, "under maintenance", 100, 60)

        self.assertEqual(car.calculate_trip_cost(10), 10.0)
        self.assertEqual(scooter.calculate_trip_cost(10), 2.5)


    def test_add_hub(self):
        fleet = FleetManager()
        fleet.add_hub("salem")
        self.assertIn("salem", fleet.hubs)

    def test_add_vehicle_to_hub(self):
        fleet = FleetManager()
        fleet.add_hub("salem")

        car = ElectricCar(1, "Tesla", 80, "available", 300, 4)
        fleet.add_vehicle_hub("salem", car)

        self.assertEqual(len(fleet.hubs["salem"]), 1)

    def test_duplicate_vehicle_id_not_allowed(self):
        fleet = FleetManager()
        fleet.add_hub("salem")

        v1 = ElectricCar(1, "Tesla", 80, "available", 300, 4)
        v2 = ElectricCar(1, "BMW", 70, "available", 400, 4)

        fleet.add_vehicle_hub("salem", v1)
        fleet.add_vehicle_hub("salem", v2)

        self.assertEqual(len(fleet.hubs["salem"]), 1)


    def test_search_battery_above_80(self):
        fleet = FleetManager()
        fleet.add_hub("salem")

        v1 = ElectricCar(1, "Tesla", 90, "available", 300, 4)
        v2 = ElectricCar(2, "BMW", 60, "available", 300, 4)

        fleet.add_vehicle_hub("salem", v1)
        fleet.add_vehicle_hub("salem", v2)

        high_battery = [v for v in fleet.hubs["salem"] if v.battery_percentage > 80]
        self.assertEqual(len(high_battery), 1)


    def test_fleet_analytics_counts(self):
        fleet = FleetManager()
        fleet.add_hub("salem")

        fleet.add_vehicle_hub("salem", ElectricCar(1, "A", 80, "available", 100, 4))
        fleet.add_vehicle_hub("salem", ElectricCar(2, "B", 70, "on trip", 100, 4))
        fleet.add_vehicle_hub("salem", ElectricCar(3, "C", 60, "under maintenance", 100, 4))

        summary = {"available": 0, "on trip": 0, "under maintenance": 0}

        for v in fleet.hubs["salem"]:
            summary[v.maintenance_status] += 1

        self.assertEqual(summary["available"], 1)
        self.assertEqual(summary["on trip"], 1)
        self.assertEqual(summary["under maintenance"], 1)


    def test_sort_by_model(self):
        fleet = FleetManager()
        fleet.add_hub("salem")

        fleet.add_vehicle_hub("salem", ElectricCar(1, "Tesla", 80, "available", 300, 4))
        fleet.add_vehicle_hub("salem", ElectricCar(2, "BMW", 80, "available", 300, 4))

        fleet.sort_vehicles_by_model("salem")
        self.assertEqual(fleet.hubs["salem"][0].model, "BMW")

    def test_sort_by_battery_desc(self):
        fleet = FleetManager()
        fleet.add_hub("salem")

        fleet.add_vehicle_hub("salem", ElectricCar(1, "A", 50, "available", 300, 4))
        fleet.add_vehicle_hub("salem", ElectricCar(2, "B", 90, "available", 300, 4))

        sorted_list = sorted(
            fleet.hubs["salem"],
            key=lambda v: v.battery_percentage,
            reverse=True
        )

        self.assertEqual(sorted_list[0].battery_percentage, 90)


if __name__ == "__main__":
    unittest.main()
