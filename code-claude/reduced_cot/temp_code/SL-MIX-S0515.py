from collections import Counter

def analyze_sensor_data(readings):
    # Process raw sensor readings
    processed = []
    for i, reading in enumerate(readings):
        # Apply calibration factor
        calibrated = reading * 0.95 if i % 2 == 0 else reading * 1.05
        processed.append(round(calibrated, 1))
    
    # Count frequency of each reading
    reading_freq = Counter(processed)
    # This calculation doesn't affect our target result
    avg_freq = sum(reading_freq.values()) / len(reading_freq) if reading_freq else 0
    
    # Find valid readings based on frequency and value
    # Readings that appear exactly once and are divisible by 3 are considered valid
    valid_readings = [val for val, freq in reading_freq.items() 
                     if freq == 1 and val % 3 == 0]
    
    # Calculate noise threshold (not used in final calculation)
    noise_threshold = sum(processed) / len(processed) if processed else 0
    
    # Apply secondary filtering based on position
    secondary_filter = lambda x, pos: x > 10 or pos % 3 == 0
    
    # Combine filters
    filter_result = [val for i, val in enumerate(valid_readings) 
                    if secondary_filter(val, i)]
    
    # Calculate the sum of filtered readings
    filtered_sum = sum(filter_result)
    
    # These lines don't affect our answer
    normalized_readings = [r / max(processed) if processed else 0 for r in processed]
    quality_score = len(filter_result) / len(readings) if readings else 0
    
    return filtered_sum

# Sample sensor data
sensor_readings = [15, 19, 22, 9, 12, 18, 24, 30, 33]

# Process the readings
result = analyze_sensor_data(sensor_readings)
print(f"Result: {result}")