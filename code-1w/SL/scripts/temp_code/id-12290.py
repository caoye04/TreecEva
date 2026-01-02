from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, 'TEMP', 23.5), (101, 'HUMID', 45), (102, 'TEMP', 24.1),
    (103, 'PRESS', 1013), (104, 'HUMID', 47), (105, 'TEMP', 22.9),
    (106, 'PRESS', 1015), (107, 'HUMID', 44), (108, 'TEMP', 25.3)
]

# Misleading initialization of irrelevant metrics
irrelevant_metrics = {
    'calibration_offset': 0.87,
    'sensor_drift': [0.1, -0.05, 0.2],
    'noise_floor': 1.3
}

# Process raw data into structured format
sensor_data = defaultdict(list)
for ts, s_type, value in timestamped_readings:
    sensor_data[s_type].append(value)

# Extract temperature values for trend analysis
temps = sensor_data['TEMP']

# Compute moving average (window size 2) to smooth fluctuations
moving_avg = [(temps[i] + temps[i+1]) / 2 for i in range(len(temps)-1)]

# Dummy transformation: normalize around baseline (not used later)
normalized_temps = [t - 20 for t in temps]  # baseline correction

# Compute volatility as mean absolute deviation from moving average
volatility = sum(abs(t - sum(moving_avg)/len(moving_avg)) for t in temps) / len(temps)

# Flag anomalies based on deviation threshold
anomalies = [t for t in temps if abs(t - 24.0) > 1.5]

# Distractor: analyze anomaly frequency using Counter (unused)
anomaly_counter = Counter(anomalies)

# Simulate data quality score based on completeness and stability
completeness = len(temps) / 10  # max expected 10 readings
stability = 1 / (1 + volatility)  # inverse relationship
data_quality_score = (completeness + stability) / 2

# Apply non-linear weighting to emphasize stability
distorted_weighting = sum([stability ** i for i in range(3)])  # geometric series distraction

# Final processing step: adjust scores based on pattern recognition
pattern_matches = 0
for i in range(len(temps) - 2):
    if temps[i] < temps[i+1] > temps[i+2]:  # peak detection
        pattern_matches += 1

# Secondary distraction: string-based tagging
reading_tags = ['reading_' + str(i) for i in range(len(timestamped_readings))]
split_tags = [tag.split('_') for tag in reading_tags]

# Core logic hidden among distractions
def calculate_final_score(data_dict):
    temp_values = data_dict['TEMP']
    humid_values = data_dict['HUMID']
    press_values = data_dict['PRESS']
    
    # Real computation path
    temp_trend = temp_values[-1] - temp_values[0]  # net change
    humid_mode = Counter(humid_values).most_common(1)[0][1]  # frequency of most common
    press_span = max(press_values) - min(press_values)
    
    # Actual formula contributing to answer
    score_component_1 = temp_trend * 10
    score_component_2 = humid_mode * 5
    score_component_3 = press_span * 2
    
    # Final score calculation — this is the key result
    final_raw = score_component_1 + score_component_2 + score_component_3
    
    # Additional misleading scaling
    scaled_distortion = final_raw * (1 + 0.1 * len(anomalies))  # red herring
    return int(final_raw)  # deterministic integral result

# Execute main logic
processed_data = dict(sensor_data)
final_score = calculate_final_score(processed_data)

# Print result as required
print(f"Target result: {final_score}")