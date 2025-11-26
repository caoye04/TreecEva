tank_capacity = 150
units_per_vehicle = 12
vehicle_count = 8
fuel_efficiency = 15

# Calculate final capacity using conditional expression
final_capacity = tank_capacity // units_per_vehicle if units_per_vehicle > 0 else 0

# Additional calculations for fleet management
remaining_fuel = tank_capacity - (vehicle_count * fuel_efficiency)
total_distance = vehicle_count * fuel_efficiency * 2

print(f"Result: {final_capacity}")