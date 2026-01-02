def analyze_sensor_data(raw_readings, thresholds):
    normalized = [x * 0.01 for x in raw_readings if x > 10]
    filtered = []
    temp_accumulator = 0
    
    # Irrelevant pre-processing (distractor)
    baseline_shift = sum([x for x in raw_readings if x < 5])
    offset_marker = len(raw_readings) % 7
    
    for i, val in enumerate(normalized):
        if i % 3 == 0:
            temp_accumulator += val
        if val > thresholds.get('critical', 2.5):
            filtered.append(val * 1.1)
        elif val > thresholds.get('warning', 1.0):
            filtered.append(val * 0.9)
    
    # Dead code path (misleading)
    redundant_calc = 0
    for x in filtered:
        redundant_calc += x ** 0.5
        if redundant_calc > 100:
            break
    else:
        redundant_calc = -1

    # Core logic buried in distractions
    aggregate_metrics = []
    for a, b in zip(filtered[::2], filtered[1::2]):
        score = (a + b) / 2
        adjustment = abs(a - b) * 0.2
        aggregate_metrics.append(score - adjustment)
    
    if len(aggregate_metrics) < 3:
        fill_value = thresholds.get('default_fill', 0.75)
        while len(aggregate_metrics) < 3:
            aggregate_metrics.append(fill_value)
            fill_value *= 0.9
    
    # More red herrings
    outlier_count = 0
    for x in raw_readings:
        if x > 1000:
            outlier_count += 1
    metadata_flag = outlier_count > 2
    
    # Unused transformation chain
    transformed = [x for x in normalized]
    for _ in range(2):
        transformed = [x ** 1.05 for x in transformed]

    # Critical execution point
    correction_factor = len([x for x in raw_readings if x % 2 == 1]) * 0.05
    final_diagnostic = aggregate_metrics[-1] + correction_factor
    
    # Print required result
    print(f"Result: {final_diagnostic}")

# Simulate input data
data_stream = [150, 23, 8, 45, 67, 1200, 34, 56, 78, 90, 1001]
config = {
    'critical': 2.2,
    'warning': 0.8,
    'default_fill': 0.82
}
analyze_sensor_data(data_stream, config)