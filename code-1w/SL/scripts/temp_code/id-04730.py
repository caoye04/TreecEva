def analyze_performance(data_map):
    # Irrelevant preprocessing
    temp_stats = {k: v * 1.5 for k, v in data_map.items() if k in ['latency', 'memory']}
    
    # Distractor: complex but unused transformation
    derived_metrics = {}
    for key, val in data_map.items():
        if val > 10:
            derived_metrics[key + '_adj'] = (val ** 0.5) * 2.1
        else:
            derived_metrics[key + '_low'] = val / 0.7

    # Actual relevant computation begins
    base_scores = {}
    for k, v in data_map.items():
        if k == 'throughput':
            base_scores['throughput_norm'] = min(v / 100.0, 1.0)
        elif k == 'efficiency':
            base_scores['efficiency_mod'] = max(0, (v - 20) / 80)
    
    # Modular arithmetic used in meaningful way
    checksum = 0
    for val in data_map.values():
        checksum = (checksum + val * 3) % 97
    
    # Weighted aggregation setup (semi-relevant)
    weights = {
        'throughput_norm': 0.6,
        'efficiency_mod': 0.4
    }
    
    metrics = base_scores  # Point of interest
    
    def calculate_rating(met, wts):
        raw_total = 0.0
        weight_sum = 0.0
        for name, score in met.items():
            raw_total += score * wts[name]
            weight_sum += wts[name]
        return raw_total / weight_sum if weight_sum > 0 else 0.0

    final_score = calculate_rating(metrics, weights)
    
    # Dead code path (never executed)
    if False:
        fallback = sum(temp_stats.values()) / len(temp_stats)
        final_score = max(final_score, fallback)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    return final_score

# Input data
system_data = {
    'throughput': 85,
    'efficiency': 68,
    'latency': 15,
    'memory': 22
}

# Execute
analyze_performance(system_data)