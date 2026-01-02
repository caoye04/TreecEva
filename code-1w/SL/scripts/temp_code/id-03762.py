from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [85, 90, 78, 92, 88, 76, 95, 89]
    metrics = defaultdict(int)
    
    # Irrelevant aggregation (distractor)
    temp_aggregates = []
    for val in raw_data:
        if val > 80:
            temp_aggregates.append(val * 0.1)
    
    # Relevant calculations
    metrics['avg_response'] = sum(raw_data) / len(raw_data)
    metrics['peak_utilization'] = max(raw_data)
    metrics['stability_ratio'] = len([x for x in raw_data if x >= 85]) / len(raw_data)
    
    # Dead code path (distractor)
    if False:
        metrics['placeholder'] = 0
    
    return metrics

def apply_correction_factor(data):
    # Minor adjustment to certain metrics
    corrected = data.copy()
    correction_applied = False
    
    if corrected['avg_response'] < 88:
        corrected['avg_response'] += 2.5
        correction_applied = True
    
    # Tracking variable not used later (distractor)
    log_entry = f"Correction {'was' if correction_applied else 'was not'} applied."
    
    return corrected

def calculate_derived_index(vals):
    # Compute a composite index (not directly used)
    index = 0
    weights = [0.1, 0.3, 0.6]
    for i, key in enumerate(['avg_response', 'peak_utilization', 'stability_ratio']):
        if i < len(weights):
            index += vals[key] * weights[i]
    return round(index, 3)

def evaluate_performance(metrics, weights):
    score = 0.0
    # Apply weighted scoring
    for key, weight in weights.items():
        if key in metrics:
            score += metrics[key] * weight
    
    # Additional logic step: bonus for high stability
    if metrics['stability_ratio'] > 0.6:
        score *= 1.1
    
    # Red herring computation (uses copied data but no effect)
    dummy_metrics = metrics.copy()
    dummy_metrics['avg_response'] = dummy_metrics['avg_response'] * 0.98
    
    return int(round(score))

# Main execution flow
raw_metrics = collect_metrics()
adjusted_metrics = apply_correction_factor(raw_metrics)

# Unused derived value (distractor)
derived_index = calculate_derived_index(adjusted_metrics)

# Weight configuration for evaluation
benchmark_weights = {
    'avg_response': 0.4,
    'peak_utilization': 0.35,
    'stability_ratio': 0.25
}

# Critical statement
final_score = evaluate_performance(adjusted_metrics, benchmark_weights)

print(f"Result: {final_score}")