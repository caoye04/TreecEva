def analyze_signal_integrity(raw_samples, threshold=0.75):
    sample_count = len(raw_samples)
    strong_signals = [s for s in raw_samples if s > threshold]
    weak_signals = [s for s in raw_samples if s <= threshold]
    
    # Distractor: Energy computation not used in final result
    total_energy = sum(s ** 2 for s in raw_samples)
    normalized_power = total_energy / sample_count if sample_count else 0
    
    # Real logic begins
    valid_segments = 0
    segment_size = 3
    for i in range(0, sample_count - segment_size + 1, segment_size):
        segment = raw_samples[i:i+segment_size]
        if all(s > 0.5 for s in segment):
            valid_segments += 1

    # Secondary path: noise classification (semi-relevant)
    noise_bursts = 0
    for i in range(1, len(weak_signals)):
        if weak_signals[i] < 0.3 and weak_signals[i-1] < 0.3:
            noise_bursts += 1

    baseline_reference = 10 * sample_count
    adjustment_magnitude = abs(len(strong_signals) - len(weak_signals))

    # Core scoring logic
    aggregate_score = 0
    if valid_segments > 0:
        aggregate_score = (len(strong_signals) * 2) + (valid_segments * 5)
    
    # Red herring: unused compensation chain
    temp_comp = 1.0
    for _ in range(3):
        temp_comp *= 0.9
    compensated_base = baseline_reference * temp_comp  # Not used

    # Conditional expression (Python feature)
    phase_flag = sample_count > 10 if len(strong_signals) > 2 else False
    
    # Bitwise distraction
    debug_signature = sample_count & 7
    checksum_probe = debug_signature ^ 5

    # Key assignment with conditional expression
    correction_factor = 7 if phase_flag else 3

    # Critical statement
    final_diagnostic = aggregate_score + (phase_flag and correction_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

# Input data
input_data = [0.8, 0.9, 0.6, 0.4, 0.2, 0.85, 0.78, 0.82, 0.35, 0.15, 0.91, 0.88]
analyze_signal_integrity(input_data)