def analyze_pattern(sequence):
    frequency = {}
    for item in sequence:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


def normalize_values(data_list):
    max_val = max(data_list)
    min_val = min(data_list)
    range_val = max_val - min_val or 1
    normalized = [(x - min_val) / range_val for x in data_list]
    # Irrelevant transformation
    offset_correction = sum(normalized) * 0.01
    return [x + offset_correction for x in normalized]


def calculate_performance(metrics):
    # Extract relevant time-series metrics
    raw_times = [entry['time'] for entry in metrics]
    
    # Distractor: process unrelated signal data
    signals = [entry['signal'] for entry in metrics if 'signal' in entry]
    signal_freq = analyze_pattern(signals)
    avg_power = sum(len(str(s)) for s in signals) / len(signals) if signals else 0

    # Normalize execution times
    norm_times = normalize_values(raw_times)
    
    # Compute efficiency score based on sorted performance
    sorted_indices = [i for i, _ in sorted(enumerate(norm_times), key=lambda x: x[1])]
    rank_boost = 0
    for idx, sorted_idx in enumerate(sorted_indices):
        if sorted_idx == idx:
            rank_boost += 0.1
    
    # Key logic: composite score with weighting
    base_score = sum(norm_times)
    penalty = 0
    for i in range(1, len(raw_times)):
        if raw_times[i] < raw_times[i-1]:
            penalty += 0.05
    
    # Distractor: unused branching
    if len(raw_times) > 10:
        temp_adjustment = base_score * 0.02
    else:
        temp_adjustment = 0  # Dead code path effect
    
    # Final computation
    stability_factor = (max(raw_times) - min(raw_times)) / len(raw_times) if raw_times else 0
    final_score = (base_score * 100) - (penalty * 1000) + rank_boost - (stability_factor * 10)
    
    # Additional red herring: string processing with no impact
    labels = ['metric_{}'.format(i) for i in range(len(metrics))]
    label_lengths = [len(lbl.replace('_', '')) for lbl in labels]
    char_sum = sum(label_lengths)
    
    return round(final_score, 4)

# Main execution
benchmark_data = [
    {'time': 120, 'signal': 'A'},
    {'time': 95, 'signal': 'B'},
    {'time': 110, 'signal': 'A'},
    {'time': 88, 'signal': 'C'},
    {'time': 92, 'signal': 'B'},
    {'time': 105, 'signal': 'A'}
]

# Execute target statement
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")