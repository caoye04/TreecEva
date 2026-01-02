from itertools import combinations

# Simulate sensor anomaly detection with feedback weighting
def analyze_sensor_reads(readings):
    base_threshold = 25
    anomalies = []
    weighted_sum = 0
    temp_cache = {}

    for i, val in enumerate(readings):
        if val > base_threshold:
            anomalies.append(i)
        weighted_sum += val * (i + 1)

    # Irrelevant combination analysis (distractor)
    for r in range(2, 4):
        combo_count = 0
        for _ in combinations(readings, r):
            combo_count += 1
        temp_cache[r] = combo_count  # Dead-end computation

    normalized_weight = weighted_sum / len(readings) if readings else 0
    return anomalies, normalized_weight


def evaluate_stability(indices, raw_data):
    if not indices:
        return 0.0
    
    peak_variation = max(raw_data) - min(raw_data)
    index_fluctuation = sum(abs(indices[i] - indices[i-1]) for i in range(1, len(indices)))
    
    # Misleading stability metric (not used later)
    fake_stability = (peak_variation + index_fluctuation) / (len(indices) + 1)
    
    real_stability = len(indices) * 1.5 - peak_variation * 0.3
    return real_stability

# Main processing chain
def generate_feedback(anomalies, weight):
    levels = set()
    for idx in anomalies:
        if idx % 3 == 0:
            levels.add('critical')
        elif idx % 2 == 0:
            levels.add('warning')
        else:
            levels.add('info')
    
    level_map = {'critical': 5, 'warning': 3, 'info': 1}
    total_level_value = sum(level_map.get(lv, 0) for lv in levels)
    
    # Extra distraction: unused transformation
    transformed = [total_level_value ** (1+i) for i in range(2)]
    
    return list(levels), total_level_value

# Final aggregation logic
def aggregate_performance(metrics):
    score_basis = 10
    adjustment = 0
    
    for m in metrics:
        if m == 'critical':
            adjustment -= 2
        elif m == 'warning':
            adjustment += 1
        elif m == 'info':
            adjustment += 0.5
    
    final_value = score_basis + adjustment
    return final_value

# Execution sequence
sensor_data = [20, 30, 40, 15, 50, 60]
anomaly_indices, avg_weight = analyze_sensor_reads(sensor_data)
stability_metric = evaluate_stability(anomaly_indices, sensor_data)
feedback_types, level_sum = generate_feedback(anomaly_indices, avg_weight)
final_score = aggregate_performance(feedback_types)

print(f"Result: {final_score}")