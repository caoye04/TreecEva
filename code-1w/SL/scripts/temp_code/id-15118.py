def evaluate_performance(metrics, data_map):
    baseline = { 'latency': 120, 'throughput': 85, 'error_rate': 0.013 }
    adjustment_factor = 0.89
    temp_result = 0
    final_score = 0
    
    # Irrelevant computation - distractor
    overhead = sum([baseline[k] * 0.01 for k in baseline if k != 'error_rate'])
    calibration_offset = overhead * adjustment_factor

    metric_set_normalized = set()
    for key in metrics:
        if key in data_map:
            if key == 'latency':
                normalized = max(0, 100 - (data_map[key] - baseline[key]) * 0.5)
                metric_set_normalized.add(round(normalized))
            elif key == 'throughput':
                normalized = min(100, (data_map[key] / baseline[key]) * 100)
                metric_set_normalized.add(round(normalized))
            elif key == 'error_rate':
                # Lower error rate is better
                penalty = data_map[key] / baseline[key] * 20
                metric_set_normalized.add(max(0, 100 - penalty))
    
    # Misleading control flow - dead branch
    if len(metric_set_normalized) > 10:
        fallback = sum(baseline.values())
        return fallback

    # Actual scoring logic
    raw_average = sum(metric_set_normalized) / len(metric_set_normalized)
    
    # Secondary adjustment based on coverage
    coverage_ratio = len(metric_set_normalized) / len(baseline)
    coverage_bonus = 10 if coverage_ratio >= 0.8 else 5 if coverage_ratio >= 0.6 else 0
    
    # Auxiliary variable with no impact
    diagnostic_trace = { 'avg': raw_average, 'coverage': coverage_ratio, 'calibration': calibration_offset }
    
    # Final score calculation
    final_score = int(raw_average + coverage_bonus)
    
    # Red herring: unused transformation
    transformed_scores = [s * adjustment_factor for s in metric_set_normalized]
    smoothed = sum(transformed_scores) / len(transformed_scores) if transformed_scores else 0
    
    return final_score

# Main execution context
benchmark_data = {
    'latency': 110,
    'throughput': 92,
    'error_rate': 0.011
}
metric_set = ['latency', 'throughput', 'error_rate']

auxiliary_weight = 1.05  # Unused in logic
normalization_cache = {}  # Dead storage

final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")