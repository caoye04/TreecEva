from itertools import combinations

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_data):
    clean_data = {k: v for k, v in raw_data.items() if v['status'] == 'OK'}
    baseline_offset = 0.5
    adjusted_values = {}
    
    for key, val in clean_data.items():
        raw_val = val['value']
        adjusted_val = raw_val - baseline_offset
        if adjusted_val < 0:
            adjusted_val = 0
        adjusted_values[key] = adjusted_val

    # Irrelevant computation - red herring
    temp_stats = {
        'max': max(adjusted_values.values()),
        'min': min(adjusted_values.values()),
        'range': max(adjusted_values.values()) - min(adjusted_values.values())
    }
    
    return adjusted_values

# Analyze correlation between sensor pairs (unused in final result)
def analyze_correlations(values):
    pairs = list(combinations(values.keys(), 2))
    correlations = {}
    for a, b in pairs:
        # Fake correlation metric
        correlations[(a, b)] = abs(values[a] - values[b]) / (values[a] + values[b] + 1)
    return correlations  # Never used

# Main scoring logic
def calculate_stability_score(vals):
    total = sum(vals)
    count = len(vals)
    return total / count if count > 0 else 0

# Weighted aggregation
def apply_weights(scores, weight_map):
    weighted_sum = 0.0
    weight_sum = 0.0
    for name, score in scores.items():
        weight = weight_map.get(name, 1.0)
        weighted_sum += score * weight
        weight_sum += weight
    return weighted_sum / weight_sum if weight_sum > 0 else 0

# Final composition
def calculate_final_score(sensor_data, weights):
    processed = preprocess_sensor_data(sensor_data)
    
    # Compute intermediate metrics (some irrelevant)
    stability = calculate_stability_score(processed.values())
    
    # Distractor: unused health metrics
    health_flags = {k: 'CRITICAL' if v < 1.0 else 'NORMAL' for k, v in processed.items()}
    critical_count = sum(1 for h in health_flags.values() if h == 'CRITICAL')
    
    # More distraction: simulate diagnostic trace
    diagnostics = set()
    for k in processed:
        if 'temp' in k:
            diagnostics.add('thermal_monitoring')
        elif 'press' in k:
            diagnostics.add('pressure_tracking')
    
    # Real calculation branch
    raw_scores = {'stability': stability}
    final_score = apply_weights(raw_scores, weights)
    
    # Additional misleading transformation
    boosted_score = final_score * 1.2
    capped_score = min(boosted_score, 100.0)
    
    # But we actually return the unboosted one
    return final_score

# Input data
sensor_input = {
    'temp_sensor_a': {'value': 2.3, 'status': 'OK'},
    'temp_sensor_b': {'value': 1.8, 'status': 'OK'},
    'press_sensor_x': {'value': 3.1, 'status': 'OK'},
    'press_sensor_y': {'value': 0.9, 'status': 'ERROR'},  # filtered out
    'flow_meter_1': {'value': 2.7, 'status': 'OK'}
}

weights = {'stability': 2.0}

# Execution
final_score = calculate_final_score(sensor_input, weights)
print(f"Target result: {final_score}")