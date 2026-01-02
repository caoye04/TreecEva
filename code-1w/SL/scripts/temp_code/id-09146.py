def process_sensor_data():
    raw_readings = [23.5, 45.0, 12.7, 89.3, 67.1, 34.8, 91.2]
    scaling_factor = 1.8
    offset = -5.5
    
    # Apply linear transformation to calibrate sensor readings
    calibrated_readings = [(v * scaling_factor) + offset for v in raw_readings]
    
    # Round to nearest integer for discretization
    rounded_values = [round(val) for val in calibrated_readings]
    
    # Scale again with a conditional adjustment
    adjustment = 2 if sum(rounded_values) > 500 else 0
    scaled_values = [val + adjustment for val in rounded_values]
    
    # Define threshold based on median-like logic
    sorted_vals = sorted(scaled_values)
    threshold = sorted_vals[len(sorted_vals) // 2]  # Middle element as pseudo-median
    
    # Compute sum of values above threshold
    filtered_sum = sum(filter(lambda x: x > threshold, scaled_values))
    
    return filtered_sum

result = process_sensor_data()
print(f"Result: {result}")