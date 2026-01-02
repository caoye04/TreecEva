def process_sensor_readings(readings):
    threshold = 50
    valid_range = lambda x: 10 <= x <= 100
    
    # Normalize readings above threshold
    normalized = [r * 0.9 for r in readings if r > threshold]
    
    # Apply filtering based on valid range
    filtered_data = list(filter(valid_range, normalized))
    
    # Compute final sum
    filtered_sum = sum(filtered_data)
    return filtered_sum

# Simulated sensor data
sensor_input = [45, 60, 80, 105, 75, 5, 90]
result = process_sensor_readings(sensor_input)
print(f"Result: {result}")