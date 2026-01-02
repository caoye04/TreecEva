from collections import defaultdict
import math

# Simulate sensor data with noise and redundancy
def preprocess_sensor_data(raw_readings):
    cleaned = []
    temp_store = []
    outlier_threshold = 3.5
    mean = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = math.sqrt(variance)

    # Misleading filtering (not actually used in final path)
    for val in raw_readings:
        if abs(val - mean) <= outlier_threshold * std_dev:
            temp_store.append(val)

    # Actual relevant processing
    filtered = [x for x in raw_readings if x > 0]  # Only positive readings valid
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    return normalized

# Analyze pattern frequency in normalized signals
def extract_patterns(data_sequence):
    pattern_counts = defaultdict(int)
    binary_states = ['low' if x < 0.5 else 'high' for x in data_sequence]
    
    # Dummy tracking variables (distractors)
    state_transitions = 0
    prev = binary_states[0]
    for curr in binary_states[1:]:
        if curr != prev:
            state_transitions += 1
        prev = curr

    # Real work: count high/low runs
    current_run = 1
    for i in range(1, len(binary_states)):
        if binary_states[i] == binary_states[i-1]:
            current_run += 1
        else:
            run_label = f"{binary_states[i-1]}_{current_run}"
            pattern_counts[run_label] += 1
            current_run = 1
    # Final run
    run_label = f"{binary_states[-1]}_{current_run}"
    pattern_counts[run_label] += 1

    return dict(pattern_counts)

# Core scoring logic
def calculate_final_score(features, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    total_weight = sum(importance_weights.values())
    
    # Irrelevant normalization step (dead computation)
    normalized_weights = {k: v / total_weight for k, v in importance_weights.items()}

    # Relevant scoring
    for feature, count in features.items():
        category = feature.split('_')[0]
        magnitude = int(feature.split('_')[1])
        weight = importance_weights.get(category, 0.1)
        contribution = count * magnitude * weight
        base_score += contribution

        # Red herring: unused penalty logic
        if magnitude > 5:
            penalty_adjustment += 0.25

    scaled_score = base_score * 0.87  # Calibration factor
    return int(scaled_score)

# Main execution
if __name__ == "__main__":
    raw_sensor_data = [0.1, -0.2, 0.4, 0.4, 0.9, 0.9, 0.9, 0.3, 0.8, 0.8, 0.8, 0.8, -0.5, 0.6]
    config_params = {'low': 1.2, 'high': 1.8}
    debug_mode = True
    
    processed_data = preprocess_sensor_data(raw_sensor_data)
    patterns = extract_patterns(processed_data)
    weights = {'low': 2, 'high': 3}
    
    # Key statement
    final_score = calculate_final_score(patterns, weights)
    
    # Output result
    print(f"Result: {final_score}")