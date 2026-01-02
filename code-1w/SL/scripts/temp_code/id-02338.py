def process_results(data, importance_weights):
    # Initialize tracking variables
    temp_sum = 0
    adjustment_factor = 0.85
    outlier_count = 0
    normalized_values = []

    # Preprocess: filter and normalize data
    for val in data:
        if val < 0 or val > 100:
            outlier_count += 1
            continue
        normalized_values.append(val / 100.0)

    # Apply lambda-based transformation for non-linear scaling
    scaled_values = list(map(lambda x: x ** 1.5, normalized_values))

    # Simulate irrelevant secondary analysis (distractor)
    avg_normalized = sum(normalized_values) / len(normalized_values) if normalized_values else 0
    variance_proxy = sum((x - avg_normalized) ** 2 for x in normalized_values) / len(normalized_values) if normalized_values else 0

    # Core scoring logic with weighted accumulation
    weighted_accum = 0
    for i, scaled in enumerate(scaled_values):
        weight = importance_weights[i % len(importance_weights)]
        weighted_accum += scaled * weight

    # Secondary distractor: unused complexity
    def analyze_trend(seq):
        return 'increasing' if seq and seq[-1] > seq[0] else 'stable_or_decreasing'
    
    trend = analyze_trend([int(x*100) for x in normalized_values])  # Not used later

    # Final computation with rounding and adjustment
    raw_score = weighted_accum * 100
    adjusted_score = raw_score * adjustment_factor
    final_score = int(round(adjusted_score))  # Final deterministic result

    # Irrelevant debug print (not affecting logic)
    debug_info = {'outliers_removed': outlier_count, 'trend_analysis': trend}

    return final_score

# Main execution context
raw_data = [85, 90, 78, 105, 92, -5, 88, 96]
weights = [0.3, 0.5, 0.7, 0.4]

intermediate_total = sum(x for x in raw_data if 0 <= x <= 100)  # Distractor variable
unused_threshold = 80.0  # Dead code variable

final_score = process_results(raw_data, weights)
print(f"Result: {final_score}")