def process_sensor_readings(readings):
    threshold = 50
    scaling_factor = 1.5
    
    # Apply scaling and filter out low readings
    scaled_readings = [x * scaling_factor for x in readings]
    filtered_data = list(filter(lambda x: x > threshold, scaled_readings))
    
    # Irrelevant tracking variable (minimal distraction)
    count_above_threshold = len(filtered_data)
    
    filtered_sum = sum(filtered_data)
    return filtered_sum

# Simulated sensor data
sensor_inputs = [20, 35, 45, 60, 80]
result = process_sensor_readings(sensor_inputs)
filtered_sum = result
print(f"Result: {filtered_sum}")