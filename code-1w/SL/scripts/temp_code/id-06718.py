from collections import defaultdict
import math

# Simulate sensor data with timestamps and readings
timestamps = [100, 101, 102, 103, 104, 105, 106, 107]
raw_readings = [23.5, 24.1, 23.9, 25.3, 26.0, 25.8, 26.2, 26.5]

# Misleading auxiliary data (distractor)
noise_floor = [0.1, 0.3, 0.2, 0.5, 0.4, 0.6, 0.7, 0.5]
baseline_offset = 22.0

# Preprocessing: filter anomalies using rolling window (relevant)
def detect_anomalies(data, window_size=3, tolerance=1.0):
    anomalies = []
    for i in range(len(data)):
        if i < window_size:
            window = data[:i+1]
        else:
            window = data[i-window_size+1:i+1]
        avg = sum(window) / len(window)
        if abs(data[i] - avg) > tolerance:
            anomalies.append(i)
    return anomalies

# Anomaly detection on raw data
anomalous_indices = detect_anomalies(raw_readings, window_size=3, tolerance=0.8)

# Process data by removing anomalies and applying calibration
processed_data = []
calibration_log = []
for idx, (ts, val) in enumerate(zip(timestamps, raw_readings)):
    if idx in anomalous_indices:
        continue
    corrected_val = val - baseline_offset  # Normalize
    processed_data.append(corrected_val)
    calibration_log.append(f"Calibrated {ts}: {corrected_val:.2f}")

# Misleading transformation chain (semi-relevant, but not used in final calc)
doubled_values = [x * 2 for x in processed_data]
squared_values = [x**2 for x in doubled_values]
sum_of_squares = sum(squared_values)

# Aggregate using frequency count of binned values (distractor)
binned = [int(x) for x in processed_data]
frequency_map = defaultdict(int)
for b in binned:
    frequency_map[b] += 1

# Core efficiency calculation function
def calculate_efficiency(values, threshold):
    if not values:
        return 0.0
    
    # Weighted accumulation based on proximity to threshold
    total_weight = 0.0
    weighted_sum = 0.0
    
    for v in values:
        distance = abs(v - threshold)
        weight = 1.0 / (1.0 + distance)  # Closer = higher weight
        weighted_sum += v * weight
        total_weight += weight
    
    if total_weight == 0:
        return 0.0
    
    return weighted_sum / total_weight

# Secondary distractor: unused helper function
def analyze_trend(seq):
    trend_score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trend_score += 1
        elif seq[i] < seq[i-1]:
            trend_score -= 1
    return trend_score

# Unused lambda (distractor)
smooth_func = lambda x: math.sin(x) + 0.5 * math.cos(x / 2)

# Key execution point
threshold = 1.5
intermediate_metric = sum(processed_data) / len(processed_data) if processed_data else 0

# Final efficiency score calculation
efficiency_score = calculate_efficiency(processed_data, threshold)

# Print result for extraction
print(f"Result: {efficiency_score}")