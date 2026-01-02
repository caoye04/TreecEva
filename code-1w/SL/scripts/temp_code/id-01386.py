from itertools import compress, cycle

def analyze_performance(metrics, thresholds):
    # Initialize tracking variables
    above_threshold = []
    performance_flags = []
    temp_accumulator = 0
    
    for i, metric in enumerate(metrics):
        if metric > thresholds[i % len(thresholds)]:
            above_threshold.append(True)
            temp_accumulator += 0.1  # Distractor: not used later
        else:
            above_threshold.append(False)
    
    # Use of lambda and filtering
    significant_metrics = list(filter(lambda x: x > 0.5, metrics))
    filtered_indices = [i for i, m in enumerate(metrics) if m > 0.5]
    
    # Distractor computation with set operations
    unique_vals = set(round(m * 10) for m in metrics)
    baseline_refs = set(range(4, 9))
    overlap_count = len(unique_vals & baseline_refs)  # Used only for flagging
    
    performance_flags = list(compress(metrics, above_threshold))
    
    # Normalize performance flags by length (avoid division by zero)
    norm_factor = len(performance_flags) if performance_flags else 1
    normalized_score = sum(performance_flags) / norm_factor
    
    return normalized_score, significant_metrics, filtered_indices

def scale_metrics(raw_scores, multiplier=2.5):
    # Apply nonlinear scaling
    scaled = [(x ** 1.1) * multiplier for x in raw_scores]
    
    # Dead code path - never executed under current logic
    if len(scaled) > 100:
        fallback = sum(scaled) / 100
        return [fallback]
    
    padding_offset = 0.01 * len(scaled)  # Unused distraction
    return [s + 0.05 for s in scaled]  # Minor adjustment

def compute_aggregate(values, importance_weights):
    weighted_sum = 0
    total_weight = 0
    
    # Simultaneous iteration with cycling weights
    weight_cycle = cycle(importance_weights)
    for v in values:
        w = next(weight_cycle)
        weighted_sum += v * w
        total_weight += w
    
    # Early termination condition that doesn't trigger
    if total_weight == 0:
        return 0.0
    
    # Final aggregation
    aggregate = weighted_sum / total_weight
    
    # Additional rounding to simulate precision requirements
    return round(aggregate, 4)

# Main execution block
if __name__ == "__main__":
    # Input data
    raw_metrics = [0.68, 0.72, 0.54, 0.81, 0.63, 0.77, 0.59]
    decision_thresholds = [0.6, 0.65, 0.55]
    weights = [0.8, 1.2, 1.0, 0.9]

    # Step 1: Analyze performance against dynamic thresholds
    score_component, key_metrics, indices = analyze_performance(raw_metrics, decision_thresholds)
    
    # Intermediate distractor variables
    avg_metric = sum(raw_metrics) / len(raw_metrics)
    peak_value = max(raw_metrics)
    shape_factor = len(key_metrics) / len(raw_metrics) if raw_metrics else 0
    
    # Step 2: Scale the original metrics nonlinearly
    scaled_values = scale_metrics(raw_metrics)
    
    # Step 3: Compute final weighted aggregate
    final_score = compute_aggregate(scaled_values, weights)
    
    # Output result as required
    print(f"Result: {final_score}")