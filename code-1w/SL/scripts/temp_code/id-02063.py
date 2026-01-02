def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x * 0.98 for x in raw_samples if x > 1.0]
    processed = [min(max(x, 0.1), 1.0) for x in raw_samples]

    # Decoy statistical analysis (unused)
    mean_val = sum(processed) / len(processed) if processed else 0
    variance = sum((x - mean_val) ** 2 for x in processed) / len(processed) if processed else 0
    entropy_estimate = -sum(p * math.log(p) for p in processed if p > 0)  # Unused

    # Signal binarization with set operations
    high_signals = {i for i, x in enumerate(processed) if x >= threshold}
    low_signals = {i for i, x in enumerate(processed) if x < threshold}
    overlap_check = high_signals & low_signals  # Always empty, red herring

    # Real computation begins: pattern detection
    transitions = []
    for i in range(1, len(processed)):
        if processed[i-1] < threshold <= processed[i]:
            transitions.append(i)
        elif processed[i-1] >= threshold > processed[i]:
            transitions.append(-i)  # Negative indicates falling edge

    # Character counting in synthetic tag (distractor)
    device_tag = 'SIGMONITORv2'
    char_count = len([c for c in device_tag if c.isalpha()])  # 11, unused

    # Critical data transformation chain
    peak_magnitudes = [processed[i] for i in high_signals]
    sorted_peaks = sorted(peak_magnitudes, reverse=True)
    top_quartile = sorted_peaks[:max(1, len(sorted_peaks) // 4)]
    avg_top_peak = sum(top_quartile) / len(top_quartile) if top_quartile else 0

    # Diagnostic metric calculation (used)
    stability_index = len(transitions) / len(processed) if processed else 0
    noise_ratio = len([x for x in processed if x < 0.3]) / len(processed)
    signal_quality = (1 - noise_ratio) * (1 - stability_index)

    # Misleading complex bit manipulation (unused)
    status_flag = 0
    for i, val in enumerate(processed):
        if val > 0.5:
            status_flag ^= (1 << (i % 8))
    # End of decoy

    # Core logic hidden among distractions
    base_energy = sum(x**2 for x in peak_magnitudes)
    pulse_count = len([t for t in transitions if t > 0])
    symmetry_score = abs(sum(transitions)) / (pulse_count + 1)

    # Final diagnostic components
    aggregate_score = base_energy * (pulse_count + 1) / (symmetry_score + 1e-6)
    correction_factor = 0.87 if noise_ratio < 0.2 else 0.65
    offset_value = len(high_signals.intersection({x % 100 for x in range(200)}))  # evaluates to len(high_signals ∩ {0..99})

    # Key statement
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Output requirement
    print(f"Result: {final_diagnostic}")

# Setup input and execute
data_stream = [0.12, 0.81, 0.93, 0.21, 0.78, 0.85, 0.91, 0.05, 0.88, 0.79, 0.94, 0.11, 0.82, 0.87]
math = __import__('math')
analyze_signal_integrity(data_stream)