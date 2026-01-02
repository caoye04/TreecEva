def analyze_sensor_data(raw_readings):
    processed = []
    temp_offset = 0.0
    cumulative_noise = 0
    
    for idx, val in enumerate(raw_readings):
        if idx % 3 == 0:
            adjusted = val * 1.05
        elif idx % 5 == 0:
            adjusted = val * 0.98
        else:
            adjusted = val + (idx % 7)
            
        if idx > 0 and abs(adjusted - processed[-1]) > 10:
            adjusted = (adjusted + processed[-1]) / 2
            
        processed.append(round(adjusted, 3))

    # Irrelevant transformation - dead path
    transformed = [x * x for x in raw_readings if x < 0]
    shadow_value = sum(transformed) if transformed else 0

    # Decoy analysis with misleading intermediate
    peak_magnitude = max(processed) * min(processed)
    decoy_metric = (peak_magnitude ** 2) / 100

    # Actual signal extraction
    valid_range = [v for v in processed if 40 < v < 90]
    if len(valid_range) < 3:
        fallback_correction = sum(valid_range)
    else:
        fallback_correction = sum(v for i, v in enumerate(valid_range) if i % 2 == 1)

    # Destructuring with red herring
    *trends, _, last_trend = processed
    
    # Real accumulation chain
    moving_avg = []
    window_size = 3
    for i in range(len(valid_range) - window_size + 1):
        window_avg = sum(valid_range[i:i+window_size]) / window_size
        moving_avg.append(round(window_avg, 3))

    baseline_shift = len([x for x in processed if x > 70]) * 0.25
    adjustment_curve = [round(baseline_shift * (1.1 ** i), 3) for i in range(5)]

    # Core calculation buried in noise
    aggregate_metrics = []
    for i, avg in enumerate(moving_avg):
        metric = avg + (fallback_correction / 100) + adjustment_curve[i % 5]
        aggregate_metrics.append(round(metric, 3))

    # Dummy logic to mislead
    outlier_buffer = []
    for x in processed:
        if x > decoy_metric:  # decoy_metric is tiny
            outlier_buffer.append(x)

    # Final correction factor derived from subtle pattern
    indices_with_jump = [i for i in range(1, len(processed)) if processed[i] - processed[i-1] > 5]
    correction_factor = len(indices_with_jump) * 1.75

    # Key assignment
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Unused but plausible-looking diagnostics
    auxiliary_score = sum(outlier_buffer) / (len(outlier_buffer) or 1) if outlier_buffer else 0
    entropy_estimate = len(trends) * baseline_shift

    print(f"Result: {final_diagnostic}")

# Input data with realistic structure
sensor_input = [85.2, 42.1, 67.3, 91.0, 44.8, 70.4, 58.9, 88.2, 46.7, 73.1, 60.2]
analyze_sensor_data(sensor_input)