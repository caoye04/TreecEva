from collections import deque

class VehicleNode:
    def __init__(self, fuel_efficiency, next_vehicle=None):
        self.fuel_efficiency = fuel_efficiency
        self.next_vehicle = next_vehicle

def process_vehicles_at_intersection(incoming_stack, passed_queue):
    total_efficiency = 0.0
    while incoming_stack:
        vehicle = incoming_stack.pop()
        if vehicle.fuel_efficiency > 25.0:
            passed_queue.append(vehicle)
            total_efficiency += vehicle.fuel_efficiency * 1.1
        else:
            total_efficiency += vehicle.fuel_efficiency * 0.95
    return total_efficiency

# Initialize vehicle linked list
vehicle_a = VehicleNode(30.5)
vehicle_b = VehicleNode(22.0)
vehicle_c = VehicleNode(35.8)
vehicle_d = VehicleNode(18.2)
vehicle_e = VehicleNode(28.7)

vehicle_d.next_vehicle = vehicle_c
vehicle_c.next_vehicle = vehicle_b
vehicle_b.next_vehicle = vehicle_e
vehicle_e.next_vehicle = vehicle_a

# Build stack from linked list (head is vehicle_d)
current = vehicle_d
incoming_vehicles = []
while current:
    incoming_vehicles.append(current)
    current = current.next_vehicle

# Process vehicles
passed_vehicles_queue = deque()
total_fuel_efficiency_after_processing = process_vehicles_at_intersection(incoming_vehicles, passed_vehicles_queue)

# Apply bonus efficiency for vehicles that passed
bonus_count = len(passed_vehicles_queue)
total_fuel_efficiency_after_processing += bonus_count * 2.5

print(f"Result: {total_fuel_efficiency_after_processing}")