def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    temp_data = [x ** 0.5 for x in metrics['raw_values'] if x > 0]
    temp_data = [x for x in temp_data if x < 100]

    # Semi-relevant preprocessing
    normalized = list(map(lambda x: round(x / max(metrics['raw_values']), 3), metrics['raw_values']))

    # Key logic begins
    high_perf_count = 0
    met_targets = 0
    bonus_factor = 1.0

    category_weights = {
        'latency': 0.4,
        'throughput': 0.35,
        'reliability': 0.25
    }

    # Misleading weight adjustment (not actually used)
    adjusted_weights = {k: v * 0.9 for k, v in category_weights.items()}
    adjusted_weights['reliability'] += 0.05  # Dead computation

    # Actual scoring logic
    for key in ['latency', 'throughput', 'reliability']:
        idx = ['latency', 'throughput', 'reliability'].index(key)
        score = normalized[idx] * 100
        
        if score >= thresholds[key]:
            met_targets += 1
            if score > thresholds[key] + 10:
                high_perf_count += 1

    # Distractor: unused function definition
    def calculate_efficiency(x, y):
        return (x * y) % 7

    baseline_reference = sum([thresholds[k] for k in thresholds]) / 3
    fluctuation_check = abs(normalized[0] - normalized[-1]) > 0.5

    if met_targets >= 2:
        base_score = 85
        if high_perf_count >= 2:
            bonus_factor = 1.2
    else:
        base_score = 60
        bonus_factor = 0.9

    # Final calculation
    final_score = base_score * bonus_factor

    # Additional red herring variables
    projected_growth = (final_score * 1.1) % 90
    stability_ratio = (high_perf_count + 1) / (met_targets + 1)

    return int(round(final_score))

# Main execution context
raw_metrics = {
    'raw_values': [450, 780, 920],  # latency(ms), throughput(req/s), reliability(%)
    'units': ['ms', 'req/s', '%']
}

threshold_map = {
    'latency': 70.0,
    'throughput': 75.0,
    'reliability': 80.0
}

intermediate_calc = [x / 10 for x in raw_metrics['raw_values'] if x > 100]
dummy_filter = list(filter(lambda x: x < 50, intermediate_calc))

final_score = evaluate_performance(raw_metrics, threshold_map)
print(f"Result: {final_score}")