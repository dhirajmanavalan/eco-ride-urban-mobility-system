from FleetManager import FleetManager
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

def test_invalid_battery_sets_zero():
    v = ElectricCar(1,'Tesla',-10,'available',300,4)
    assert v.battery_percentage == 0