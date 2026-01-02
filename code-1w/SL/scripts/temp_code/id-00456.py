def analyze_temperatures(raw_readings):
    scaled_readings = [x * 1.8 + 32 for x in raw_readings]  # Convert to Fahrenheit
    valid_range = set(range(68, 89))  # Acceptable room temperature range
    
    # Filter temperatures within acceptable comfort zone
    filtered_temps = [temp for temp in scaled_readings if int(temp) in valid_range]
    
    # Apply correction factor using lambda
    correction = lambda x: x - 1.5 if x > 80 else x + 0.5
    processed_data = [correction(temp) for temp in filtered_temps]
    
    # Slice to exclude edge measurements (first and last)
    processed_data = processed_data[1:-1]
    
    filtered_sum = sum(processed_data)
    return filtered_sum

# Simulated sensor data in Celsius
sensor_input = [20.0, 20.5, 21.0, 22.0, 23.5, 24.0, 25.0]
result = analyze_temperatures(sensor_input)
print(f"Result: {result}")