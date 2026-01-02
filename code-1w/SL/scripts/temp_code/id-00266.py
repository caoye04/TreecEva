def analyze_sensor_array(raw_readings, calibration_offset=0.73):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 0.98 + 2.1 for x in raw_readings if x > 0]
    filtered = [y for y in normalized if y < 100]

    # Misleading intermediate computation (dead path)
    outlier_count = 0
    temp_buffer = []
    for val in raw_readings:
        if val > 950:
            outlier_count += 1
            temp_buffer.append(val * calibration_offset)

    # Unused helper function (red herring)
    def smooth(data):
        return [sum(data[i:i+3]) / 3 for i in range(len(data)-2)]

    # Actual relevant data processing begins
    base_magnitude = sum(abs(x) for x in raw_readings)
    checksum = 0
    for i, reading in enumerate(raw_readings):
        if i % 2 == 0:
            checksum ^= int(reading)  # Bitwise XOR accumulation

    # Conditional expression with meaningful logic
    adjustment = 1.5 if len(raw_readings) > 5 else 0.8

    # Tuple unpacking (relevant)
    (primary, secondary) = (raw_readings[0], raw_readings[-1])

    # Destructuring with zip and enumerate (required Python feature)
    indexed_shift = 0
    for idx, (a, b) in enumerate(zip(raw_readings, raw_readings[1:])):
        indexed_shift += (idx + 1) * (a - b)  # Accumulate position-weighted difference

    # Complex but deterministic aggregation
    aggregate_score = base_magnitude + checksum + abs(primary - secondary) * adjustment
    
    # Correction based on parity of sum (subtle but critical)
    total_sum = sum(raw_readings)
    correction_factor = -5 if total_sum % 2 == 0 else 7

    # Final diagnostic calculation (target statement)
    final_diagnostic = aggregate_score + correction_factor

    # Dead code path (distraction)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) * 0.5

    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data with domain-specific meaning
sensor_data = [12, -45, 89, 102, -33, 67, 201]
analyze_sensor_array(sensor_data)