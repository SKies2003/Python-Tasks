from car_factory import Vehicle, Car, ElectricCar

def test_drive_vehicle(vehicle):
    vehicle.drive()
    print(vehicle.get_status())

if __name__ == "__main__":    
    # Build our vehicle fleet
    car1 = Car("Toyota Fortuner", "Black")
    car2 = Car("RR Phantom", "Red")
    ecar1 = ElectricCar("Tesla Model S", "White")
    print(f"\nTotal vehicles produced: {Vehicle.get_total_vehicles_produced()}")
    # v = Vehicle("Generic Model", "Gray") # TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'drive', 'get_status'
    # vehicle_fleet = [car1, car2, ecar1]

    # for vehicle in vehicle_fleet:
    #     print(f"\n--- Testing a {vehicle.model} ---")
    #     test_drive_vehicle(vehicle)
    
    print(f"100 miles is equal to {Vehicle.miles_to_km(100)} kilometers.")