from collections import Counter

def calculate_noise_level(readings):
    # Calculate noise as standard deviation of differences
    if not readings:
        return 0
    differences = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    mean_diff = sum(differences) / max(1, len(differences))
    # This noise calculation isn't used in the main function
    return mean_diff

def calculate_optimal_threshold(readings):
    # Identify potential anomalies in sensor readings
    if not readings:
        return 0
    
    # Calculate basic statistics
    avg_reading = sum(readings) / len(readings)
    max_reading = max(readings)
    min_reading = min(readings)
    
    # Calculate frequency of each reading value
    reading_counts = Counter(readings)
    most_common = reading_counts.most_common(1)[0][0] if reading_counts else 0
    
    # These variables look important but don't affect the final result
    range_factor = max_reading - min_reading
    variance_estimate = sum((x - avg_reading) ** 2 for x in readings) / len(readings)
    
    # Calculate threshold based on weighted factors
    base_threshold = (avg_reading + most_common) / 2
    
    # Apply adjustments based on data distribution
    above_avg = [x for x in readings if x > avg_reading]
    below_avg = [x for x in readings if x <= avg_reading]
    
    # This adjustment factor isn't actually used
    adjustment = 1.0 if len(above_avg) > len(below_avg) else 0.8
    
    # Calculate final threshold with some operations that don't affect result
    result = base_threshold * 0.75 + avg_reading * 0.25
    potential_result = result + (max_reading - avg_reading) * 0.1
    
    # This condition always evaluates to True with our data
    if avg_reading > 0:
        return round(result, 2)
    else:
        return round(potential_result, 2)

# Sample sensor data from a temperature monitoring system
sensor_data = [22.5, 22.7, 22.4, 22.6, 22.8, 22.5, 35.2, 22.6, 22.5, 22.7]

# Calculate baseline statistics that aren't directly used
baseline_mean = sum(sensor_data[:5]) / 5
baseline_max = max(sensor_data)
baseline_min = min(sensor_data)

# Calculate noise level in the readings
noise_level = calculate_noise_level(sensor_data)

# These variables create distraction
outlier_threshold = baseline_mean * 1.5
potential_outliers = [x for x in sensor_data if x > outlier_threshold]

# Calculate the optimal threshold for anomaly detection
optimal_threshold = calculate_optimal_threshold(sensor_data)

print(f"Result: {optimal_threshold}")