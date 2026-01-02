def analyze_temperatures(raw_readings):
    scaled_readings = [int(temp * 1.8 + 32) for temp in raw_readings]  # Convert to Fahrenheit
    offset = 10
    adjusted_readings = [temp + offset for temp in scaled_readings]
    processed_data = adjusted_readings[1:7:2]  # Slice: every second element from index 1 to 6
    filtered_sum = sum([x for x in processed_data if x % 3 == 0])
    return filtered_sum

# Simulated sensor data (Celsius)
data_stream = [20.0, 22.5, 19.8, 25.3, 27.0, 30.2, 24.1]
final_result = analyze_temperatures(data_stream)
print(f"Result: {final_result}")