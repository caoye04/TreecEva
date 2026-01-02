def calculate_efficiency(readings):
    total = sum(readings)
    count = len(readings)
    average = total / count if count else 0
    efficiency_factor = 0.87
    return average * efficiency_factor

# Sensor data collection
raw_data = [105, 234, 189, 92, 201, 158, 177]

# Filter out readings below threshold using lambda
valid_range = lambda x: 90 <= x <= 250
filtered_readings = list(filter(valid_range, raw_data))

# Irrelevant distraction: string processing (minimal interference)
device_id = "SENSOR-TRX2"
normalized_id = device_id.lower().replace("-", "_")

# Core computation
energy_output = calculate_efficiency(filtered_readings)

# Output result
print(f"Result: {energy_output}")