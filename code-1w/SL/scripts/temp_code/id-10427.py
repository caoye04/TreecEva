from collections import defaultdict, Counter
from itertools import combinations

# Simulate sensor readings with noise and redundancy
def preprocess_sensor_data(raw_readings):
    filtered_data = []
    outlier_count = 0
    temp_accumulator = 0
    smoothing_factor = 0.85

    for reading in raw_readings:
        if reading < -100 or reading > 150:  # hardware error range
            outlier_count += 1
            continue
        adjusted = reading * smoothing_factor
        temp_accumulator += adjusted
        if adjusted > 50:
            filtered_data.append(int(adjusted))
    
    # Irrelevant aggregation
    avg_temp = temp_accumulator / len(filtered_data) if filtered_data else 0
    median_estimate = sorted(filtered_data)[len(filtered_data)//2] if filtered_data else 0

    return filtered_data

# Analyze patterns in processed sensor data
def detect_anomaly_patterns(data):
    pattern_counter = Counter()
    sequence_gaps = []
    
    for i in range(len(data) - 1):
        gap = data[i+1] - data[i]
        sequence_gaps.append(gap)
        if gap > 20:
            pattern_counter['large_jump'] += 1
        elif gap < -20:
            pattern_counter['sharp_drop'] += 1
    
    # Use of itertools to generate red herring combinations
    false_alerts = 0
    for pair in combinations(data, 2):
        if abs(pair[0] - pair[1]) == 33:
            false_alerts += 1  # irrelevant count

    # Return only meaningful stats
    return pattern_counter.get('large_jump', 0) - pattern_counter.get('sharp_drop', 0)

# Main scoring logic
def calculate_final_score(data):
    base_score = sum(data)
    penalty = 0
    
    # Multiple assignment distraction
    (multiplier, offset, _) = (1.2, -5, 'deprecated_flag')
    
    # Nested loop tracking state across iterations
    history_tracker = defaultdict(int)
    for i in range(len(data)):
        for j in range(i+1, min(i+4, len(data))):
            diff = abs(data[i] - data[j])
            if diff > 25:
                history_tracker['high_variance'] += 1
            elif diff < 5:
                history_tracker['stable_pair'] += 1

    # Real penalty calculation
    if history_tracker['high_variance'] > 3:
        penalty = 15

    # Dead code path - never executed due to logic
    if len(data) > 1000:
        fallback_score = base_score * 0.9
        return int(fallback_score)

    intermediate_result = base_score * multiplier + offset
    final_score = int(intermediate_result - penalty)
    
    # Additional irrelevant transformation
    checksum = 0
    for idx, val in enumerate(data):
        checksum ^= (val + idx) % 17
    
    return final_score

# Entry point
if __name__ == "__main__":
    raw_sensor_input = [
        120, 130, 999, -200, 115, 60, 55, 140, 138, 139,
        45, 44, 40, 132, 128, 127, 53, 54, 135, 136
    ]
    
    # Unused variable - distractor
    calibration_matrix = [[i*j for j in range(3)] for i in range(3)]
    
    processed_data = preprocess_sensor_data(raw_sensor_input)
    anomaly_metric = detect_anomaly_patterns(processed_data)
    final_score = calculate_final_score(processed_data)
    
    print(f"Result: {final_score}")