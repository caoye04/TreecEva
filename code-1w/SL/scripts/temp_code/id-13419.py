def analyze_sensor_data(raw_readings, threshold, safety_margin):
    # Normalize readings using baseline offset
    baseline = 10.0
    normalized = [x - baseline for x in raw_readings]

    # Apply dynamic noise filter based on moving average
    smoothed = []
    for i in range(1, len(normalized) - 1):
        avg_neighbor = (normalized[i-1] + normalized[i+1]) / 2
        if abs(normalized[i] - avg_neighbor) < 3.5:
            smoothed.append(avg_neighbor)
        else:
            smoothed.append(normalized[i])

    # Placeholder for unused diagnostic metric
    peak_fluctuation = max(smoothed) - min(smoothed) if smoothed else 0

    # Introduce irrelevant secondary processing path (dead code branch)
    debug_mode = False
    auxiliary_buffer = []
    if debug_mode:
        for val in smoothed:
            auxiliary_buffer.append(val ** 2)  # Never executed

    # Core logic: identify values above dynamic threshold
    dynamic_threshold = threshold + safety_margin
    filtered_data = [x for x in smoothed if x > dynamic_threshold]

    # Secondary filtering via slicing (relevant use)
    if len(filtered_data) > 4:
        filtered_data = filtered_data[1:-1]  # Remove first and last to reduce outlier impact

    # Calculate correction factor based on data density
    density = len([x for x in smoothed if x > threshold])
    coverage_ratio = density / len(smoothed) if smoothed else 0
    correction_factor = round(coverage_ratio * 2.5, 3)

    # UNUSED distraction variables
    aggregation_weight = 0.87
    temporal_decay = 1.05
    stability_index = sum([abs(smoothed[i] - smoothed[i-1]) for i in range(1, len(smoothed))]) if smoothed else 0

    # Key computational statement
    filtration_score = sum(filtered_data) * correction_factor

    # Print result as required
    print(f"Result: {filtration_score}")

    return filtration_score

# Simulate sensor input
sensor_input = [25.1, 18.3, 12.7, 9.8, 21.0, 16.5, 14.2, 23.8, 11.0, 19.4]
threshold_setting = 8.5
margin = 1.2

result = analyze_sensor_data(sensor_input, threshold_setting, margin)