import itertools

def analyze_phase_shift(data_window, threshold=0.75):
    above_threshold = [x > threshold for x in data_window]
    cross_points = []
    for i in range(1, len(above_threshold)):
        if above_threshold[i] != above_threshold[i-1]:
            cross_points.append(i)
    
    # Distractor: unused computation
    cumulative_drift = sum(abs(a - b) for a, b in zip(data_window, data_window[1:]))
    normalized_drift = cumulative_drift / len(data_window) if data_window else 0
    
    return cross_points

def validate_stability(pattern_seq):
    runs = []
    current_run = 1
    for i in range(1, len(pattern_seq)):
        if pattern_seq[i] == pattern_seq[i-1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)
    
    # Semi-relevant: computes max_run but not used directly in final answer
    max_run = max(runs) if runs else 0
    avg_run = sum(runs) / len(runs) if runs else 0
    
    return avg_run > 1.2

def calculate_rating(flags, samples):
    base_weight = 0.37
    adjustment_factor = 0.08
    
    # Real logic begins
    valid_flags = [f for f in flags if f is not None]
    flag_sum = sum(int(f) for f in valid_flags)
    
    # Use slicing to get subset
    sample_subset = samples[::2]  # every other sample
    high_activity = len([s for s in sample_subset if s > 0.5])
    
    # Composite score calculation
    activity_score = high_activity * base_weight
    flag_score = flag_sum * adjustment_factor
    
    # Distractor variables
    temp_ratio = len(sample_subset) / len(samples) if samples else 0
    padding_offset = len(samples) % 4
    
    # Final score influenced only by activity_score and flag_score
    raw_score = activity_score + flag_score
    
    # Additional logic step: apply penalty if instability detected
    binary_flags = [bool(f) for f in valid_flags]
    if any(a and b for a, b in zip(binary_flags, binary_flags[1:])):
        raw_score -= 0.15
    
    return round(raw_score * 100)

# Main execution block
if __name__ == "__main__":
    signal_data = [0.81, 0.62, 0.93, 0.45, 0.78, 0.69, 0.31, 0.52]
    
    # Generate convergence flags using auxiliary analysis
    transitions = analyze_phase_shift(signal_data)
    convergence_flags = [False, True, None, True, False, None, True]
    
    # Simulate metric sampling with itertools
    shifted_pairs = list(itertools.pairwise(signal_data))
    metric_samples = [abs(a - b) for a, b in shifted_pairs]
    
    # Validate pattern stability (distractor call - not used in final path)
    pattern_cycle = [1, 1, 0, 1, 1, 1, 0]
    stability = validate_stability(pattern_cycle)
    
    # Key statement
    final_score = calculate_rating(convergence_flags, metric_samples)
    
    print(f"Result: {final_score}")