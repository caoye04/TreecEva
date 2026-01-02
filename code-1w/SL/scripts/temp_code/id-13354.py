from itertools import combinations

# Simulate sensor data processing with noise filtering and scoring
def process_sensor_readings(raw_data, threshold):
    filtered = [x for x in raw_data if x > threshold]
    noise_floor = sum(1 for x in raw_data if x < 50)  # distractor: not used later
    return filtered if filtered else [0]

# Identify anomalous patterns using pairwise differences
def has_anomaly(sequence):
    if len(sequence) < 2:
        return False
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    spike_count = sum(1 for d in diffs if d > 75)  # distractor metric
    return any(d > 100 for d in diffs)

# Main scoring logic combining multiple criteria
def calculate_final_score(entries, limits):
    base_score = 0
    penalty_adjustment = 0
    temp_buffer = []  # irrelevant accumulator

    for entry in entries:
        sensor_id = entry['id']
        readings = entry['values']
        avg_reading = sum(readings) / len(readings)
        
        # Distractor computation: track high-frequency fluctuations
        fluctuation_index = sum(1 for r in readings if r > 90) * 0.5
        temp_buffer.append(fluctuation_index)  # stored but never used

        processed = process_sensor_readings(readings, limits['primary'])
        anomaly_flag = has_anomaly(readings)
        
        # Core scoring logic
        if avg_reading > limits['critical']:
            base_score += 15
        elif avg_reading > limits['warning']:
            base_score += 8
        else:
            base_score += 3
            
        # Apply conditional penalty
        if anomaly_flag and len(processed) < 5:
            penalty_adjustment -= 7

    # Secondary adjustment using set operations (required feature)
    unique_contributions = set(temp_buffer)
    diversity_bonus = len(unique_contributions) * 2  # minor impact

    # Conditional expression usage (required feature)
    final_score = base_score + penalty_adjustment + (diversity_bonus if diversity_bonus < 10 else 10)
    
    # Irrelevant tuple unpacking (distractor)
    backup_weights = (0.1, 0.3, 0.6)
    w1, w2, w3 = backup_weights
    
    # Final result output
    print(f"Result: {final_score}")
    return final_score

# Input data setup
data_entries = [
    {'id': 'S1', 'values': [85, 92, 45, 98, 102, 40]},
    {'id': 'S2', 'values': [60, 68, 70, 72, 65]},
    {'id': 'S3', 'values': [110, 30, 115, 25, 120, 20, 125]}
]

thresholds = {
    'primary': 40,
    'warning': 60,
    'critical': 80
}

# Execute main function
target_result = calculate_final_score(data_entries, thresholds)