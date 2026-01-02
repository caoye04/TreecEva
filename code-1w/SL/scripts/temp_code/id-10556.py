def analyze_sensor_data(raw_stream, calibration_key):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.003 for x in raw_stream if x > 0]
    filtered = list(filter(lambda v: v < 1000, normalized))
    snapshot = ''.join([chr(int(x) % 127) for x in filtered[:10]])

    # Meaningful but misleading intermediate (red herring)
    entropy_guess = sum([filtered[i] ^ filtered[i+1] for i in range(len(filtered)-1)]) % 10000

    # Actual signal extraction (key path)
    valid_points = []
    for val in raw_stream:
        if val % 4 == 0 and val > 0:
            adjusted = val // 4
            if adjusted % 2 == 1:
                valid_points.append(adjusted)

    # Decoy analysis using string methods (distractor)
    metadata_tag = f"LOG_{calibration_key.upper()}_END"
    tag_parts = metadata_tag.split('_')
    if len(tag_parts) > 3:
        shift_offset = ord(tag_parts[1][0]) % 5
    else:
        shift_offset = 0

    # Fake diagnostic with dictionary operations (dead path)
    diagnostics = {"level": "critical", "noise_floor": 42.5, "peak_count": len(filtered)}
    if diagnostics["level"] == "warning":
        diagnostics["status_code"] = 1
    else:
        diagnostics["status_code"] = -1  # Never used

    # Core logic: find second-highest valid point and apply modular transform
    if len(valid_points) >= 2:
        sorted_valid = sorted(valid_points, reverse=True)
        primary_signal = sorted_valid[1]  # Second highest
        base_energy = (primary_signal * 7) % 89
    else:
        base_energy = 13

    # Secondary correction via bitwise interaction
    control_flag = calibration_key.lower().count('a') | 5
    correction_factor = (base_energy ^ control_flag) - 3

    # Use list comprehension to compute distractor metric
    volatility = [x for x in filtered if x % 2 == 0]
    avg_volatility = sum(volatility) / len(volatility) if volatility else 0.0

    # Real aggregation (buried among noise)
    aggregate_score = 0
    for i, pt in enumerate(valid_points):
        if i % 3 == 0:
            aggregate_score += pt % 17

    # Final computation — this is the answer
    final_diagnostic = aggregate_score + correction_factor

    # Print required result
    print(f"Result: {final_diagnostic}")

    # Unused return branches (dead code)
    if final_diagnostic < 0:
        return None
    return diagnostics  # Not part of execution flow affecting answer

# Simulate input data and execution
sensor_input = [12, 24, 55, 64, 99, 100, 108, 150, 192, 200, 212]
calibration_code = "safemode"

analyze_sensor_data(sensor_input, calibration_code)