def evaluate_performance(metrics, weights):
    # Normalize metrics to a 0-1 scale
    normalized = {}
    for k, v in metrics.items():
        if v > 100:
            normalized[k] = 1.0
        elif v < 0:
            normalized[k] = 0.0
        else:
            normalized[k] = v / 100.0

    # Apply weight adjustments based on priority tiers
    adjusted_scores = []
    tier_mapping = {'critical': 1.5, 'important': 1.2, 'routine': 1.0, 'optional': 0.8}
    priority_tiers = {
        'latency': 'critical',
        'throughput': 'important',
        'accuracy': 'critical',
        'memory_usage': 'routine',
        'cache_hit_rate': 'important'
    }

    temp_debug_sum = 0
    for metric_name, base_value in normalized.items():
        if metric_name in weights:
            tier = priority_tiers.get(metric_name, 'routine')
            weight = weights[metric_name]
            adjusted = base_value * weight * tier_mapping[tier]
            adjusted_scores.append(adjusted)
            temp_debug_sum += adjusted  # Not used in final result

    # Simulate historical comparison (distractor computation)
    historical_averages = [0.82, 0.79, 0.83, 0.80, 0.81]
    avg_historical = sum(historical_averages) / len(historical_averages)
    improvement_count = 0
    for s in adjusted_scores:
        if s > avg_historical:
            improvement_count += 1

    # Calculate composite using only specific components
    critical_metrics = ['latency', 'accuracy']
    critical_weight_sum = sum(weights[m] for m in critical_metrics)
    critical_score_sum = 0
    for m in critical_metrics:
        norm_val = normalized[m]
        crit_weight = weights[m]
        critical_score_sum += norm_val * crit_weight

    # Final aggregation uses only critical score and throughput
    throughput_score = normalized['throughput'] * weights['throughput']
    raw_final = (critical_score_sum + throughput_score) * 100

    # Apply arbitrary scaling factor observed in legacy systems
    legacy_factor = 0.97
    final_score = int(raw_final * legacy_factor)

    # Dead code branch - never executed under current logic
    if False:
        fallback = sum(normalized.values()) * 50
        final_score = fallback

    return final_score

# Main execution block
def main():
    metric_set = {
        'latency': 94,
        'throughput': 87,
        'accuracy': 96,
        'memory_usage': 70,
        'cache_hit_rate': 85
    }

    benchmark_weights = {
        'latency': 0.3,
        'throughput': 0.25,
        'accuracy': 0.35,
        'memory_usage': 0.05,
        'cache_hit_rate': 0.05
    }

    # Irrelevant preprocessing: convert to sets and perform unused operations
    metric_names = set(metric_set.keys())
    weight_keys = set(benchmark_weights.keys())
    common_keys = metric_names & weight_keys
    extra_analysis = {k: metric_set[k] ** 2 for k in metric_names if k not in weight_keys}

    # Unused list comprehension - red herring
    _ = [x.upper() for x in metric_set.keys() if 'e' in x]

    final_score = evaluate_performance(metric_set, benchmark_weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()