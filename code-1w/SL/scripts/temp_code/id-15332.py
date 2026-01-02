def calculate_performance(data):
    # Preprocessing: extract relevant time samples
    time_slices = [entry['timestamp'] for entry in data if entry['active']]
    slice_deltas = [time_slices[i+1] - time_slices[i] for i in range(len(time_slices)-1)]
    
    # Irrelevant computation: track unused statistics
    avg_time = sum(time_slices) / len(time_slices)
    max_gap = max(slice_deltas) if slice_deltas else 0
    min_gap = min(slice_deltas) if slice_deltas else 0
    gap_variance = sum((d - (sum(slice_deltas)/len(slice_deltas)))**2 for d in slice_deltas) / len(slice_deltas) if slice_deltas else 0

    # Focus on sequence patterns in benchmark phases
    phase_sequence = [entry['phase'] for entry in data]
    unique_phases = list(dict.fromkeys(phase_sequence))  # Preserves order
    
    # Misleading structure: complex phase scoring (only first 3 matter)
    phase_weights = {p: idx + 1 for idx, p in enumerate(unique_phases)}
    total_weight = sum(phase_weights.values())
    
    # Actual logic: count transitions between active phases
    transition_count = 0
    for i in range(len(phase_sequence) - 1):
        if phase_sequence[i] != phase_sequence[i+1]:
            transition_count += 1

    # Distractor: unused normalization
    normalized_transitions = transition_count / len(data) if data else 0
    
    # Core metric: average delta weighted by transition frequency
    base_metric = sum(slice_deltas) / len(slice_deltas) if slice_deltas else 0
    adjustment_factor = transition_count % 7
    
    # Final score depends only on base_metric and adjustment_factor
    final_score = int(base_metric * adjustment_factor)
    
    return final_score

# Simulated benchmark log
timestamp_log = list(range(100, 200, 3))
benchmark_data = [
    {'timestamp': timestamp_log[i], 'active': i % 2 == 0, 'phase': ['init', 'run', 'pause', 'run', 'halt'][i % 5]} 
    for i in range(30)
]

# Dead code path: never used
unused_aggregate = sum(d['timestamp'] for d in benchmark_data if d['phase'] == 'unknown') if any(d['phase'] == 'unknown' for d in benchmark_data) else 0

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")