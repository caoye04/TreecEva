def calculate_performance(baseline, stress_tests):
    # Compute intersection of keys as common metrics
    common_metrics = set(baseline.keys()) & set(stress_tests.keys())
    
    # Calculate average deviation for common metrics
    deviations = []
    for metric in common_metrics:
        baseline_val = baseline[metric]
        stress_val = stress_tests[metric]
        if baseline_val != 0:
            deviation = abs(stress_val - baseline_val) / baseline_val
            deviations.append(deviation)
    
    avg_deviation = sum(deviations) / len(deviations) if deviations else 0
    max_deviation = max(deviations) if deviations else 0
    
    # Performance score based on inverse of average deviation (higher is better)
    stability_bonus = 100 * (1 - min(max_deviation, 1))
    raw_score = 1000 * (1 / (1 + avg_deviation))
    final_score = raw_score + stability_bonus
    
    return final_score

# Baseline system performance metrics
baseline_metrics = {
    'latency_ms': 120,
    'throughput_rps': 250,
    'error_rate': 0.02,
    'memory_mb': 450
}

# Stress test results under heavy load
stress_test_results = {
    'latency_ms': 180,
    'throughput_rps': 210,
    'error_rate': 0.035,
    'disk_io_iops': 1200  # Not in baseline
}

# Irrelevant auxiliary variable (minimal distraction)
ignored_diagnostic = {'cpu_peak': 95.6}

final_score = calculate_performance(baseline_metrics, stress_test_results)
print(f"Target result: {final_score}")