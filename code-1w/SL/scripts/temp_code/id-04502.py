from collections import defaultdict

# Simulate sensor readings with noise and calibration
def generate_sensor_data():
    raw_data = [105, 98, 110, 92, 108]
    calibrated = [val - 5 for val in raw_data]
    return calibrated

# Filter out extreme values based on dynamic threshold
def filter_outliers(data, threshold=10):
    median_val = sorted(data)[len(data)//2]
    filtered = [x for x in data if abs(x - median_val) <= threshold]
    return filtered

# Apply weighted scoring using configuration map
def compute_weighted_scores(entries, config_map):
    score_dict = defaultdict(float)
    total_weight = sum(config_map.values())
    
    for i, val in enumerate(entries):
        weight = config_map.get(i % len(config_map), 1.0)
        score_dict[i] = val * weight
    
    # Irrelevant accumulation (distractor)
    temp_sum = 0
    for v in score_dict.values():
        temp_sum += v * 0.1  # Noise contribution, not used later
    
    return dict(score_dict)

# Main computation logic
def compute_final_score(readings, weights):
    adjusted = [x * 0.95 for x in readings]  # Minor correction factor
    scores = compute_weighted_scores(adjusted, weights)
    
    # Secondary processing: only use even-indexed contributions
    final_value = 0
    for idx, s in scores.items():
        if idx % 2 == 0:
            final_value += s
    
    # Dead code path - looks relevant but unused (distractor)
    if len(scores) > 10:
        fallback = sum(scores.values()) / len(scores)
        final_value = fallback  # Never reached
    
    # Additional red herring calculation
    phantom_correction = 0
    for k in range(len(adjusted)):
        phantom_correction += adjusted[k] % (k + 1) if k != 0 else 0
    
    return int(final_value)

# Execution flow
if __name__ == "__main__":
    data = generate_sensor_data()
    clean_data = filter_outliers(data, threshold=12)
    
    # Weight configuration for scoring (real impact)
    weights = {0: 1.2, 1: 0.8, 2: 1.5}
    
    # Spurious intermediate variable (distractor)
    normalized = [round(x / max(clean_data), 2) for x in clean_data]
    
    # Key execution point
    final_score = compute_final_score(clean_data, weights)
    
    # Output result as required
    print(f"Result: {final_score}")