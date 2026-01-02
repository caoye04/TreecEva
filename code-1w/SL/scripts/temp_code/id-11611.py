from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
def generate_sensor_readings():
    raw_data = [
        {'time': 1, 'value': 15, 'sensor': 'A', 'status': 'ok'},
        {'time': 2, 'value': 18, 'sensor': 'B', 'status': 'ok'},
        {'time': 3, 'value': 14, 'sensor': 'A', 'status': 'noisy'},
        {'time': 4, 'value': 21, 'sensor': 'C', 'status': 'ok'},
        {'time': 5, 'value': 17, 'sensor': 'B', 'status': 'ok'},
        {'time': 6, 'value': 19, 'sensor': 'A', 'status': 'ok'},
        {'time': 7, 'value': 23, 'sensor': 'C', 'status': 'error'},
        {'time': 8, 'value': 16, 'sensor': 'B', 'status': 'ok'},
    ]
    return raw_data

# Filter and aggregate valid sensor readings
def process_sensor_data(raw_data):
    valid_readings = []
    error_count = 0
    status_log = defaultdict(int)
    total_value = 0  # distractor: used for logging only

    for entry in raw_data:
        status_log[entry['status']] += 1
        if entry['status'] == 'error':
            error_count += 1
            continue
        if entry['value'] < 10 or entry['value'] > 25:
            continue  # filter outliers
        valid_readings.append(entry)
        total_value += entry['value']  # not directly contributing to result

    # Compute per-sensor averages
    sensor_values = defaultdict(list)
    for r in valid_readings:
        sensor_values[r['sensor']].append(r['value'])
    
    sensor_avg = {}
    for sensor, values in sensor_values.items():
        sensor_avg[sensor] = sum(values) / len(values)
    
    # Distractor: unused complex structure
    summary_stats = {
        'readings_count': len(valid_readings),
        'sensors_active': list(sensor_avg.keys()),
        'overall_mean': sum(sum(v) for v in sensor_values.values()) / max(len(valid_readings), 1),
        'noise_warnings': status_log['noisy']
    }
    
    return sensor_avg, summary_stats, error_count

# Calculate final weighted score based on sensor reliability
def calculate_final_score(processed_data):
    sensor_avg = processed_data[0]
    weights = {'A': 0.5, 'B': 0.3, 'C': 0.2}
    score = 0.0
    fallback_adjustment = 1.0

    # Apply weighted average, with logic branching
    for sensor, avg in sensor_avg.items():
        if sensor in weights:
            contribution = avg * weights[sensor]
            score += contribution
        else:
            fallback_adjustment += 0.1  # dead code path (never executed)
    
    # Additional adjustment based on number of sensors
    active_sensors = len(sensor_avg)
    if active_sensors == 3:
        score *= 1.1
    elif active_sensors == 2:
        score *= 1.05
    else:
        score *= 0.95
    
    # Irrelevant string manipulation (distractor)
    code_version = "v1.2.3"
    version_digits = [int(c) for c in code_version if c.isdigit()]
    version_factor = sum(version_digits) / len(version_digits) if version_digits else 1.0
    
    # Final transformation
    final_score = int(round(score * 10))  # scale and discretize
    return final_score

# Main execution flow
data = generate_sensor_readings()
processed_data = process_sensor_data(data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")