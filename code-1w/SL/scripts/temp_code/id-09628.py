def analyze_sensor_data(raw_readings, calibration_sequence):
    cumulative_score = 0
    temp_buffer = []
    checksum = 0
    outlier_count = 0
    baseline_reference = [x ** 0.5 for x in range(1, len(calibration_sequence) + 1)]

    # Irrelevant pre-processing (distractor)
    normalization_factor = sum(baseline_reference) / len(baseline_reference)
    adjusted_baseline = [x / normalization_factor for x in baseline_reference]

    for i, reading in enumerate(raw_readings):
        if reading < -100 or reading > 100:
            outlier_count += 1
            continue

        # Real logic begins: transform and accumulate
        transformed = abs(reading) ^ (i % 17)  # Bitwise XOR with index hash
        temp_buffer.append(transformed)

        if i % 3 == 0:
            cumulative_score += transformed * 2
        elif i % 3 == 1:
            cumulative_score -= transformed // 3
        else:
            cumulative_score += (transformed % 7)

        # Checksum for decoy path (never used)
        checksum ^= transformed

    # Dead code path - misleading intermediate result
    def compute_health_index(buf):
        return sum(x for x in buf if x > 50) // max(1, len(buf))

    health_diag = compute_health_index(temp_buffer)  # Unused

    # Linear search for pattern (red herring)
    pattern_found = False
    for j in range(len(temp_buffer) - 2):
        if temp_buffer[j] < temp_buffer[j+1] < temp_buffer[j+2]:
            pattern_found = True
            break

    # Distractor variables with plausible names
    stability_metric = len([x for x in temp_buffer if x < 40])
    volatility_index = sum(1 for x in temp_buffer if x > 70)
    redundancy_check = list(zip(temp_buffer, baseline_reference[:len(temp_buffer)]))

    # Key accumulation using enumerate (required feature)
    offset_correction = 0
    for idx, (val, base) in enumerate(redundancy_check):
        if idx % 4 == 0:
            offset_correction += val % base if base != 0 else 0

    # Actual answer components
    adjustment_factor = (outlier_count * 13) - offset_correction
    cumulative_score += sum([x & 15 for x in temp_buffer])  # Add bitwise AND side-effect

    # Final computation (target execution point)
    final_diagnostic = cumulative_score + adjustment_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused complex structure (distractor)
    class DiagnosticNode:
        def __init__(self, value):
            self.value = value
            self.flagged = False

    node_chain = [DiagnosticNode(x) for x in temp_buffer[::5]]

    return final_diagnostic

# Input data (deterministic)
readings = [i * (-1)**i * (i % 23) for i in range(1, 34)]
calibration = [i*2 for i in range(1, 34)]

result = analyze_sensor_data(readings, calibration)
