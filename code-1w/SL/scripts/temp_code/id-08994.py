def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant transformation: Normalize readings (not used in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100, 2) for x in raw_readings]

    # Distractor variables
    baseline_adjustment = sum([x for x in raw_readings if x > 50]) * 0.03
    temp_offset = max(raw_readings) - min(raw_readings)
    shadow_buffer = [x * 1.1 for x in raw_readings if x < 40]  # Dead code path

    # Real computation begins: filter critical readings
    critical_readings = [x for x in raw_readings if x > thresholds[0] and x % 2 == 1]

    # Misleading intermediate score (looks important but unused)
    heuristic_score = len(critical_readings) * temp_offset // 2

    # Actual signal processing chain
    processed_signals = []
    for idx, val in enumerate(critical_readings):
        if idx % 2 == 0:
            processed_signals.append(val ** 0.5)
        else:
            processed_signals.append(val // 3)

    # Secondary distractor: simulate calibration (never applied)
    calibration_map = dict(zip(['low', 'mid', 'high'], [1.05, 1.0, 0.95]))
    drift_correction = sum([x for x in raw_readings if x in range(45, 75)]) * 0.01

    # Key data transformation using enumerate and zip
    index_weights = [1.1 ** i for i in range(len(processed_signals))]
    weighted_values = []
    for i, val in enumerate(processed_signals):
        weight = index_weights[i] if i < len(index_weights) else 1.0
        weighted_values.append(val * weight)

    # Aggregate from weighted signals
    aggregate_score = int(sum(weighted_values))

    # Another red herring: complex bit manipulation with no impact
    decoy_state = 0b101010
    for x in raw_readings:
        decoy_state ^= (x & 0b1111) << 2
        if decoy_state > 200:
            decoy_state = decoy_state >> 1

    # Conditional correction factor based on threshold crossing pattern
    pattern_detected = False
    for a, b in zip(raw_readings, raw_readings[1:]):
        if a < thresholds[1] and b > thresholds[1]:
            pattern_detected = True
            break

    correction_factor = 17 if pattern_detected else -5

    # Critical assignment point
    final_diagnostic = aggregate_score + correction_factor

    # Unused sorting operation (distractor)
    sorted_diagnostics = sorted(weighted_values, reverse=True)

    # Output required result
    print(f"Result: {final_diagnostic}")

# Simulate sensor input and execute
data_stream = [32, 55, 67, 44, 73, 58, 61, 79]
trigger_limits = [50, 60]
analyze_sensor_data(data_stream, trigger_limits)