def preprocess_readings(raw_readings):
    processed = {}
    for sensor, values in raw_readings.items():
        baseline = sum(values[:3]) / 3
        processed[sensor] = [x - baseline for x in values]
    return processed

raw_sensor_data = {
    'temp': [20.1, 20.3, 19.9, 25.4, 26.1, 27.3],
    'pressure': [101.2, 100.8, 101.5, 98.3, 97.1, 96.4],
    'humidity': [45.2, 44.8, 46.1, 50.3, 52.7, 53.1]
}

# Irrelevant transformation - distractor
shifted_data = {k: [v[i] - v[i-1] for i in range(1, len(v))] for k, v in raw_sensor_data.items()}
smoothed_humidity = [round((raw_sensor_data['humidity'][i] + raw_sensor_data['humidity'][i+1]) / 2, 2) 
                      for i in range(len(raw_sensor_data['humidity']) - 1)]

processed_sensors = preprocess_readings(raw_sensor_data)

# Extract anomalies above threshold - relevant
anomalies = {}
for sensor, readings in processed_sensors.items():
    anomalies[sensor] = [r for r in readings[3:] if abs(r) > 5.0]

# Distractor: unused function simulating calibration
def calibrate_system(log_matrix):
    total = 0
    for row in log_matrix:
        for val in row:
            total += (val * 0.95) ** 2
    return total // 10

calibration_logs = [
    [1.2, 3.4, 2.1],
    [0.9, 5.6, 4.3],
    [2.2, 1.8, 3.7]
]
unused_calibration_score = calibrate_system(calibration_logs)  # Dead code path

# Transform metrics using cumulative deviations
transformed_metrics = []
for key in ['temp', 'pressure', 'humidity']:
    series = processed_sensors[key][3:]
    cum_dev = 0
    cum_series = []
    for val in series:
        cum_dev += val
        cum_series.append(cum_dev)
    transformed_metrics.append(cum_series)

# Decoy analysis on shifted data
shift_anomalies = {k: sum(1 for x in v if x < -1.0) for k, v in shifted_data.items()}
decoy_insight = sum(shift_anomalies.values()) * 2  # Misleading intermediate result

# Real analysis function with recursion
def analyze_pattern(metric_list):
    if not metric_list:
        return 0
    if len(metric_list) == 1:
        return sum(abs(x) for x in metric_list[0])
    
    mid = len(metric_list) // 2
    left = metric_list[:mid]
    right = metric_list[mid:]
    
    left_result = analyze_pattern(left)
    right_result = analyze_pattern(right)
    
    # Combine with set operation distraction
    flat_left = {round(x) for sublist in left for x in sublist if x > 0}
    flat_right = {round(x) for sublist in right for x in sublist if x < 0}
    overlap_count = len(flat_left.intersection(flat_right))
    
    return left_result + right_result - overlap_count

# Key statement
final_diagnostic = analyze_pattern(transformed_metrics)

# Print result as required
print(f"Result: {final_diagnostic}")