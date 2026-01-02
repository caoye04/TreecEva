def analyze_filtration_process(raw_readings):
    base_threshold = 42
    adjustment_factor = 1.5
    temp_buffer = []
    weighted_values = []
    
    for reading in raw_readings:
        normalized = reading - base_threshold
        if normalized < 0:
            adjusted = abs(normalized) * adjustment_factor
        else:
            adjusted = normalized ** 0.5
        weighted_values.append(int(adjusted))
    
    # Simulate intermediate diagnostic trace (not used in final result)
    diagnostic_trace = [x % 7 for x in weighted_values if x > 5]
    trace_sum = sum(diagnostic_trace)
    average_diagnostic = trace_sum / len(diagnostic_trace) if diagnostic_trace else 0

    # Core logic: filter based on dynamic condition
    dynamic_limit = len(weighted_values) // 2 + 3
    masked_values = [v for v in weighted_values if v % 3 != 0]  # Distractor list
    
    # Actual filtration path
    valid_entries = []
    for idx, wv in enumerate(weighted_values):
        if idx % 2 == 0 and wv > 2:
            valid_entries.append(wv)
        elif wv > 5:
            valid_entries.append(wv + 1)

    # Key computation point
    filtered_weights = [fw for fw in valid_entries if fw < dynamic_limit]
    filtration_score = sum(filtered_weights)

    # Dead code branch - never executed due to logic above
    if len(raw_readings) > 1000:
        overflow_correction = max(filtration_score, 100)
        filtration_score -= overflow_correction

    print(f"Result: {filtration_score}")
    return filtration_score

# Input data
sensor_log = [45, 40, 55, 30, 60, 39, 70, 25]
analyze_filtration_process(sensor_log)