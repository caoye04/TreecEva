def analyze_sensor_data(raw_readings, threshold=75):
    # Simulate preprocessing of IoT sensor array data
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100) for x in raw_readings]
    outliers = set()
    for i, val in enumerate(normalized):
        if i > 0 and abs(val - normalized[i-1]) > 40:
            outliers.add(i)
            outliers.add(i-1)

    # Irrelevant transformation: frequency domain simulation (distractor)
    freq_components = []
    for k in range(len(normalized)):
        comp = sum(normalized[n] * (2.0 ** (-2.0j * 3.14159 * k * n / len(normalized))) for n in range(len(normalized)))
        freq_components.append(abs(comp))

    # Identify stable segments above threshold
    stable_segments = []
    current_segment = []
    for idx, reading in enumerate(normalized):
        if reading >= threshold and idx not in outliers:
            current_segment.append(reading)
        else:
            if len(current_segment) >= 3:
                stable_segments.append(current_segment)
            current_segment = []
    if len(current_segment) >= 3:
        stable_segments.append(current_segment)

    # Flatten segments into candidate pool
    candidate_pool = []
    for segment in stable_segments:
        candidate_pool.extend(segment)

    # Secondary filter based on modular consistency (relevant logic)
    purified_elements = []
    for val in candidate_pool:
        if val % 5 == 0 and val % 3 != 0:  # divisible by 5 but not by 3
            purified_elements.append(val)

    # Dead code path: entropy calculation (unused)
    if len(purified_elements) > 10:
        import math
        counts = {}
        for v in purified_elements:
            counts[v] = counts.get(v, 0) + 1
        entropy = -sum((count / len(purified_elements)) * math.log2(count / len(purified_elements)) for count in counts.values())
        entropy = round(entropy, 3)

    # Key computation — target variable
    filtration_score = len(purified_elements)

    # Decoy variable with misleading name
    efficiency_ratio = sum(purified_elements) / len(purified_elements) if purified_elements else 0

    # Unused clustering attempt (distractor)
    clusters = {}
    for elem in purified_elements:
        bucket = elem // 10
        if bucket not in clusters:
            clusters[bucket] = []
        clusters[bucket].append(elem)

    # Early termination mock (never triggers due to data)
    if filtration_score < 0:
        return -1

    print(f"Result: {filtration_score}")
    return filtration_score

# Simulated environmental sensor readings (pre-seeded)
data_stream = [68, 70, 72, 85, 90, 92, 45, 88, 91, 87, 89, 93, 95, 73, 77, 80, 82, 96, 98, 100]
analyze_sensor_data(data_stream)