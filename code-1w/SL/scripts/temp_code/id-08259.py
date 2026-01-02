from collections import defaultdict
from itertools import combinations

# Simulate sensor data drift and correction in an environmental monitoring system
def preprocess_data(raw_readings):
    processed = []
    drift_compensation = 0.0
    for val in raw_readings:
        if val > 95:
            drift_compensation += 0.5
        elif val < 10:
            drift_compensation -= 0.3
        corrected = val + drift_compensation
        processed.append(round(corrected, 2))
    return processed

# Identify anomalous patterns using sliding window analysis
def detect_anomalies(values, window_size=3, tolerance=5.0):
    anomalies = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i+window_size]
        avg = sum(window) / window_size
        if abs(window[-1] - avg) > tolerance:
            anomalies.append(i + window_size - 1)
    # Distractor: unused combination logic
    _ = list(combinations(values, 2))  # Irrelevant but plausible
    return list(set(anomalies))

# Calculate reliability weights based on anomaly frequency
def calculate_reliability_weights(indices, length):
    count_per_position = defaultdict(int)
    for idx in indices:
        bucket = (idx // 10) * 10
        count_per_position[bucket] += 1
    weights = [1.0] * length
    for i in range(length):
        bucket = (i // 10) * 10
        weights[i] = max(0.5, 1.0 - 0.1 * count_per_position[bucket])
    return weights

# Main scoring logic with conditional adjustments
def calculate_final_score(data, thresholds):
    base_score = 0
    adjustment_factor = 1.0
    high_threshold, low_threshold = thresholds
    
    # State tracking variables (some are distractions)
    spike_count = 0
    dip_count = 0
    sustained_high = 0
    temp_buffer = []  # Collected but not used later
    
    for x in data:
        if x > high_threshold:
            spike_count += 1
            sustained_high += 1
            adjustment_factor *= 0.95
        elif x < low_threshold:
            dip_count += 1
            sustained_high = max(0, sustained_high - 1)
            adjustment_factor *= 1.02
        else:
            sustained_high = max(0, sustained_high - 0.5)
        
        # Complex but semi-relevant accumulation
        temp_buffer.append(x * adjustment_factor)
        
        if sustained_high >= 3:
            base_score += 2
        else:
            base_score += 1
    
    # Final adjustment using buffer (only last element used)
    if temp_buffer:
        final_drift = round(temp_buffer[-1], 2)
        base_score += int(final_drift % 5)
    
    # Dead code path - never executed due to logic above
    extreme_case = False
    if extreme_case:
        backup = sum(temp_buffer) / len(temp_buffer)
        base_score = int(backup % 100)
    
    return int(base_score)

# Generate synthetic dataset
raw_sensor_data = [85, 96, 97, 88, 45, 12, 8, 98, 99, 100, 73, 68, 11, 94, 93]

# Execution pipeline
processed_data = preprocess_data(raw_sensor_data)
anomaly_indices = detect_anomalies(processed_data, window_size=3, tolerance=8.0)
reliability_weights = calculate_reliability_weights(anomaly_indices, len(processed_data))

thresholds_config = (92.0, 15.0)
final_score = calculate_final_score(processed_data, thresholds_config)

# Output result
print(f"Result: {final_score}")