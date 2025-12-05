import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../exp04')))
from exp1 import main


def test_vehicle_parent_class():
    v = main.Vehicle("Ford", "Mustang")
    assert v.make == "Ford"
    assert hasattr(v, 'display_info'), "Vehicle class missing display_info method"

def test_car_child_class():
    # Test Inheritance
    c = main.Car("Toyota", "Camry", 4)
    assert isinstance(c, main.Vehicle), "Car must inherit from Vehicle"
    assert c.num_doors == 4, "Car did not store num_doors correctly"