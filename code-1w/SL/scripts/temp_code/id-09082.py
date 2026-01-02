from collections import defaultdict

# Simulate sensor data processing with noise filtering and scoring
def preprocess_data(raw_entries):
    processed = []
    noise_floor = 0.1
    for entry in raw_entries:
        sensor_id = entry['id']
        readings = entry['values']
        valid_readings = [r for r in readings if r >= noise_floor]
        avg_reading = sum(valid_readings) / len(valid_readings) if valid_readings else 0
        processed.append({'sensor': sensor_id, 'avg': avg_reading})
    return processed

# Track occurrence of sensors exceeding dynamic thresholds
def build_threshold_tracker(processed_data, base_thresholds):
    tracker = defaultdict(int)
    temp_cache = {}  # Irrelevant cache (distractor)
    for record in processed_data:
        sensor = record['sensor']
        value = record['avg']
        threshold = base_thresholds.get(sensor, 0.5)
        if value > threshold:
            tracker[sensor] += 1
        elif value < threshold * 0.1:
            temp_cache[sensor] = value  # Dead code path effect (distractor)
    return tracker

# Main scoring logic combining frequency, decay, and normalization
def calculate_final_score(data_log, thresholds):
    total_weight = 0.0
    score_components = []
    decay_factor = 0.95
    max_contributions = 10
    
    # Preprocess and track high-value sensors
    clean_data = preprocess_data(data_log)
    event_count = build_threshold_tracker(clean_data, thresholds)
    
    # Compute contribution per sensor with diminishing returns
    for sensor_id, count in event_count.items():
        capped_count = min(count, max_contributions)
        contribution = capped_count * decay_factor ** (max_contributions - capped_count)
        score_components.append(contribution)
    
    # Final aggregation with normalization
    raw_total = sum(score_components)
    normalization_factor = len(event_count) if event_count else 1
    normalized_total = raw_total / normalization_factor
    
    # Extra irrelevant calculations (distractors)
    outlier_ratio = sum(1 for d in clean_data if d['avg'] > 1.0) / len(clean_data) if clean_data else 0
    adjustment_bias = outlier_ratio * 0.05  # Not used
    
    final_score = int(round(normalized_total * 100))
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data setup
data_log = [
    {'id': 'S1', 'values': [0.0, 0.0, 0.15, 0.2, 0.25]},
    {'id': 'S2', 'values': [0.8, 0.85, 0.9, 0.0, 0.0]},
    {'id': 'S1', 'values': [0.3, 0.35, 0.4, 0.0]},
    {'id': 'S3', 'values': [0.05, 0.06, 0.0, 0.0]},
    {'id': 'S2', 'values': [0.95, 1.0, 0.0]},
    {'id': 'S1', 'values': [0.5, 0.6, 0.7, 0.8, 0.0]}
]

thresholds = {
    'S1': 0.25,
    'S2': 0.75,
    'S3': 0.5
}

# Execution point of interest
final_score = calculate_final_score(data_log, thresholds)