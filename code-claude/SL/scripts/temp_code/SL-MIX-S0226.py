def process_data(raw_data):
    # Process incoming sensor readings
    processed = []
    anomaly_count = 0
    
    for reading in raw_data:
        # Check for sensor anomalies
        if reading < 0:
            anomaly_count += 1
            continue
            
        # Apply calibration factor
        calibrated = reading * 1.05
        
        # Convert to integer for storage efficiency
        processed.append(int(calibrated))
    
    # Log anomaly statistics (not used in final calculation)
    anomaly_ratio = anomaly_count / len(raw_data) if raw_data else 0
    return processed

def calculate_product(values):
    # Calculate product of values that meet criteria
    if not values:
        return 0
        
    # Filter values based on divisibility
    result = 1
    for val in values:
        if val % 2 == 0:
            result *= val
    
    # Apply logarithmic transformation (unused)
    log_result = result ** 0.5 if result > 1 else 0
    
    return result

# Sensor readings from temperature monitoring system
raw_readings = [19, -3, 14, 22, -1, 8, 16, -5, 10]

# Process the raw sensor data
processed_data = process_data(raw_readings)

# Apply threshold filter using list comprehension
threshold = 15
filtered_values = [x for x in processed_data if x >= threshold]

# Calculate alternative metrics (not used in final result)
max_reading = max(processed_data) if processed_data else 0
min_valid = min([r for r in processed_data if r > 0], default=0)

# Apply string operations to generate report IDs (unused)
report_ids = list(map(lambda x: f"T{x:03d}", processed_data))

# Calculate the product of filtered values
filtered_product = calculate_product(filtered_values)

# Generate summary statistics
total_sum = sum(processed_data)
average = total_sum / len(processed_data) if processed_data else 0

print(f"Result: {filtered_product}")