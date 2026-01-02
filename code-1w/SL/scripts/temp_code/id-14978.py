def analyze_sensor_array(raw_readings, calibration_offset):
    temporal_weights = [0.1, 0.2, 0.35, 0.15, 0.2]
    filtered_readings = []
    for i, reading in enumerate(raw_readings):
        adjusted = (reading + calibration_offset) * temporal_weights[i % len(temporal_weights)]
        if adjusted > 50:
            adjusted = 50 + (adjusted - 50) ** 0.5
        filtered_readings.append(round(adjusted, 3))

    # Irrelevant transformation path (dead logic)
    inverted_chain = [abs(x - 255) for x in raw_readings if x < 0]
    processed_inversions = list(map(lambda x: x * 1.5, inverted_chain))  # Unused

    # Signal convergence analysis
    moving_avg = []
    window_size = 3
    for i in range(len(filtered_readings) - window_size + 1):
        window = filtered_readings[i:i + window_size]
        moving_avg.append(sum(window) / window_size)

    trend_magnitude = 0.0
    for i in range(1, len(moving_avg)):
        trend_magnitude += abs(moving_avg[i] - moving_avg[i-1])

    # Simulated noise floor adjustment (distractor)
    noise_floor = 2.718
    decay_factor = 0.95
    for _ in range(50):
        noise_floor *= decay_factor
        if noise_floor < 0.1:
            break

    # Key signal convergence logic
    converged_signals = []
    for val in moving_avg:
        if val > 30 and val < 45:
            converged_signals.append(val * 1.15)
        elif val >= 45:
            converged_signals.append(val * 0.9)
        else:
            converged_signals.append(val)

    # System bias computation with string-based red herring
    status_labels = ['nominal', 'elevated', 'critical', 'recovered', 'stable']
    encoded_flags = []
    for label in status_labels:
        shifted = ''.join(chr((ord(c) - 97 + 3) % 26 + 97) for c in label)  # Caesar cipher +97 offset
        encoded_flags.append(shifted.upper())  # Result unused

    active_count = sum(1 for x in status_labels if len(x) > 7)  # Misleading count

    # Actual bias calculation
    base_bias = sum(converged_signals) / len(converged_signals) if converged_signals else 0
    peak_deviation = max(converged_signals) - min(converged_signals) if converged_signals else 0
    system_bias = (base_bias * 0.7) + (peak_deviation * 0.3)

    # Final aggregation with tuple unpacking (relevant)
    metrics_bundle = (system_bias, trend_magnitude, len(converged_signals))
    bias_component, _, length_factor = metrics_bundle

    def aggregate_metrics(signals, bias):
        total_power = sum(x ** 2 for x in signals)
        signal_entropy = 0
        for x in signals:
            if x > 0:
                signal_entropy -= (x / sum(signals)) * (x / sum(signals))
        diversity_index = signal_entropy + len(set(round(x, 1) for x in signals))
        return int((total_power * 0.4) + (bias * 0.3) + (diversity_index * 10) + (length_factor * 2))

    final_diagnostic = aggregate_metrics(converged_signals, system_bias)
    
    # Dead code branches (distractors)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
    elif final_diagnostic > 1000:
        final_diagnostic = 999  # Never reached

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
sensor_input = [89, 72, 94, 68, 77]
calib_offset = -12

result = analyze_sensor_array(sensor_input, calib_offset)