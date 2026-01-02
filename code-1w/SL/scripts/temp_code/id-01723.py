def process_metrics(log, thresh):
    total_entries = len(log)
    valid_count = 0
    temp_sum = 0.0
    outlier_count = 0
    efficiency_score = 0
    running_stats = {}

    # Initialize running stats with default values
    for key in ['latency', 'throughput', 'errors']:
        running_stats[key] = []

    # Simulate data filtering and processing
    for entry in log:
        latency = entry.get('latency')
        throughput = entry.get('throughput')
        error_flag = entry.get('error')

        if latency is None or throughput is None:
            continue

        adjusted_latency = latency * 0.95
        normalized_throughput = throughput / (latency + 1e-5)

        # Irrelevant transformation
        squared_metric = (adjusted_latency ** 2) + (normalized_throughput ** 2)

        if adjusted_latency > thresh:
            outlier_count += 1
            continue

        if not error_flag:
            valid_count += 1
            temp_sum += normalized_throughput
            running_stats['latency'].append(adjusted_latency)
            running_stats['throughput'].append(normalized_throughput)

        # Dead code branch - never executed due to logic above
        if error_flag and False:
            backup_value = throughput * 0.1
            running_stats['errors'].append(backup_value)

    # Compute efficiency score based on valid, non-outlier entries
    if valid_count > 0:
        average_normalized = temp_sum / valid_count
        penalty_factor = 1 - (outlier_count / total_entries)
        efficiency_score = average_normalized * penalty_factor * 100

    # Distractor computation
    phantom_score = 0
    for i in range(3):
        for j in range(3):
            phantom_score += (i * j - 2) ** 2  # No impact on final result

    # Final aggregation
    final_output = efficiency_score + 0.0  # Redundant addition

    return int(final_output)

# Generate synthetic data log
data_log = [
    {'latency': 120, 'throughput': 850, 'error': False},
    {'latency': 95, 'throughput': 900, 'error': True},
    {'latency': 150, 'throughput': 700, 'error': False},
    {'latency': 80, 'throughput': 950, 'error': False},
    {'latency': 200, 'throughput': 600, 'error': False},
    {'latency': 110, 'throughput': 880, 'error': False}
]

threshold = 140
result_var = process_metrics(data_log, threshold)
print(f"Result: {result_var}")