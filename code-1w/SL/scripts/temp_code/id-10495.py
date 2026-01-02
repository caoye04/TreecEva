def analyze_performance(metrics):
    # Irrelevant transformation
    temp_data = {k: v ** 2 for k, v in metrics.items() if v > 5}
    
    # Distractor computation
    outlier_count = 0
    for val in metrics.values():
        if val < 3 or val > 18:
            outlier_count += 1

    # Semi-relevant normalization (not used later)
    normalized = {k: (v - 5) / 10 for k, v in metrics.items()}

    # Key processing: filter and scale valid scores
    processed = {}
    for k, v in metrics.items():
        if 4 <= v <= 16:
            processed[k] = v * 1.5
    
    return processed


def calculate_stability_index(data):
    # Dead code path - never used
    if len(data) == 0:
        return 0
    variance = sum((x - 10) ** 2 for x in data.values())
    return variance // len(data) if data else 0


def calculate_final_score(results, thresholds):
    base_score = 0
    penalty = 0
    
    # Multiple nested logic with distractors
    for key, value in results.items():
        if key in thresholds:
            threshold_val = thresholds[key]
            if value >= threshold_val:
                base_score += value
            else:
                # Complex but ultimately minor penalty system
                diff = threshold_val - value
                if diff > 5:
                    penalty += 3
                elif diff > 2:
                    penalty += 2
                else:
                    penalty += 1
    
    # Distractor: unused aggregation
    avg_result = sum(results.values()) / len(results) if results else 0
    max_deviation = max(abs(v - avg_result) for v in results.values())

    # Final score calculation - only this matters
    final_score = base_score - penalty
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Main execution
raw_metrics = {
    'latency': 12,
    'throughput': 14,
    'accuracy': 9,
    'consistency': 6,
    'response_time': 11
}

thresholds_config = {
    'latency': 10,
    'throughput': 13,
    'accuracy': 8,
    'consistency': 5,
    'response_time': 12
}

# Process the metrics
filtered_results = analyze_performance(raw_metrics)

# Unused stability check
stability = calculate_stability_index(filtered_results)

# Critical statement
final_score = calculate_final_score(filtered_results, thresholds_config)