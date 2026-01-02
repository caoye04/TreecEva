def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant pre-processing (distractor)
    normalized = [x * 0.98 for x in raw_readings if x > 0]
    outliers = [i for i, v in enumerate(normalized) if v > 500]
    filtered = [v for v in normalized if v < 400]

    # Real processing begins: frequency transformation
    transformed = []
    for i, val in enumerate(calibration_sequence):
        if i % 3 == 0:
            transformed.append(val ** 0.5)
        elif i % 3 == 1:
            transformed.append(val // 4)
        else:
            transformed.append(val + 2)

    # Decoy analysis path (dead code - never used)
    def legacy_analysis(data):
        return sum(x * 2 for x in data if x % 2 == 0)
    
    temp_result = [x for x in transformed if x % 2 == 1]
    secondary_buffer = [0] * len(temp_result)
    for idx, item in enumerate(temp_result):
        secondary_buffer[idx] = item * 3 - 1

    # Actual critical logic: checksum with bit manipulation
    base_checksum = 0
    for num in raw_readings[:len(calibration_sequence)]:
        base_checksum ^= (num << 1)  # Bitwise shift and XOR
        base_checksum &= 0xFFFF  # Keep within 16-bit range

    # Data alignment using zip and enumerate (required feature)
    aligned_pairs = []
    for i, (a, b) in enumerate(zip(filtered, transformed)):
        if i % 2 == 0:
            aligned_pairs.append((a + b) * 1.5)
        else:
            aligned_pairs.append((a - b) * 0.75)

    # Misleading statistical summary (irrelevant)
    avg_misleading = sum(aligned_pairs) / len(aligned_pairs) if aligned_pairs else 0
    variance_proxy = sum((x - avg_misleading) ** 2 for x in aligned_pairs) / len(aligned_pairs)

    # Core diagnostic chain
    rolling_diagnostics = []
    accumulator = base_checksum % 100
    for j in range(5):
        if j % 2 == 0:
            accumulator += j * 3
        else:
            accumulator -= j * 2
        rolling_diagnostics.append(accumulator)

    # Correction based on parity and magnitude
    magnitude_key = len([x for x in raw_readings if x > 100])
    parity_flag = (magnitude_key + base_checksum) % 4

    intermediate_state = rolling_diagnostics[parity_flag] if parity_flag < len(rolling_diagnostics) else 42

    # Final aggregation with decoy list extension
    aggregate_metrics = rolling_diagnostics.copy()
    aggregate_metrics.append(intermediate_state * 2)
    aggregate_metrics.append(intermediate_state - 10)

    # Dead branch: looks important but unused
    if len(filtered) > 10:
        extra_adjustment = sum(filtered) // 100
        aggregate_metrics.append(extra_adjustment)

    # Key statement
    correction_factor = (base_checksum & 0xFF) - 50  # Extract byte and offset
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Output required format
    print(f"Result: {final_diagnostic}")

# Inputs
sensor_input = [120, -5, 340, 150, 95, 200, 450, 80, 110, 300]
calibration_profile = [16, 25, 36, 49, 64, 81, 100, 121]
analyze_sensor_data(sensor_input, calibration_profile)