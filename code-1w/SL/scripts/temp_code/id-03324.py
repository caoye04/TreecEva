def evaluate_performance(log, baseline):
    # Irrelevant transformation: frequency map (distractor)
    freq_map = {}
    for entry in log:
        key = entry['metric']
        freq_map[key] = freq_map.get(key, 0) + 1

    # Misleading aggregation path (dead code path)
    temp_aggregate = 0
    for val in freq_map.values():
        temp_aggregate += val * 1.5

    # Real logic begins: filter valid results above threshold
    valid_entries = [e for e in log if e['result'] > baseline['threshold']]

    # Decoy statistical calculation (irrelevant)
    mean_deviation = sum(abs(e['result'] - baseline['mean']) for e in log) / len(log)
    adjusted_baseline = baseline['mean'] + (mean_deviation * 0.2)

    # Bit manipulation red herring
    magic_flag = 0b101010
    if len(valid_entries) & 1:
        magic_flag ^= 0b1111

    # Conditional expression with distractor branches
    scaling_factor = 1.75 if len(valid_entries) > 4 else (1.25 if adjusted_baseline < 85 else 1.0)

    # Set-based filtering: relevant concept (core logic)
    target_categories = {'throughput', 'latency', 'accuracy'}
    covered = {entry['metric'] for entry in valid_entries}  
    coverage_bonus = 10 if target_categories.issubset(covered) else 0

    # Primary score computation (hidden among noise)
    base_score = sum(entry['result'] for entry in valid_entries)
    penalty = 0
    for entry in valid_entries:
        if entry['result'] < baseline['penalty_line']:
            penalty += 5

    # Secondary distraction: unused recursive helper
    def calculate_depth(data, depth=0):
        return depth if not data else calculate_depth(data[1:], depth + 1)

    # Tertiary distraction: unused data structure transformation
    inverted_index = {e['result']: e['metric'] for e in log}
    sorted_inverted = sorted(inverted_index.items(), reverse=True)

    # Final conditional expression combining core elements
    final_score = base_score - penalty + coverage_bonus if base_score > 0 else -1
    return final_score

# Benchmark configuration (real parameter)
benchmark = {
    'threshold': 70,
    'mean': 75,
    'penalty_line': 60
}

# Assessment log with mixed metrics and results (input data)
assessment_log = [
    {'metric': 'accuracy', 'result': 88},
    {'metric': 'throughput', 'result': 92},
    {'metric': 'latency', 'result': 76},
    {'metric': 'accuracy', 'result': 67},  # Below threshold
    {'metric': 'throughput', 'result': 94},
    {'metric': 'energy', 'result': 50},     # Below threshold, irrelevant metric
    {'metric': 'latency', 'result': 81},
    {'metric': 'accuracy', 'result': 90}
]

# Execution point of interest
final_score = evaluate_performance(assessment_log, benchmark)
print(f"Result: {final_score}")