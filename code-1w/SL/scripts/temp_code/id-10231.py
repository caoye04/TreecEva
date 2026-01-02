def evaluate_performance(metrics, baseline):
    # Irrelevant transformation: noise filter (not used in result)
    filtered_noise = {k: v * 0.95 for k, v in metrics.items() if 'error' in k}
    
    # Distractor computation: confidence level (semi-relevant but unused)
    confidence_level = sum(metrics.get(k, 0) for k in metrics if 'precision' in k) / len(metrics)

    # Core logic begins: efficiency ratio calculation
    efficiency_ratios = []
    for key, value in metrics.items():
        if 'throughput' in key:
            base_val = baseline.get(key, 1.0)
            efficiency_ratios.append(value / base_val)
    
    avg_efficiency = sum(efficiency_ratios) / len(efficiency_ratios) if efficiency_ratios else 0

    # Use set operations to identify anomalous dimensions
    metric_keys = set(metrics.keys())
    baseline_keys = set(baseline.keys())
    common_dims = metric_keys & baseline_keys  # Intersection
    missing_in_baseline = metric_keys - baseline_keys  # Difference

    # Bonus applied if no missing dimensions
    completeness_bonus = 10 if not missing_in_baseline else 0

    # Recursive depth counter (simple recursion)
    def calculate_depth(d):
        return 1 + sum(calculate_depth(v) for v in d.values() if isinstance(v, dict)) if d else 0
    
    hierarchy = {'system': {'cpu': {}, 'gpu': {'thread': {}}}}
    depth_penalty = calculate_depth(hierarchy) * -2

    # Tuple unpacking for version info (distractor with partial relevance)
    version_info = ('v2', 'patch_3', 'release')
    ver_tag, _, release_type = version_info
    version_multiplier = 1.1 if release_type == 'release' else 0.9

    # Final score computation (depends only on avg_efficiency, bonus, and penalty)
    final_score = (avg_efficiency * 100) + completeness_bonus + depth_penalty
    return final_score

# Main execution
baseline_metrics = {
    'throughput_batch': 80,
    'throughput_stream': 120,
    'error_rate': 0.05
}

current_metrics = {
    'throughput_batch': 96,
    'throughput_stream': 144,
    'error_rate': 0.03,
    'precision_top1': 0.92,
    'precision_top5': 0.98
}

# Key statement
final_score = evaluate_performance(current_metrics, baseline_metrics)
print(f"Result: {final_score}")