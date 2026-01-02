def evaluate_performance(metrics, data):
    # Initialize various tracking variables
    base_points = 0
    bonus_tally = 0
    penalty_counter = 0
    temp_accumulator = 0  # Used in intermediate calc, not in final result

    # Distractor: Preprocess unrelated signal values
    signal_buffer = [x % 7 for x in data['readings']]
    filtered_signals = [s for s in signal_buffer if s > 3]
    signal_peak = max(filtered_signals) if filtered_signals else 0

    # Real logic begins: analyze metric compliance
    required_metrics = {'latency', 'throughput', 'jitter', 'reliability'}
    optional_metrics = {'power_efficiency', 'thermal_output', 'noise_ratio'}
    present_metrics = set(metrics)

    # Core scoring based on set operations
    mandatory_met = required_metrics.intersection(present_metrics)
    optional_met = optional_metrics.intersection(present_metrics)
    missing_mandatory = required_metrics - mandatory_met

    # Base points for mandatory metrics
    for _ in mandatory_met:
        base_points += 17

    # Bonus for optional ones
    for _ in optional_met:
        bonus_tally += 9

    # Penalty for each missing mandatory metric
    for _ in missing_mandatory:
        penalty_counter += 5

    # Secondary distraction: simulate thermal adjustment (unused)
    thermal_adj = 0
    if 'thermal_output' in present_metrics:
        for i in range(len(data['temperatures'])):
            if data['temperatures'][i] > 75:
                thermal_adj -= 1.5
    # End of irrelevant section

    # Use of bitwise to obfuscate relevance
    encoded_flag = 0
    for val in data['checksums']:
        encoded_flag ^= val  # XOR all checksums

    # Another red herring: sort and process unused list
    sorted_power = sorted([p * 0.95 for p in data['power_levels']], reverse=True)
    if len(sorted_power) > 3:
        avg_top_three = sum(sorted_power[:3]) / 3
        temp_accumulator += int(avg_top_three // 10)

    # Final score calculation — only base_points, bonus_tally, penalty_counter matter
    final_score = base_points + bonus_tally - penalty_counter

    # Print result as required
    return final_score

# Input data
benchmark_data = {
    'readings': [23, 45, 67, 89, 12, 34],
    'temperatures': [68, 76, 82, 71],
    'checksums': [10, 20, 30, 40],
    'power_levels': [120, 150, 130, 140, 110]
}

metric_set = ['latency', 'throughput', 'jitter', 'reliability', 'power_efficiency']

# Execute and print
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")