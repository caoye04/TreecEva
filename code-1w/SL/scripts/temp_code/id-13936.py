def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant pre-processing (distractor)
    normalized = [x * 0.98 + 1.5 for x in raw_readings if x > -200]
    filtered = [x for x in normalized if x < 1000]
    temp_cache = {i: val ** 0.5 for i, val in enumerate(filtered) if val > 0}

    # Critical path begins: extract key features
    valid_indices = []
    for i, val in enumerate(raw_readings):
        if val >= thresholds[0] and val <= thresholds[1]:
            valid_indices.append(i)

    # Dead code path - looks important but unused (red herring)
    def legacy_calibrate(x):
        return (x * 1.05) - 2.3

    # Decoy transformation on wrong data subset
    shadow_copy = raw_readings[::-1]
    for j in range(len(shadow_copy)):
        shadow_copy[j] = shadow_copy[j] ^ 0xFF  # Bitwise red herring

    # Real processing starts here: frequency analysis
    freq_map = {}
    for idx in valid_indices:
        reading = raw_readings[idx]
        freq_map[reading] = freq_map.get(reading, 0) + 1

    # Use zip to align indices and values for scoring
    paired_metrics = []
    for index, value in zip(valid_indices, [raw_readings[i] for i in valid_indices]):
        score = (value % 17) * (index % 5)
        adjustment = 1 if value > thresholds[0] + (thresholds[1] - thresholds[0]) / 2 else 0.85
        paired_metrics.append(score * adjustment)

    # Compute intermediate stats (some irrelevant)
    avg_metric = sum(paired_metrics) / len(paired_metrics) if paired_metrics else 0
    peak = max(freq_map.keys(), default=0)
    entropy_proxy = sum([v * v for v in freq_map.values()])  # Misleading complexity

    # Distractor: unused complex calculation
    checksum = 0
    for i, val in enumerate(raw_readings):
        checksum ^= int(val * 1.7)
        checksum = (checksum + i) % 10000

    # Core logic: weighted aggregation based on frequency and position
    weighted_sum = 0
    weight_total = 0
    for i, metric in enumerate(paired_metrics):
        freq = freq_map[raw_readings[valid_indices[i]]]
        weight = freq * (i + 1) ** 0.5
        weighted_sum += metric * weight
        weight_total += weight

    final_score = 0
    if weight_total > 0:
        final_score = weighted_sum / weight_total

    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Simulate sensor readings and execute
data_stream = [84, 92, 84, 75, 96, 84, 75, 92, 88, 92, 84]
bounds = [80, 95]
result = analyze_sensor_data(data_stream, bounds)