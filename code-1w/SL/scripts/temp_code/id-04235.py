def evaluate_performance(data, config):
    threshold = 75
    adjustment = 0.1
    base_multiplier = len(data) * 0.5

    # Irrelevant preprocessing (distractor)
    normalized = [max(0, min(x, 100)) for x in data]
    outliers = [x for x in normalized if x < 20 or x > 90]
    
    # Semi-relevant transformation
    weighted_values = list(map(lambda x, w: x * w, data, config))
    
    # Core logic hidden among distractions
    avg = sum(weighted_values) / len(weighted_values) if weighted_values else 0
    
    # Red herring computation (dead path due to fixed condition)
    penalty = 0
    if len(outliers) > 100:  # Impossible given input size
        penalty = len(outliers) * 2
    
    # Actual score calculation
    if avg >= threshold:
        final = avg * base_multiplier + adjustment
    else:
        final = avg - penalty  # penalty always 0
    
    # Extra noise
    debug_info = {'input_count': len(data), 'has_outliers': bool(outliers)}
    return int(final)

# Main execution
metrics = [88, 92, 76, 85, 91]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Unused variables (distractors)
calibration_data = [0.5, 0.7, 0.6]
scaling_factor = sum(calibration_data) * 2.1
placeholder_result = None

intermediate_total = sum(x ** 0.5 for x in metrics)  # unused

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")