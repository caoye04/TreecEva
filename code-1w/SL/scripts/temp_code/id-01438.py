def analyze_signal_processing_chain():
    # Simulate a signal processing pipeline with phase adjustments and amplitude corrections
    frequencies = [50, 60, 100, 120, 400]
    phases = [15, -30, 90, 45, -180]
    amplitudes = [1.0, 0.8, 1.2, 0.5, 2.0]

    # Irrelevant baseline metrics (distractor)
    total_metrics = len(frequencies) + len(phases)
    scaling_factor = 1.0
    adjustment_log = []

    # Amplitude normalization (semi-relevant, but not used in final answer)
    normalized_amplitudes = [amp * scaling_factor for amp in amplitudes]
    avg_amplitude = sum(normalized_amplitudes) / len(normalized_amplitudes)

    # Track cumulative phase rotation across bands
    cumulative_rotation = 0
    phase_contributions = []

    # Process each frequency band with conditional phase updates
    for idx, (freq, phase) in enumerate(zip(frequencies, phases)):
        if freq < 100:
            adjusted_phase = phase * 1.5
        elif freq == 100:
            adjusted_phase = phase + 10
        else:
            adjusted_phase = phase * 0.8 if phase > 0 else phase * 1.1

        # Only positive phase contributions affect cumulative rotation
        if adjusted_phase > 0:
            cumulative_rotation += adjusted_phase
            phase_contributions.append((idx, adjusted_phase))

        # Log irrelevant intermediate state
        adjustment_log.append(f"Band {idx}: {freq}Hz, raw={phase}, adj={adjusted_phase:.1f}")

    # Apply modulo to get net phase within circle
    net_phase_shift = cumulative_rotation % 360

    # Dead code path - never executed under current logic
    if len(adjustment_log) > 100:
        net_phase_shift *= 2

    # Unused sorting of logs (distractor)
    sorted_logs = sorted(adjustment_log, key=lambda x: x.lower())

    # Output the target result
    print(f"Result: {net_phase_shift}")

    return net_phase_shift

analyze_signal_processing_chain()