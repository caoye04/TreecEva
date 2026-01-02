import itertools

def main():
    # System initialization parameters (some are decoys)
    clock_rate = 2400
    buffer_size = 512
    sample_window = 128
    calibration_factor = 0.987
    noise_threshold = 0.045
    legacy_mode = False
    debug_override = False
    temporal_offset = 17
    gain_stages = [1.0, 1.2, 1.5, 1.8, 2.0]
    
    # Real-time signal acquisition (simulated)
    raw_samples = [
        0.12, 0.34, 0.28, 0.91, 0.15, 0.76, 0.63, 0.44,
        0.88, 0.21, 0.57, 0.39, 0.72, 0.66, 0.50, 0.83
    ]
    
    # Irrelevant preprocessing path (dead code due to legacy_mode=False)
    if legacy_mode:
        processed_legacy = []
        for x in raw_samples:
            processed_legacy.append((x * 2.1) % 1.0)
        normalized_data = processed_legacy
    else:
        # Active normalization using gain stages (only first three used)
        temp_normalized = [x * gain_stages[2] for x in raw_samples]  # uses 1.5x gain
        normalized_data = [min(x, 0.99) for x in temp_normalized]
    
    # Simulate frame segmentation using string-like operations on data labels
    frame_tags = ['F1', 'F2', 'F3', 'F4']
    frame_lookup = {tag: idx for idx, tag in enumerate(frame_tags)}
    active_frames = frame_tags[:3]
    
    # Distractor: complex but unused combinatorics on frame permutations
    frame_perms = list(itertools.permutations(active_frames))
    perm_scores = []
    for perm in frame_perms:
        score = 0
        for i, tag in enumerate(perm):
            score += (i + 1) * (frame_lookup[tag] + 1)
        perm_scores.append(score)
    
    # Unused statistical decoy variables
    avg_perm_score = sum(perm_scores) / len(perm_scores) if perm_scores else 0
    max_deviation = max(perm_scores) - min(perm_scores) if perm_scores else 0
    
    # Actual signal processing begins here — relevant logic
    filtered_samples = [x for x in normalized_data if x > noise_threshold]
    
    # Bucketing into quartiles using manual thresholds (not using external libs)
    quartile_breaks = [0.25, 0.50, 0.75, 1.00]
    bucket_counts = [0, 0, 0, 0]
    for val in filtered_samples:
        for q_idx, brk in enumerate(quartile_breaks):
            if val <= brk:
                bucket_counts[q_idx] += 1
                break
    
    # Secondary transformation: pair differences in sliding window
    diff_series = []
    for i in range(len(filtered_samples) - 1):
        diff_series.append(abs(filtered_samples[i+1] - filtered_samples[i]))
    
    # String-based encoding of state (using string methods as required)
    state_flags = []
    for d in diff_series:
        if d < 0.1:
            state_flags.append('S')  # stable
        elif d < 0.3:
            state_flags.append('M')  # moderate
        else:
            state_flags.append('V')  # volatile
    
    flag_string = ''.join(state_flags)
    volatility_pattern = flag_string.strip('S')  # remove leading/trailing S
    
    # Misleading complexity: entropy approximation (unused)
    unique_trigrams = set()
    for i in range(len(flag_string) - 2):
        trigram = flag_string[i:i+3]
        unique_trigrams.add(trigram)
    estimated_entropy = len(unique_trigrams) / 20.0  # arbitrary scaling
    
    # Core diagnostic logic — depends only on bucket distribution and pattern length
    def analyze_signal_quality(buffer):
        # Key formula: weighted sum from bucket counts
        weight_vector = [1, 2, 4, 8]
        shape_metric = sum(b * w for b, w in zip(bucket_counts, weight_vector))
        
        # Pattern complexity from string runs
        runs = 1
        for i in range(1, len(volatility_pattern)):
            if volatility_pattern[i] != volatility_pattern[i-1]:
                runs += 1
        
        # Final diagnostic: combination of shape and dynamics
        base_score = shape_metric * 3.7
        adjustment = runs * 1.25
        return int(base_score - adjustment)  # deterministic integer output

    # Simulate intermediate diagnostics (distraction)
    preliminary_diagnostics = []
    for i in range(3):
        probe = analyze_signal_quality([0.1, 0.2, 0.3])
        preliminary_diagnostics.append(probe)
    
    # UNUSED recursive red herring function
    def recursive_energy_estimate(level, factor):
        if level <= 1:
            return factor
        return factor + 0.5 * recursive_energy_estimate(level - 1, factor * 0.9)
    
    energy_proxy = recursive_energy_estimate(5, 1.0)  # Computed but not used
    
    # The actual call that produces the target variable
    diagnostic_buffer = filtered_samples.copy()
    final_diagnostic = analyze_signal_quality(diagnostic_buffer)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()