def analyze_sensor_data(raw_readings, calibration_offset=0.7):
    # Irrelevant preprocessing: normalize string labels (distractor)
    labels = ['sens_a', 'sens_b', 'sens_c', 'sens_d', 'sens_e']
    normalized_labels = [label.upper().replace('_', '-') for label in labels if 'b' not in label]
    offset_map = {i: calibration_offset * (i % 3) for i in range(5)}

    # Real data path: extract numeric sequences
    filtered_readings = [x for x in raw_readings if isinstance(x, int) and x > 0]
    processed = [x * 0.95 + calibration_offset for x in filtered_readings]

    # Bit manipulation decoy (unused but plausible)
    checksum = 0
    for val in raw_readings:
        if isinstance(val, int):
            checksum ^= (val << 2) & 0xFF
    checksum_valid = (checksum % 13 == 0)

    # Distractor: dead-end statistical analysis
    mean_val = sum(processed) / len(processed) if processed else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in processed) / len(processed) if processed else 0
    outlier_threshold = mean_val + 1.5 * variance_proxy ** 0.5
    outliers = [x for x in processed if x > outlier_threshold]  # Unused

    # Core logic disguised among distractions
    temperature_fluctuations = [processed[i+1] - processed[i] for i in range(len(processed)-1)]
    temperature_fluctuations.append(sum(temperature_fluctuations[:2]))  # Synthetic padding

    # Complex slicing and aggregation (key relevant step)
    rolling_window = [sum(processed[i:i+3]) for i in range(len(processed)-2)]
    scaled_window = [round(w * 0.33, 2) for w in rolling_window]
    aggregate_metrics = [scaled_window[0], scaled_window[-1], min(scaled_window), max(scaled_window), sum(scaled_window)/len(scaled_window)]

    # Decoy control flow with misleading early return
    if len(raw_readings) < 10:
        temp_correction = sum(temperature_fluctuations) // 2
        final_diagnostic = temp_correction * 2  # Dead assignment
    else:
        pass  # Simulated branching distraction

    # Critical statement embedded in noise
    final_diagnostic = aggregate_metrics[3] + temperature_fluctuations[-2]

    # Red herring: unused transformation chain
    inverted_path = processed[::-1]
    smoothed = [inverted_path[i] * 0.9 for i in range(len(inverted_path)) if i % 2 == 0]
    derived_score = sum(smoothed) / 100.0  # Completely irrelevant

    print(f"Result: {final_diagnostic}")

# Simulate sensor input with mixed types (realistic noise)
raw_input_stream = [105, 210, 'err', 195, 208, None, 215, 190, 200, 210, 'N/A', 220]
analyze_sensor_data(raw_input_stream)