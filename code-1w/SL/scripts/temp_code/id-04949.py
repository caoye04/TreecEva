def analyze_pattern(seq_list, threshold_config):
    # Irrelevant transformation: reverses but not used in final logic
    reversed_seq = [seq[::-1] for seq in seq_list]
    
    # Distractor computation: calculates mean lengths but unused
    mean_length = sum(len(seq) for seq in seq_list) / len(seq_list) if seq_list else 0
    
    # Semi-relevant preprocessing: normalize thresholds
    normalized_thresholds = {k: v * 0.95 for k, v in threshold_config.items()}
    adjusted_high = normalized_thresholds['high'] + 0.1
    adjusted_low = normalized_thresholds['low'] - 0.1

    # Core logic: evaluate sequence stability using enumerate and zip
    stability_flags = []
    for i, seq in enumerate(seq_list):
        if len(seq) < 2:
            stability_flags.append(False)
            continue
        # Use of zip to compare consecutive elements
        diffs = [abs(b - a) for a, b in zip(seq, seq[1:])]
        # Apply threshold logic with logical operations
        stable = all(d <= adjusted_high for d in diffs) and any(d >= adjusted_low for d in diffs)
        stability_flags.append(stable)
    
    # Accumulate score based on stability and position
    raw_score = sum(i + 1 for i, flag in enumerate(stability_flags) if flag)
    
    # Red herring function: defined but not contributing to final answer
    def auxiliary_metric(data):
        return sum(sum(d) for d in data if len(d) > 1) % 100
    
    # Unused variable from irrelevant path
    backup_score = auxiliary_metric(seq_list) if len(seq_list) > 3 else 0
    
    # Final adjustment: scale raw score by number of valid thresholds
    scaling_factor = len([t for t in normalized_thresholds.values() if t > 0])
    return int(raw_score * scaling_factor)

# Wrapper function to simulate modular design
def calculate_equilibrium(sequences, thresholds):
    # Misleading pre-check that doesn't affect outcome
    if not sequences or not thresholds:
        return -1
    
    # Tuple unpacking for clarity (though one value is unused)
    config_keys, config_values = zip(*thresholds.items())
    unused_key_moment = sum(1 for k in config_keys if 'mid' in k)  # dead-end computation
    
    # Lambda for dynamic filtering (moderately relevant)
    filter_fn = lambda x: x > thresholds.get('low', 0)
    filtered_count = sum(1 for seq in sequences for val in seq if filter_fn(val))
    
    # Actual call with distraction
    base_result = analyze_pattern(sequences, thresholds)
    
    # Final interference: adjust by filtered count only if even
    adjustment = filtered_count if filtered_count % 2 == 0 else 0
    return base_result + adjustment

# Input setup
sequence_data = [
    [1.0, 1.8, 2.1],
    [3.0, 3.1, 3.2, 3.3],
    [5.0, 5.6, 5.4],
    [7.0, 7.05]
]

threshold_settings = {
    'low': 0.4,
    'high': 0.85,
    'mid_range': 0.6  # used only in dead-end
}

# Key execution point
equilibrium_score = calculate_equilibrium(sequence_data, threshold_settings)
print(f"Target result: {equilibrium_score}")