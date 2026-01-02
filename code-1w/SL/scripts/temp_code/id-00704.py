def process_signal_stream(raw_samples, threshold=0.75):
    # Simulate preprocessing of sensor data
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]

    # Irrelevant transformation: frequency domain mock (dead logic)
    dummy_fft = [abs(n) ** 2 for n in normalized][:len(normalized)//2]
    spectral_entropy = 0.0
    for val in dummy_fft:
        if val > 0.5:
            spectral_entropy += val * 0.3

    # Real path: detect pulses above threshold
    pulse_indices = []
    for i, val in enumerate(normalized):
        if val > threshold:
            pulse_indices.append(i)

    # Distractor: unused sliding window stats
    window_size = 3
    rolling_averages = []
    for i in range(len(normalized) - window_size + 1):
        window = normalized[i:i+window_size]
        rolling_averages.append(sum(window) / window_size)

    # Key signal feature: inter-pulse intervals
    intervals = []
    for i in range(1, len(pulse_indices)):
        intervals.append(pulse_indices[i] - pulse_indices[i-1])

    # Inject red herring: character counting in debug mode (never used)
    debug_tag = "pulse_analysis_v2"
    char_count = sum(1 for c in debug_tag if c in 'aeiou')

    # Generate timing log with slice offsets
    timing_log = [interval * 1.5 for interval in intervals if interval > 1]

    # Set flags based on pattern
    analysis_flags = []
    for t in timing_log:
        if t > 3.0:
            analysis_flags.append(2)
        elif t > 1.5:
            analysis_flags.append(1)
        else:
            analysis_flags.append(0)
    
    return timing_log, analysis_flags


def aggregate_metrics(log, flags):
    # Use zip to pair values and compute weighted diagnostic
    total_score = 0.0
    for val, flag in zip(log, flags):
        if flag == 2:
            total_score += val * 2.1
        elif flag == 1:
            total_score += val * 1.3
    
    # Decoy summation with no effect
    phantom_sum = sum(log) * 0.1
    
    # Final diagnostic score
    final_diagnostic = round(total_score, 4)
    
    # Dead code branch: never reached due to prior logic
    if len(log) < 0:  # Impossible condition
        final_diagnostic *= 0.5
        
    return final_diagnostic

# Simulated sensor input (deterministic)
raw_input = [0.05, 0.88, 0.12, 0.95, 0.67, 0.08, 0.93, 0.25, 0.82, 0.11, 0.91]

# Execute main processing chain
timing_data, detection_flags = process_signal_stream(raw_input, threshold=0.75)
final_diagnostic = aggregate_metrics(timing_log=timing_data, analysis_flags=detection_flags)

# Output result as required
print(f"Result: {final_diagnostic}")