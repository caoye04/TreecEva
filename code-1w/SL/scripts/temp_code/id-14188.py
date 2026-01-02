def analyze_trend(data, threshold=0.5):
    trend_vector = [1 if v > threshold else -1 for v in data]
    return sum(trend_vector)

# Simulate sensor stability index (irrelevant computation)
stability_log = [0.87, 0.91, 0.88, 0.90]
baseline_offset = 0.02
calibrated_stability = [s + baseline_offset for s in stability_log]

# Key performance metrics from system logs
metrics = {
    'latency': 0.45,
    'throughput': 0.88,
    'consistency': 0.76,
    'availability': 0.93
}

# Weight mapping using lambda for dynamic adjustment
weight_adjuster = lambda base: {k: base * (1.1 if k in ['throughput', 'availability'] else 0.9) for k in metrics.keys()}
weights = weight_adjuster(0.25)

# Auxiliary function to compute weighted score
def evaluate_performance(met, wgt):
    # Initialize accumulators
    raw_sum = 0.0
    weight_sum = 0.0
    adjusted_metrics = {}
    
    # Preprocess metrics with normalization (some are already normalized)
    for key in met:
        normalized_val = min(max(met[key], 0.0), 1.0)
        adjusted_metrics[key] = normalized_val ** 0.5 if key == 'latency' else normalized_val
    
    # Apply weights
    for k in met:
        contribution = adjusted_metrics[k] * wgt[k]
        raw_sum += contribution
        weight_sum += wgt[k]
    
    # Compute final weighted score
    performance_index = raw_sum / weight_sum if weight_sum > 0 else 0.0
    
    # Additional logic to simulate conditional bonus
    bonus_eligible = all(met[k] >= 0.75 for k in ['throughput', 'availability'])
    bonus_factor = 1.1 if bonus_eligible else 1.0
    
    # Final scoring with bonus
    final = performance_index * bonus_factor
    
    # Dead code branch - never executed but adds cognitive load
    if False:
        fallback = sum(met.values()) / len(met)
        final = max(final, fallback)
    
    return round(final, 4)

# Irrelevant list processing (distractor)
dummy_labels = ['A', 'B', 'C']
label_map = {lbl: idx for idx, lbl in enumerate(dummy_labels)}

# Execute main evaluation
temp_data = [0.3, 0.6, 0.7]
_ = analyze_trend(temp_data, threshold=0.5)  # Unused result

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")