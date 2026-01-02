import itertools

# Simulate sensor array readings with noise filtering
def collect_filtered_readings(raw_data, threshold=0.5):
    filtered = []
    cumulative = 0
    for val in raw_data:
        if abs(val) > threshold:
            cumulative += val * 0.9
            filtered.append(cumulative)
    return filtered

# Analyze temporal patterns in sensor data
def detect_anomalies(series):
    anomalies = 0
    for i in range(1, len(series)):
        diff = series[i] - series[i-1]
        if diff > 1.2 or diff < -1.2:
            anomalies += 1
    return anomalies

# Compute weighted reliability index across multiple dimensions
def compute_reliability_index(readings, weights):
    base_score = sum(abs(r) for r in readings)
    adjustment_factor = 1.0
    temp_sum = 0
    
    # Irrelevant accumulation (distractor)
    for _ in itertools.repeat(None, 3):
        temp_sum += len(readings) // 2
    
    if len(readings) > 5:
        adjustment_factor *= 0.85
    else:
        adjustment_factor *= 1.1
    
    # Semi-relevant transformation
    smoothed = [readings[0]]
    for i in range(1, len(readings)):
        smoothed.append((smoothed[-1] + readings[i]) * 0.5)
    
    smoothing_effect = sum(smoothed) / (sum(readings) + 1e-8)
    adjustment_factor *= max(0.7, min(1.3, smoothing_effect))
    
    return base_score * adjustment_factor

# Final performance evaluation combining multiple metrics
def evaluate_performance(weight_vector, results_map):
    metric_weights = weight_vector
    raw_results = results_map
    
    processed = {}
    for k, v in raw_results.items():
        if k == 'sensor_a':
            processed[k] = sum(x ** 0.5 for x in v if x > 0)
        elif k == 'sensor_b':
            processed[k] = sum(x ** 2 for x in v) / len(v)
        else:
            processed[k] = sum(v)
    
    # Dead code path (distractor)
    if False:
        backup_weights = [w * 2 for w in metric_weights]
        fallback = sum(backup_weights)

    composite = 0
    total_weight = sum(metric_weights)
    
    # Introduce bitwise distraction
    magic_offset = 0
    for i, w in enumerate(metric_weights):
        if i % 2 == 0:
            magic_offset ^= int(w * 10) & 7
    
    # Actual computation path
    for idx, (key, score) in enumerate(processed.items()):
        weight = metric_weights[idx] if idx < len(metric_weights) else 0.5
        composite += weight * score
        
        # Misleading intermediate calculation
        temp_debug = score * (weight + 1) / (idx + 1)

    final_adjustment = detect_anomalies([1, 1.1, 0.9, 2.3, 2.4, 0.1])
    composite /= (total_weight + 1e-8)
    
    # Key statement
    final_score = int(composite - magic_offset + final_adjustment)
    
    # Irrelevant combinatorics (distractor)
    combo_count = 0
    for combo in itertools.combinations([1,2,3,4], 3):
        combo_count += 1
    
    return final_score

# Main execution
raw_sensor_data = {
    'sensor_a': [0.1, 0.8, -1.2, 0.5, 2.1, -0.3],
    'sensor_b': [0.4, 0.6, 0.5, 0.7],
    'sensor_c': [1.1, 2.2, 1.9]
}

weights = [0.6, 0.9, 1.2]

filtered_a = collect_filtered_readings(raw_sensor_data['sensor_a'])
reliability = compute_reliability_index(filtered_a, weights)

# Execution point of interest
final_score = evaluate_performance(weights, raw_sensor_data)
print(f"Target result: {final_score}")