def analyze_metrics(data_set):
    baseline = sum(data_set) / len(data_set)
    deviation = [abs(x - baseline) for x in data_set]
    outlier_threshold = baseline * 0.2
    outliers = [x for x in data_set if abs(x - baseline) > outlier_threshold]
    filtered = [x for x in data_set if x not in outliers]  # Remove outliers
    return sum(filtered) / len(filtered) if filtered else baseline


def calculate_performance(results, adj):
    adjusted_results = [val * (1 + adj) for val in results]
    mean_val = sum(adjusted_results) / len(adjusted_results)
    
    # Simulate phase shift correction (irrelevant to final result)
    shifted = [mean_val * 0.95] * len(adjusted_results)
    dummy_sum = sum(shifted) * 0.1  # Distractor computation

    # Apply conditional boost based on performance tier
    performance_tier = 'high' if mean_val >= 80 else 'low'
    bonus = 10 if performance_tier == 'high' else 0
    
    # Unrelated set operations for distraction
    categories = {'A', 'B', 'C'}
    exclusions = {'C', 'D'}
    valid_categories = categories - exclusions
    category_count = len(valid_categories)  # Not used later

    # Final score with bonus
    final_score = mean_val + bonus
    
    # Dead code branch (never executed)
    if len(results) < 0:
        final_score -= 5
        redundant_adjustment = 2.0
        final_score *= redundant_adjustment

    return final_score

# Main execution block
raw_data = [75, 82, 78, 90, 85, 60, 95]
adjustment_factor = 0.05

# Preliminary analysis (distraction)
smoothed_data = [x * 1.02 for x in raw_data]
interim_avg = sum(smoothed_data) / len(smoothed_data)
proxy_metric = analyze_metrics(smoothed_data)  # Unused

benchmark_results = [76, 80, 84, 88, 92]
final_score = calculate_performance(benchmark_results, adjustment_factor)
print(f"Result: {final_score}")