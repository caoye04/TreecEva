def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: normalize data (not used in final path)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > 0.5 * sum(raw_readings) / len(raw_readings)]

    # Distractor: complex but unused transformation
    transformed = []
    for i, val in enumerate(calibration_sequence):
        if i % 2 == 0:
            transformed.append(val ** 0.5 if val > 0 else 0)
        else:
            transformed.append(val * 2)

    # Real computation begins: extract key features
    window_size = 3
    rolling_averages = [
        sum(raw_readings[i:i+window_size]) / window_size
        for i in range(len(raw_readings) - window_size + 1)
    ]

    # Use slicing and set operations to identify anomalies
    baseline = raw_readings[:len(raw_readings)//2]
    recent = raw_readings[len(raw_readings)//2:]
    baseline_set = set(round(x, 2) for x in baseline)
    recent_set = set(round(x, 2) for x in recent)
    overlap_count = len(baseline_set & recent_set)

    # Dead code path - looks important but unused
    def deprecated_analysis(data):
        return sum(x*x for x in data) // len(data)

    # Key signal extraction using enumerate and zip
    weighted_sum = 0
    for idx, (b, r) in enumerate(zip(baseline[:len(recent)], recent)):
        weighted_sum += (r - b) * (idx + 1)

    # Secondary metric with distractor variables
    volatility = sum(
        abs(raw_readings[i] - raw_readings[i-1])
        for i in range(1, len(raw_readings))
    )
    stability_score = 1 / (1 + volatility) if volatility else 1

    # Unused complexity: recursive detour
    def calculate_depth(arr):
        if len(arr) <= 1:
            return len(arr)
        return calculate_depth(arr[:len(arr)//2]) + 1

    depth_metric = calculate_depth(raw_readings)  # Computed but irrelevant

    # Core logic embedded among distractions
    aggregate_score = 0
    for i, val in enumerate(rolling_averages):
        if val > sum(raw_readings) / len(raw_readings):
            aggregate_score += int(val)

    # Misleading intermediate with similar naming
    diagnostic_flag = overlap_count > 3
    correction_factor = 1.75 if diagnostic_flag else 0.85
    offset_value = len(baseline_set | recent_set) - len(baseline_set)

    # Critical execution point
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Return unused values to mislead tracing
    return depth_metric, stability_score, transformed

# Input data
sensor_input = [12.5, 14.0, 18.2, 17.9, 20.1, 19.8, 22.3, 21.0]
calib_seq = [0.8, 1.2, 0.9, 1.5, 1.1]

# Execute function
analyze_sensor_data(sensor_input, calib_seq)