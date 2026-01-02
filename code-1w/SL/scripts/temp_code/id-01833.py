def analyze_sensor_data():
    # Simulated environmental sensor readings (temperature, pressure, humidity)
    raw_readings = [
        (23.5, 1013.25, 45), (24.1, 1012.80, 47), (22.9, 1014.10, 44),
        (25.3, 1011.90, 50), (26.0, 1010.75, 53), (24.8, 1012.20, 49)
    ]

    # Secondary calibration coefficients (unused in final logic - red herring)
    calib_x, calib_y, calib_z = 1.002, 0.998, 1.011

    # Extract temperature and pressure for trend analysis
    temperatures = [entry[0] for entry in raw_readings]
    pressures = [entry[1] for entry in raw_readings]

    # Compute moving average of temperature (distractor computation)
    temp_moving_avg = []
    for i in range(2, len(temperatures)):
        temp_moving_avg.append((temperatures[i-2] + temperatures[i-1] + temperatures[i]) / 3)

    # Irrelevant string-based identifier processing (string method + enumerate distraction)
    sensor_ids = ['SNSR_A01', 'SNSR_B02', 'SNSR_C03', 'SNSR_D04', 'SNSR_E05', 'SNSR_F06']
    id_suffixes = [sid.split('_')[-1] for sid in sensor_ids]
    indexed_suffixes = list(enumerate(id_suffixes, start=1))

    # Unused transformation: reverse and slice (dead code path)
    reversed_pairs = list(zip(reversed(temperatures), pressures))[::2]

    # Real data path begins here: detect anomalous pressure drop
    pressure_deltas = [pressures[i] - pressures[i+1] for i in range(len(pressures)-1)]
    significant_drops = [delta for delta in pressure_deltas if delta > 1.0]

    # Compute diagnostic baseline from temperature variance
    mean_temp = sum(temperatures) / len(temperatures)
    temp_variance = sum((t - mean_temp) ** 2 for t in temperatures) / len(temperatures)
    stability_index = 1 / (temp_variance + 1)  # Higher = more stable

    # Simulated hardware jitter compensation (bitwise distraction)
    jitter_mask = 0b1101 ^ 0b1011 & 0b0110  # Irrelevant bit ops
    jitter_threshold = (jitter_mask << 2) | 0b0011  # Unused constant

    # Primary metric: cumulative pressure stress factor
    stress_factor = sum(pressure_deltas) * 10

    # Hidden correction based on initial vs final temp (key insight)
    temp_trend = temperatures[-1] - temperatures[0]
    if temp_trend > 0:
        trend_modifier = 2
    else:
        trend_modifier = -1

    # Nested conditional with tuple unpacking (relevant logic)
    diagnostics = []
    for i, (t, p) in enumerate(zip(temperatures, pressures)):
        if t > 24 and p < 1012:
            score_code = 'HIGH'
            level_flag = 3
        elif t > 23:
            score_code = 'MODERATE'
            level_flag = 2
        else:
            score_code = 'LOW'
            level_flag = 1
        # Append tuple (index, flag, code) - destructuring later
        diagnostics.append((i, level_flag, score_code))

    # Destructuring assignment in loop (actual usage)
    aggregate_metrics = []
    for idx, flag, code in diagnostics:
        if flag >= 2:
            aggregate_metrics.append(flag * (idx + 1))

    # Spurious list slicing distraction
    mid_metrics = aggregate_metrics[1:-1] if len(aggregate_metrics) > 2 else [0]
    mid_avg = sum(mid_metrics) / len(mid_metrics)

    # UNUSED function (decoy)
    def calculate_entropy(data):
        from math import log
        total = sum(data)
        probs = [v/total for v in data]
        return -sum(p * log(p) for p in probs if p > 0)

    # Constants for final calculation
    scaling_constant = 17
    base_offset = 312
    correction_factor = len(significant_drops) + trend_modifier

    # Critical statement
    final_diagnostic = aggregate_metrics[-1] + correction_factor * scaling_constant

    # Print result (required)
    print(f"Result: {final_diagnostic}")

    # Unused entropy of aggregate metrics (red herring)
    if len(aggregate_metrics) > 1:
        entropy = sum(m * 0.01 for m in aggregate_metrics)

    return final_diagnostic

# Execute and capture
result = analyze_sensor_data()