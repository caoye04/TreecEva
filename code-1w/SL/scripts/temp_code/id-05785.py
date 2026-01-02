def analyze_sensor_data(raw_readings, threshold=100):
    # Irrelevant preprocessing: normalize data (not used in final path)
    normalized = [x / max(raw_readings) * 100 for x in raw_readings]
    filtered = [x for x in raw_readings if x > threshold]

    # Distractor: complex frequency analysis (dead end)
    frequency_map = {}
    for val in raw_readings:
        frequency_map[val] = frequency_map.get(val, 0) + 1
    dominant_frequency = max(frequency_map, key=frequency_map.get)

    # Real computation begins: segment and transform
    segments = [raw_readings[i:i+3] for i in range(0, len(raw_readings), 3)]
    processed_segments = []
    for seg in segments:
        if len(seg) == 3:
            # Compute weighted transformation
            transformed = seg[0] * 0.2 + seg[1] * 0.3 + seg[2] * 0.5
            processed_segments.append(round(transformed))

    # Misleading statistical summary (unused)
    mean_val = sum(processed_segments) / len(processed_segments) if processed_segments else 0
    outlier_count = sum(1 for x in processed_segments if x > mean_val * 1.5)

    # Critical path: trend analysis using slicing and zip
    trends = []
    for curr, next_val in zip(processed_segments, processed_segments[1:]):
        trends.append(1 if next_val >= curr else -1)

    # Another distractor: symmetry check (never used)
    reversed_trends = trends[::-1]
    is_symmetric = trends[:len(trends)//2] == reversed_trends[:len(trends)//2]

    # Generate diagnostic levels using enumerate and conditional logic
    diagnostic_levels = []
    for i, trend in enumerate(trends):
        if i % 3 == 0:
            diagnostic_levels.append(trend * 10)
        elif i % 2 == 0:
            diagnostic_levels.append(trend * 5)
        else:
            diagnostic_levels.append(0)

    # Decoy aggregation (looks important but unused)
    cumulative_risk = sum(abs(x) for x in diagnostic_levels if x < 0)

    # Actual signal extraction
    valid_diagnostics = [x for x in diagnostic_levels if x != 0]
    if not valid_diagnostics:
        valid_diagnostics = [42]  # fallback

    # Apply artificial correction based on length parity
    offset_key = len(valid_diagnostics) % 4
    corrections = {0: -3, 1: 5, 2: -7, 3: 9}
    correction_factor = corrections[offset_key]

    # Final metric construction with slicing
    rolling_averages = []
    for i in range(len(valid_diagnostics) - 1):
        window_avg = (valid_diagnostics[i] + valid_diagnostics[i+1]) / 2
        rolling_averages.append(int(window_avg))

    aggregate_metrics = rolling_averages[::2] if len(rolling_averages) > 5 else rolling_averages[1::2]
    
    # Key statement
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Unused but plausible-looking telemetry
    telemetry_summary = {"stability": sum(trends), "anomalies": outlier_count, "peak": dominant_frequency}

    return final_diagnostic

# Input data
sensor_input = [120, 85, 95, 110, 90, 130, 105, 115, 80, 140, 125]
analyze_sensor_data(sensor_input)