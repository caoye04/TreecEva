def calculate_performance(results):
    base_weights = {'latency': 0.4, 'throughput': 0.35, 'memory': 0.25}
    scaling_factor = 1.5
    
    # Preprocess: normalize results around median
    all_values = sorted([v for r in results for v in r.values()])
    median_val = all_values[len(all_values) // 2]
    normalized = [{k: (v - median_val) * scaling_factor for k, v in r.items()} for r in results]
    
    # Misleading: temperature adjustment (not used in final score)
    temperature_offset = 0.18
    adjusted_latency = [n['latency'] + temperature_offset for n in normalized]
    avg_adjusted_latency = sum(adjusted_latency) / len(adjusted_latency)

    # Compute efficiency ratios (some distraction here)
    efficiency_ratios = []
    for n in normalized:
        if n['latency'] > 0:
            ratio = n['throughput'] / (n['latency'] + 0.1)
            efficiency_ratios.append(ratio)
    
    # Real computation begins: weighted sum per test
    weighted_scores = []
    for entry in normalized:
        score = 0
        for metric, weight in base_weights.items():
            score += entry[metric] * weight
        weighted_scores.append(score)
    
    # Aggregate with outlier suppression
    sorted_scores = sorted(weighted_scores)
    trimmed = sorted_scores[1:-1] if len(sorted_scores) > 2 else sorted_scores
    
    # Final aggregation
    raw_performance = sum(trimmed) / len(trimmed)
    
    # Distractor: hypothetical compression gain (unused)
    compression_gain = raw_performance * 0.07
    projected_gain = round(compression_gain, 3)
    
    # Actual final score calculation
    stability_penalty = len(results) * 0.01
    final_score = raw_performance - stability_penalty
    
    return final_score

# Simulated benchmark data from 5 test runs
test_run_1 = {'latency': 120, 'throughput': 85, 'memory': 60}
test_run_2 = {'latency': 110, 'throughput': 90, 'memory': 65}
test_run_3 = {'latency': 130, 'throughput': 80, 'memory': 58}
test_run_4 = {'latency': 115, 'throughput': 88, 'memory': 62}
test_run_5 = {'latency': 125, 'throughput': 82, 'memory': 64}

benchmark_results = [test_run_1, test_run_2, test_run_3, test_run_4, test_run_5]

# Key execution point
calibration_mode = False
if not calibration_mode:
    final_score = calculate_performance(benchmark_results)

print(f"Result: {final_score}")