def analyze_sensor_data(raw_readings, calibration_offset):
    # Irrelevant pre-processing block (dead code path)
    temp_buffer = [x * 0.98 for x in raw_readings if x > 50]
    outlier_count = 0
    for val in temp_buffer:
        if val > 100:
            outlier_count += 1
            break

    # Actual signal processing begins
    filtered_signal = [x + calibration_offset for x in raw_readings]
    window_size = 3
    moving_averages = []

    for i in range(len(filtered_signal) - window_size + 1):
        window = filtered_signal[i:i + window_size]
        avg = sum(window) / window_size
        moving_averages.append(round(avg, 2))

    # Distractor: unused transformation
    inverted_phase = [1.0 / (x + 1e-5) for x in moving_averages]
    normalized_power = [x ** 2 for x in inverted_phase]  # Unused

    # Key data structures
    metrics_catalog = {
        'baseline': sum(moving_averages[:4]),
        'trend': moving_averages[-1] - moving_averages[0],
        'stability': moving_averages.count(min(moving_averages)),
        'peak_response': max(moving_averages),
        'settling_time': len([x for x in moving_averages if abs(x - moving_averages[-1]) < 0.5])
    }

    # Decoy dictionary with similar names
    decoy_catalog = {k + '_alt': v * 0.1 for k, v in metrics_catalog.items()}
    shadow_copy = dict(metrics_catalog)  # Red herring

    operation_sequence = ['baseline', 'trend', 'settling_time', 'peak_response']
    execution_flags = [True, False, True, True]
    active_phases = [op for op, flag in zip(operation_sequence, execution_flags) if flag]

    # Bit manipulation decoy
    bit_fiddle = 0
    for op in operation_sequence:
        bit_fiddle ^= len(op) << 2
    masked_result = bit_fiddle & 0xFFFF  # Not used later

    # Real computation path
    aggregate_metrics = {}
    for key, value in metrics_catalog.items():
        if key in operation_sequence:
            aggregate_metrics[key] = int(abs(value)) * (3 if 'response' in key else 2)

    # Slicing distraction
    recent_metrics = moving_averages[::2]  # Every second element
    historical_trend = recent_metrics[::-1]  # Reverse order, unused

    # Conditional correction factor
    base_correction = 0
    if aggregate_metrics['baseline'] > 50:
        base_correction += 7
    if aggregate_metrics['trend'] < 0:
        base_correction -= 3
    else:
        base_correction += 4

    anomaly_detector = set()
    for i, val in enumerate(moving_averages):
        if val > 15 and i % 2 == 0:
            anomaly_detector.add(i)
    severity_score = len(anomaly_detector) * 5  # Unused distractor

    # Critical assignment
    correction_factor = base_correction * len(active_phases)
    final_diagnostic = aggregate_metrics[operation_sequence[-1]] + correction_factor

    # Unrelated logging block (dead code)
    debug_log = []
    for k, v in decoy_catalog.items():
        if 'alt' in k:
            debug_log.append(f'{k}:{v:.3f}')

    return final_diagnostic

# Simulated sensor input
sensor_input = [45, 52, 60, 63, 58, 55, 50, 48]
calibration_shift = 2.5

result = analyze_sensor_data(sensor_input, calibration_shift)
print(f'Result: {result}')