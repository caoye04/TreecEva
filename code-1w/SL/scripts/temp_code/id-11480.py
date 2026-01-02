from collections import defaultdict

# Simulate sensor readings with some noise and redundancy
def generate_sensor_data():
    raw_readings = [12.5, 13.0, 11.8, 14.2, 13.1, 12.9, 13.3, 14.0]
    timestamps = list(range(len(raw_readings)))
    labeled_readings = dict(zip(timestamps, raw_readings))
    return labeled_readings

# Filter out fluctuations below sensitivity threshold
def filter_noise(data, threshold=0.3):
    filtered = {}
    prev = None
    for t, val in sorted(data.items()):
        if prev is None or abs(val - prev) >= threshold:
            filtered[t] = val
        prev = val
    return filtered

# Apply dynamic weighting based on time-of-day bias (simulated)
def apply_temporal_weights(data):
    weights = defaultdict(float)
    for t in data:
        if t < 3:
            weights[t] = 0.8
        elif t < 6:
            weights[t] = 1.0
        else:
            weights[t] = 1.2
    return weights

# Compute composite score with normalization and outlier dampening
def compute_normalized_contributions(readings, weights):
    contributions = []
    base_values = list(readings.values())
    mean_val = sum(base_values) / len(base_values)
    variance = sum((x - mean_val) ** 2 for x in base_values) / len(base_values)
    std_dev = variance ** 0.5
    
    for t, val in readings.items():
        z_score = (val - mean_val) / (std_dev + 1e-8)
        # Dampen extreme values
        adjusted_val = mean_val + z_score * min(abs(z_score), 2)
        weighted_contribution = adjusted_val * weights[t]
        contributions.append(weighted_contribution)
    
    # Irrelevant side computation - distractor
    entropy_proxy = 0.0
    for c in contributions:
        if c > 0:
            entropy_proxy -= c * math.log(c + 1e-6)
    
    return contributions

# Final aggregation with redundant checks
def compute_final_score(readings, weights):
    valid_keys = [k for k in readings.keys() if k >= 0]
    temp_store = []
    for i, k in enumerate(valid_keys):
        if k in weights:
            temp_store.append(readings[k] * weights[k])
    
    # Secondary processing path - partially redundant
    norm_contribs = compute_normalized_contributions(readings, weights)
    raw_total = sum(temp_store)
    norm_total = sum(norm_contribs)
    
    # Weighted blend - but norm_total dominates
    total_score = 0.3 * raw_total + 0.7 * norm_total
    
    # Dead code branch - red herring
    if len(readings) > 100:
        backup_estimator = max(norm_contribs) * len(norm_contribs)
        total_score = min(total_score, backup_estimator)
    
    # Final adjustment: offset by initial timestamp influence
    first_time = min(readings.keys())
    total_score -= first_time * 0.15
    
    return total_score

# Misleading auxiliary function that is never called
def estimate_error_margin(data):
    return sum(abs(x - 13.0) for x in data.values()) * 0.05

# Unused global variable - distraction
calibration_offset = 2.1

import math

# Main execution flow
data = generate_sensor_data()
data = filter_noise(data, threshold=0.35)
weights = apply_temporal_weights(data)
total_score = compute_final_score(data, weights)

# Additional irrelevant transformation
transformed_scores = [math.sin(v * 0.1) for v in data.values()]
summary_stat = sum(transformed_scores) / len(transformed_scores)

print(f"Result: {total_score}")