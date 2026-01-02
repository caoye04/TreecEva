def process_sensor_readings(readings):
    threshold = 25
    valid_range = lambda x: 10 <= x <= 100
    
    # Normalize readings by adjusting offset
    adjusted_readings = [r + 5 for r in readings]
    
    # Identify anomalous values outside acceptable range
    anomalies = [val for val in adjusted_readings if not valid_range(val)]
    
    # Filter only high-confidence readings above threshold
    filtered_data = [val for val in adjusted_readings if val > threshold and valid_range(val)]
    
    # Compute summary statistics
    avg_original = sum(readings) / len(readings) if readings else 0
    filtered_sum = sum(filtered_data)
    
    # Dummy variables to slightly increase cognitive load (minimal interference)
    normalized_total = sum([abs(x - avg_original) for x in readings])
    anomaly_count = len(anomalies)
    
    return filtered_sum

sensor_inputs = [15, 30, 40, 5, 70, 80]
result = process_sensor_readings(sensor_inputs)
print(f"Result: {result}")