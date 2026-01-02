def analyze_signal(samples, threshold=100):
    raw_energy = sum(x ** 2 for x in samples)
    normalized_power = raw_energy / len(samples) if samples else 0

    # Irrelevant signal quality metrics (distraction)
    peak_amplitude = max(samples, default=0)
    noise_floor = min(samples, default=0)
    waveform_complexity = len(set(samples))

    # Distractor: unused function
    def estimate_bandwidth(s): return len(s) // 2

    # Key processing path begins
    significant_components = [x for x in samples if abs(x) > threshold]
    saturation_count = sum(1 for x in significant_components if x > 150)

    # Decoy transformation
    dummy_transform = [x ^ 255 for x in samples[:10]] if len(samples) > 5 else []
    magic_offset = len(dummy_transform) * 0.01

    # Conditional expression with red herring
    mode_flag = 'high' if len(significant_components) > 5 else 'low'
    scaling_factor = 0.8 if mode_flag == 'low' else 1.2

    # Bit manipulation decoy
    bit_analysis = 0
    for x in samples[:3]:
        bit_analysis ^= (x & 170)  # Only uses even bits, irrelevant

    # Core logic disguised among distractions
    clipped_values = [min(max(x, -128), 127) for x in samples]
    average_clipped = sum(clipped_values) / len(clipped_values)
    deviation_score = sum(abs(x - average_clipped) for x in clipped_values)

    # Another distraction: set operations with no impact
    unique_positives = set(x for x in samples if x > 0)
    unique_negatives = set(-x for x in samples if x < 0)
    symmetry_index = len(unique_positives & unique_negatives)

    # Critical intermediate values
    aggregate_measure = deviation_score / (1 + symmetry_index)
    
    # Logical operation chain with short-circuit red herring
    has_spike = any(x > 200 for x in samples)
    is_stable = len(samples) > 0 and all(x < 180 for x in samples)
    correction_factor = 0.1 if has_spike or not is_stable else 0.05

    # Dead code path
    if False:
        backup_estimator = sum(x * 0.9 for x in samples)
        aggregate_measure += backup_estimator * 0.01

    # KEY STATEMENT
    final_diagnostic = aggregate_measure * (1 + correction_factor)
    
    # Unrelated logging
    debug_log = f'Diagnostic: {final_diagnostic:.2f}'
    metadata_tags = ['signal', 'v2'] if scaling_factor > 1 else ['legacy']

    # Output requirement
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data with meaningful structure
input_samples = [50, -30, 120, 160, 45, -70, 110, 190, 65, 85, -40, 130, 170, 95]
analyze_signal(input_samples)