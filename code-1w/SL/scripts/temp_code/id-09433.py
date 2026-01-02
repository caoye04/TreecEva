def analyze_temperatures(raw_readings):
    scaled_readings = [x * 1.8 + 32 for x in raw_readings]  # Convert to Fahrenheit
    valid_range = lambda x: 32 <= x <= 212
    filtered_readings = list(filter(valid_range, scaled_readings))
    offset = 10
    adjusted_readings = [x - offset for x in filtered_readings]
    processed_data = adjusted_readings[1:6:2]  # Slice: start=1, stop=6, step=2
    temp_log = [f'{x:.1f}F' for x in processed_data]  # Logging string (irrelevant)
    filtered_sum = sum(processed_data)
    return filtered_sum

# Simulated sensor data (Celsius)
input_temps = [0, 10, 20, 30, 40, 50, 60]
result = analyze_temperatures(input_temps)
print(f"Result: {result}")