def process_sensor_readings(readings):
    threshold = 50
    squared_values = [x**2 for x in readings]
    valid_range_mask = [True if 100 < x < 900 else False for x in squared_values]
    
    # Extract values where squared value is within expected sensor range
    filtered_data = [readings[i] for i in range(len(readings)) if valid_range_mask[i]]
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_original = sum(readings) / len(readings) if readings else 0
    
    # Key computation step
    filtered_sum = sum(map(lambda x: x**2, filtered_data))
    
    # Additional unrelated transformation (low interference)
    inverted = [-x for x in readings]
    
    return filtered_sum

# Simulated sensor data input
data_stream = [8, 12, 7, 15, 4, 11]
result = process_sensor_readings(data_stream)
print(f"Target result: {result}")