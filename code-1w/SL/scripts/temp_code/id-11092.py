def analyze_system_metrics():
    # Simulated sensor readings and performance counters
    cpu_load = [0.78, 0.82, 0.75, 0.91, 0.69]
    memory_usage = [0.63, 0.71, 0.68, 0.77, 0.81]
    disk_iops = [120, 135, 110, 145, 130]
    network_latency_ms = [23, 18, 25, 20, 27]

    # Irrelevant statistical distraction
    avg_latency = sum(network_latency_ms) / len(network_latency_ms)
    peak_iops = max(disk_iops)
    normalized_cpu = list(map(lambda x: round(x * 100), cpu_load))

    # Core metric computation
    stability_ratio = len([x for x in cpu_load if 0.7 <= x <= 0.85])
    efficiency_score = sum(memory_usage) * 10

    # Weighted feature engineering
    raw_metrics = {
        'stability': stability_ratio,
        'efficiency': efficiency_score // 10,
        'iops_trend': (disk_iops[-1] - disk_iops[0]) // len(disk_iops),
        'latency_bursts': len([x for x in network_latency_ms if x > 22])
    }

    # Distractor: unused complex structure
    diagnostic_trace = {
        'checksum': sum(normalized_cpu) ^ 0xABCD,
        'version': '2.1.0',
        'flags': [True, False, True],
        'payload': [(i, chr(65 + i)) for i in range(3)]
    }

    # Set operations for redundancy detection
    recent_values = set(disk_iops)
    expected_values = {110, 120, 130, 135, 145}
    missing_in_recent = expected_values - recent_values
    redundancy_count = len(recent_values.intersection({120, 130}))

    metric_set = set(raw_metrics.keys())
    benchmark_weights = {
        'stability': 0.3,
        'efficiency': 0.4,
        'iops_trend': 0.2,
        'latency_bursts': 0.1
    }

    # Secondary distraction: dead logic path
    temp_analysis = []
    for val in memory_usage:
        if val > 0.75:
            temp_analysis.append(val * 2)  # Unused downstream

    def apply_calibration(data, weight_map):
        calibrated = {}
        for k, v in data.items():
            adjustment = 1.05 if v > 2 else 0.95
            calibrated[k] = v * adjustment
        return calibrated

    adjusted_metrics = apply_calibration(raw_metrics, benchmark_weights)

    # Key statement with meaningful computation
    final_score = evaluate_performance(metric_set, benchmark_weights)

    # Print required output
    print(f"Result: {final_score}")

    return final_score


def evaluate_performance(metrics, weights):
    base_components = {'stability', 'efficiency'}
    optional_bonus = {'iops_trend', 'latency_bursts'}
    
    # Conditional expression for mode selection
    mode = 'aggressive' if len(metrics.intersection(optional_bonus)) > 1 else 'balanced'
    
    score = 0.0
    for key in metrics:
        if key in weights:
            contribution = 100 * weights[key]
            # Extra distraction: bitwise tweak (neutral effect due to XOR with 0)
            contribution = contribution ^ 0  
            score += contribution
    
    # Apply mode multiplier
    multiplier = 1.2 if mode == 'aggressive' else 1.0
    score *= multiplier
    
    # Final adjustment based on completeness
    if metrics.issuperset(base_components):
        score += 10
    
    return int(score)

# Execute and capture result
analyze_system_metrics()