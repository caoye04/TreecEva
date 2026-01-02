def evaluate_performance(metrics, threshold):
    # Irrelevant preprocessing: normalize unused fields
    normalized = [m / max(metrics) for m in metrics]
    
    # Distractor computation: calculate entropy (not used)
    import math
    entropy = sum(-p * math.log2(p) for p in normalized if p > 0)

    # Key logic begins
    high_performers = list(filter(lambda x: x > threshold, metrics))
    bonus_factor = 1.5 if len(high_performers) > 2 else 1.0
    
    # Secondary filtering: based on volatility
    avg = sum(metrics) / len(metrics)
    deviations = [abs(x - avg) for x in metrics]
    volatile_count = sum(1 for d in deviations if d > avg * 0.3)

    adjustment = 0.9 if volatile_count > len(metrics) // 2 else 1.0
    
    # Core scoring
    base_score = sum(metrics)
    penalty = 10 if any(m < threshold * 0.5 for m in metrics) else 0
    
    # Final composition
    raw_final = (base_score - penalty) * bonus_factor * adjustment
    
    # Dead code path: never executed due to data range
    if threshold < 0:
        raw_final = abs(raw_final)
    
    return int(raw_final)

# Main execution
metric_data = [85, 90, 92, 45, 88]
base_threshold = 80

# Auxiliary variable with misleading name
aggregate_result = sum(x**2 for x in metric_data)  # Unused

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

# Print result
print(f"Result: {final_score}")