def analyze_sensor_stream(raw_readings, thresholds):
    base_offset = 2.5
    temp_cache = []
    outlier_count = 0
    correction_factor = 1.75
    aggregation_log = []

    for idx, reading in enumerate(raw_readings):
        if reading < 0:
            adjusted = abs(reading) * 0.5
        else:
            adjusted = reading + base_offset

        temp_cache.append(adjusted)

        if len(thresholds) > idx % len(thresholds):
            if adjusted > thresholds[idx % len(thresholds)]:
                outlier_count += 1
                continue

        if idx % 3 == 0:
            temp_cache[-1] *= 0.9

    # Irrelevant transformation on unused list
    processed_pairs = [x * 1.1 for x in temp_cache if x > 3]
    sorted_pairs = sorted(enumerate(processed_pairs), key=lambda x: x[1])

    # Dead code path - never accessed
    if False:
        backup_state = {"data": temp_cache, "count": outlier_count}
        for k in backup_state:
            pass

    # Actual signal extraction
    valid_indices = {i for i in range(len(temp_cache)) if i % 4 != 3}
    shifted_values = [temp_cache[i] for i in valid_indices]

    secondary_filter = []
    for val in shifted_values:
        if val > 1.0 and not (val > 10.0 and val < 15.0):  # Excludes mid-range anomalies
            secondary_filter.append(round(val, 2))

    # Distractor: complex but unused set logic
    exclusion_zones = {round(x, 1) for x in raw_readings if x < 5}
    auxiliary_map = dict(zip(exclusion_zones, [x**0.5 for x in exclusion_zones]))

    # Key computation path
    filtered_data = [x for x in secondary_filter if x not in exclusion_zones]

    # Noise weighting - irrelevant to final result
    noise_weight = 0.0
    for zone in exclusion_zones:
        if zone in auxiliary_map:
            noise_weight += auxiliary_map[zone]

    # Critical assignment
    filtration_score = sum(filtered_data) * correction_factor

    # Red herring: additional modification that doesn't affect output
    if len(filtered_data) > 5:
        filtration_score -= noise_weight

    print(f"Result: {filtration_score}")
    return filtration_score

# Simulated sensor data and threshold levels
sensor_input = [4.2, -3.1, 8.7, 12.3, 1.9, 6.5, 14.0, -0.8, 3.3, 9.4, 11.1, 2.7]
dynamic_thresholds = [7.0, 10.5, 5.0, 13.0]

result = analyze_sensor_stream(sensor_input, dynamic_thresholds)