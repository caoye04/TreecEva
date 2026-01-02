temperature_readings = [18, 21, 25, 29, 33, 36, 40, 42]

# Define acceptable operating ranges as a set of temperatures
valid_ranges = set(range(20, 38))

# Identify critical zones from high-risk sensors (above 35 or below 22)
critical_zones = set(temp for temp in temperature_readings if temp < 22 or temp > 35)

# Filter stable readings within optimal range
stable_readings = [t for t in temperature_readings if 25 <= t <= 32]

# Compute overlap between valid ranges and critical zones
dynamic_threshold = sum(stable_readings) / len(stable_readings)
result = len(valid_ranges & critical_zones)

print(f"Result: {result}")