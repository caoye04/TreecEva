from collections import Counter

def process_sensor_readings(data):
    # Calculate statistics on sensor readings
    avg_reading = sum(data) / len(data)
    max_reading = max(data)
    min_reading = min(data)
    
    # Filter values within threshold range
    threshold_high = avg_reading * 1.2
    threshold_low = avg_reading * 0.8
    
    # Track occurrences for frequency analysis
    reading_counts = Counter(data)
    most_common = reading_counts.most_common(1)[0][0]
    
    # Apply primary filter - values within thresholds
    filtered_data = [x for x in data if threshold_low <= x <= threshold_high]
    
    # Apply secondary filter - remove values divisible by most_common if most_common > 1
    if most_common > 1:
        secondary_filtered = [x for x in filtered_data if x % most_common != 0]
        potential_outliers = len(filtered_data) - len(secondary_filtered)
    else:
        secondary_filtered = filtered_data
        potential_outliers = 0
    
    # Calculate unique elements in filtered data
    unique_elements = len(set(filtered_data))
    
    # Calculate alternative metrics (not used in final result)
    data_range = max_reading - min_reading
    normalized_values = [x/max_reading for x in filtered_data]
    
    print(f"Result: {unique_elements}")
    return unique_elements

# Sensor data from monitoring system
sensor_readings = [12, 15, 12, 18, 20, 15, 22, 18, 12, 24, 30, 35, 12, 15]
process_sensor_readings(sensor_readings)