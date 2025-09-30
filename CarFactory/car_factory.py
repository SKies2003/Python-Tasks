from abc import ABC, abstractmethod

class Vehicle(ABC):
    _total_vehicles_produced = 0
    def __init__(self, model, color):
        self.model = model
        self.color = color
        Vehicle._total_vehicles_produced += 1

    @classmethod
    def get_total_vehicles_produced(cls):
        return cls._total_vehicle_produced
    
    @staticmethod
    def miles_to_km(miles):
        return miles*1.60934
    
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

class Car(Vehicle):
    """Represents a car in our factory."""
    def __init__(self, model: str, color: str):
        """Initializes a new Car object."""
        super().__init__(model, color)
        self._fuel_level = 100.0
    
    def get_fuel_level(self):
        return self._fuel_level
    
    def get_status(self):
        "Returns the details of the car."
        return f"A {self.color} {self.model} with {self._fuel_level}% fuel."
    
    def drive(self):
        """Simulates driving the car, consuming the fuel."""
        if self._fuel_level > 0:
            print("The car is driving...")
            self._fuel_level -= 10.0
        else:
            print("Out of fuel! Cannot drive.")
    
    def refuel(self, amount: float):
        """Refuels the car, ensuring it never exceeds 100"""
        new_fuel_level = self._fuel_level + amount
        if new_fuel_level > 100:
            self._fuel_level = 100.0
        else:
            self._fuel_level = new_fuel_level
        print(f"Car has been refueled to {self._fuel_level}%")

class ElectricCar(Vehicle):
    """Represents an electric car in our factory."""
    def __init__(self, model: str, color: str):
        super().__init__(model, color)
        self._battery_level = 100.0

    def get_status(self): # Overriding
        """Returns the details of the electric car."""
        return f"A {self.color} {self.model} with {self._battery_level}% battery."
    
    def drive(self):
        """Simulates driving the car, consuming the battery."""
        if self._battery_level > 0:
            print("The electric car is driving silently...")
            self._battery_level -= 10.0
        else:
            print("Out of battery! Please charge.")
    
    def charge(self, amount: float):
        """Charges the car, ensuring it never exceeds 100"""
        new_battery_level = self._battery_level + amount
        if new_battery_level > 100:
            self._battery_level = 100.0
        else:
            self._battery_level = new_battery_level
        print(f"Car has been charged to {self._battery_level}%")


if __name__ == "__main__":
    # Build our first cars
    car1 = Car("Toyota Fortuner", "Black")
    car2 = Car("RR Phantom", "Red")
    ecar1 = ElectricCar("Tesla Model S", "White")

    print("--- Initial Car Details ---")
    # # Test the action
    # print(car1.get_status())
    # print(car2.get_status())
    print(ecar1.get_status())

    print("\n--- Driving Car ---")
    # # Final Test Drive
    # car1.drive()
    ecar1.drive()
    
    print("\n--- Final Car Details ---")
    # print(car1.get_status())
    # print(car2.get_status()) # To show it's unchanged
    print(ecar1.get_status())

    # print("\n--- Driving the car continuously ---")
    # for i in range(11):
    #     car1.drive()
    
    # print("\n--- Refuel the car ---")
    # car1.refuel(120)

    print("\n--- Charge the car ---")
    ecar1.charge(120)

    # print("\n--- Driving the car and checking the fuel level ---")
    # for i in range(2):
    #     car1.drive()
    # print(car1.get_fuel_level())

    print(car2.get_status())
