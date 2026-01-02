def evaluate_performance(metrics, cutoff):
    active_metrics = {x for x in metrics if x > 0}
    outliers = {x for x in metrics if x > 2 * cutoff}
    valid_metrics = active_metrics - outliers

    # Irrelevant tracking variables (distractors)
    peak_value = max(metrics)
    normalized_sum = sum(x / peak_value for x in valid_metrics)
    adjustment_factor = len(outliers) * 0.5 if outliers else 0

    base_score = sum(valid_metrics)
    penalty = 0
    for val in valid_metrics:
        if val < cutoff:
            # Nested condition with moderate depth
            for i in range(2):
                if i == 1 and val < cutoff * 0.5:
                    penalty += 1
    
    # Secondary computation that doesn't affect final result
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    fluctuation_index = sum(1 for i in range(1, len(metrics)) if metrics[i] != metrics[i-1])

    # Core logic step
    final_score = base_score - penalty + adjustment_factor  # adjustment_factor not actually used in pure logic

    # Dead code path (irrelevant function call)
    def log_analysis():
        return "Analysis complete"
    
    _ = log_analysis()  # Misleading side effect

    return int(final_score)

# Main execution
productivity_data = [12, -5, 30, 15, 0, 25, 8, 3]
cutoff_threshold = 10

# Set conversion for filtering
productivity_set = set(productivity_data)

# Key statement
final_score = evaluate_performance(productivity_set, cutoff_threshold)

print(f"Target result: {final_score}")