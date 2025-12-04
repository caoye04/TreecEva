import itertools

def process_sensor_data(readings):
    # Process sensor readings and filter out anomalies
    processed = []
    anomaly_count = 0
    
    # Track min and max for informational purposes
    min_value = float('inf')
    max_value = float('-inf')
    
    for i, reading in enumerate(readings):
        # Apply calibration adjustment
        adjusted = reading * 1.05
        
        # Track min/max of adjusted values
        min_value = min(min_value, adjusted)
        max_value = max(max_value, adjusted)
        
        # Apply noise filter - values divisible by 3 are considered noise
        if int(adjusted) % 3 == 0:
            anomaly_count += 1
            continue
            
        # Valid reading
        processed.append(adjusted)
    
    # Calculate some statistics (not all are used)
    mean_value = sum(processed) / len(processed) if processed else 0
    range_value = max_value - min_value
    
    return processed, anomaly_count, mean_value, range_value

# Sensor data from multiple sources
sensor_a = [12, 15, 9, 23, 18, 17]
sensor_b = [14, 8, 21, 6, 33, 10]

# Combine data sources with enumeration
combined_data = []
for idx, (a, b) in enumerate(zip(sensor_a, sensor_b)):
    # XOR operation to determine which reading to use
    use_a = (idx & 1) == 0  # Use sensor A for even indices
    combined_data.append(a if use_a else b)

# Process the combined readings
processed_readings, anomalies, avg, data_range = process_sensor_data(combined_data)

# Take a slice of the processed readings
sliced_readings = processed_readings[1:5]

# Apply a transformation based on position
transformed_values = []
for pos, val in enumerate(sliced_readings, 1):
    # Transformation: multiply by position if value > 15, otherwise divide
    if val > 15:
        transformed_values.append(val * pos)
    else:
        transformed_values.append(val / pos)

# Filter values based on a threshold derived from data
threshold = avg - (anomalies * 0.5)
filtered_values = [val for val in transformed_values if val > threshold]

# Calculate the sum of filtered values
filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")
