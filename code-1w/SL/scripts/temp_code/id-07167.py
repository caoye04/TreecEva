from itertools import compress, cycle

# Simulate sensor data processing with weighted reliability scoring
def collect_diagnostics():
    base_readings = [85, 90, 78, 92, 88]
    calibration_offset = 2
    adjusted = [r + calibration_offset for r in base_readings]
    
    # Irrelevant filtered version (dead-end computation)
    high_only = [v for v in adjusted if v > 85]
    normalized = [(x - min(adjusted)) / (max(adjusted) - min(adjusted)) * 100 for x in adjusted]
    
    return normalized

def compute_stability_index(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    avg_change = sum(diffs) / len(diffs)
    stability = 100 - (avg_change * 2)
    return round(stability, 2)

def apply_correction_factor(val, factor=0.95):
    # Unused helper function (distractor)
    return val * factor

def evaluate_performance(metrics, weights):
    # Core logic: weighted sum of key metrics
    w_acc = weights['accuracy']
    w_prec = weights['precision']
    w_stab = weights['stability']
    
    accuracy_metric = metrics['accuracy']
    precision_metric = metrics['precision']
    stability_metric = metrics['stability']
    
    # Misleading intermediate calculation (not used in final result)
    raw_total = accuracy_metric + precision_metric + stability_metric
    adjustment_pass = raw_total * 0.01 if raw_total > 200 else 0
    
    # Actual answer computation
    weighted_sum = w_acc * accuracy_metric + w_prec * precision_metric + w_stab * stability_metric
    
    # Extra unused branching (distractor path)
    if weighted_sum < 80:
        fallback_mode = True
        correction_hook = lambda x: x * 1.1
    else:
        fallback_mode = False  # This path taken, but doesn't affect output
    
    return int(round(weighted_sum))

# Main execution flow
data_stream = collect_diagnostics()
accuracy_score = data_stream[0]  # Most recent reading as accuracy proxy
precision_score = sum(data_stream) / len(data_stream)  # Average consistency
stability_index = compute_stability_index(data_stream)

# Additional irrelevant aggregation (distractor)
rolling_window = list(zip(data_stream, data_stream[1:]))
pair_trends = [1 if b > a else 0 for a, b in rolling_window]
trend_bias = sum(pair_trends)

# Build metric dictionary
performance_metrics = {
    'accuracy': accuracy_score,
    'precision': precision_score,
    'stability': stability_index,
    'redundant_flag': False  # Unused field
}

# Weight configuration (critical for final computation)
weight_scheme = {
    'accuracy': 0.4,
    'precision': 0.35,
    'stability': 0.25
}

# Apply weighting model
temp_buffer = [x * 0.99 for x in data_stream]  # Distractor buffer
final_score = evaluate_performance(performance_metrics, weight_scheme)

# Print result for extraction
print(f"Result: {final_score}")