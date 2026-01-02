from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly filtering
def collect_sensor_readings():
    raw_readings = [
        ('sensor_a', 23), ('sensor_b', 45), ('sensor_a', 21),
        ('sensor_c', 67), ('sensor_b', 48), ('sensor_a', 22),
        ('sensor_d', 12), ('sensor_c', 65), ('sensor_b', 44)
    ]
    return raw_readings

# Process readings: group by sensor and compute average
def process_readings(raw):    
    grouped = defaultdict(list)
    for sensor, val in raw:
        grouped[sensor].append(val)
    
    averages = {}
    for sensor, values in grouped.items():
        averages[sensor] = sum(values) / len(values)
    
    # Distractor: count frequency (not used later)
    all_values = [v for vals in grouped.values() for v in vals]
    freq_counter = Counter(all_values)
    
    return averages

# Apply calibration adjustment based on sensor type
def apply_calibration(averages):
    calibration_map = {
        'sensor_a': 1.05,
        'sensor_b': 0.98,
        'sensor_c': 1.02,
        'sensor_d': 1.10
    }
    
    adjusted = {}
    temp_store = []  # Irrelevant accumulation
    for sensor, avg in averages.items():
        if sensor in calibration_map:
            corrected = avg * calibration_map[sensor]
            adjusted[sensor] = round(corrected, 2)
            temp_store.append(corrected)  # Dead-end tracking
    
    # Extra logic: find max (not used)
    if adjusted:
        max_val = max(adjusted.values())
        for s, v in adjusted.items():
            if v == max_val:
                peak_sensor = s  # Unused variable
    
    return adjusted

# Filter out sensors below threshold and compute final score
def calculate_final_score(calibrated):
    valid_sensors = []
    total_contribution = 0.0
    
    # Only include sensors with reading >= 25.0
    for sensor, value in calibrated.items():
        if value >= 25.0:
            valid_sensors.append(sensor)
            total_contribution += value

    # Compute penalty for excluded sensors (distractor calculation)
    all_count = len(calibrated)
    valid_count = len(valid_sensors)
    exclusion_penalty = (all_count - valid_count) * 2.5  # Not applied but computed

    # Final score is total contribution minus fixed offset
    base_offset = 15.0
    final_score = total_contribution - base_offset
    
    # Additional red herring: normalize by number of valid sensors if any
    if valid_sensors:
        dummy_normalized = final_score / len(valid_sensors)  # Not used
    
    return final_score

# Execution flow
raw_data = collect_sensor_readings()
processed_data = process_readings(raw_data)
calibrated_data = apply_calibration(processed_data)
final_score = calculate_final_score(calibrated_data)
print(f"Result: {final_score}")