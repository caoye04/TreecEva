def filter_sequence(data, threshold):
    # Filter readings above threshold
    filtered = [x for x in data if x <= threshold]
    # This is just for logging, doesn't affect result
    discarded = len(data) - len(filtered)
    return filtered, discarded

def calculate_statistics(values):
    # Basic statistics calculation
    if not values:
        return 0, 0, 0
    avg = sum(values) / len(values)
    # These calculations aren't used in the final result
    max_val = max(values)
    min_val = min(values)
    return avg, min_val, max_val

def calculate_adjusted_pressure(readings, filter_threshold):
    # Process the middle section of readings
    mid_start = len(readings) // 3
    mid_end = 2 * len(readings) // 3
    mid_section = readings[mid_start:mid_end]
    
    # Apply calibration factor to the readings
    calibration = 0.95
    calibrated = [reading * calibration for reading in mid_section]
    
    # Filter out anomalous readings
    filtered_readings, anomaly_count = filter_sequence(calibrated, filter_threshold)
    
    # Calculate baseline from first few readings (not used in final calculation)
    baseline_readings = readings[:3]
    baseline, _, _ = calculate_statistics(baseline_readings)
    
    # Calculate adjusted pressure from filtered readings
    if filtered_readings:
        mean_pressure, _, _ = calculate_statistics(filtered_readings)
        # Apply compensation factor
        compensation = 1.05
        result = mean_pressure * compensation
    else:
        # Fallback if all readings were filtered out
        result = 0
    
    return round(result, 2)

# Sensor pressure readings (kPa)
readings = [102.5, 103.1, 101.8, 104.2, 105.7, 103.4, 102.9, 101.5, 102.3]

# Threshold for filtering anomalous readings
filter_threshold = 104.0

# Process readings and calculate adjusted pressure
final_pressure = calculate_adjusted_pressure(readings, filter_threshold)
print(f"Result: {final_pressure}")