from itertools import compress

# Sensor readings from thermal array (in arbitrary units)
raw_readings = [105, 98, 112, 95, 108, 115, 99, 103, 107, 110]

# Threshold filter: only accept readings within normal operating range
is_valid = lambda x: 97 <= x <= 110

# Apply filter to get valid readings
valid_mask = list(map(is_valid, raw_readings))
filtered_readings = list(compress(raw_readings, valid_mask))

# Efficiency calculation as average of valid sensor readings
calculate_efficiency = lambda data: sum(data) / len(data) if data else 0

# Compute final energy output based on efficiency
energy_output = calculate_efficiency(filtered_readings)

print(f"Result: {energy_output}")