def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [x * 0.98 for x in raw_readings if x > 0]
    offset_adjusted = [x - 5 for x in raw_readings]

    # Distractor: complex-looking but unused signal filtering
    def butterworth_filter(signal):
        return [s * 0.5 + 0.5 for s in signal]

    filtered = butterworth_filter(offset_adjusted)  # Dead path

    # Real computation begins: extract anomalies using set logic
    baseline = set(range(100, 200))
    observed = set(raw_readings)
    anomalies = observed - baseline  # Values outside expected range

    # Use enumerate to find positions of high-risk anomalies
    critical_indices = []
    for i, val in enumerate(raw_readings):
        if val in anomalies and val > 250:
            critical_indices.append(i)

    # Misleading aggregation: looks important but unused
    risk_sum = sum([raw_readings[i] ** 2 for i in critical_indices])
    severity_level = len(critical_indices) * 100

    # Core logic hidden among distractions
    temp_registry = {}
    for idx, (a, b) in enumerate(zip(calibration_sequence, raw_readings)):
        temp_registry[idx] = (a + b) % 97

    # Another red herring: recursive checksum (never called)
    def recursive_checksum(data, depth=0):
        if depth >= 3:
            return data[0]
        return recursive_checksum(data[1:] + [data[0]], depth + 1)

    # Actual key computation chain
    running_total = 0
    for i in range(len(raw_readings)):
        if i % 3 == 0:
            running_total += raw_readings[i] // 7
        elif i % 4 == 0:
            running_total -= raw_readings[i] // 11

    # Hidden dependency: count overlapping indices
    overlap_count = 0
    calib_set = set(calibration_sequence)
    for i in critical_indices:
        if i < len(calibration_sequence) and calibration_sequence[i] in observed:
            overlap_count += 1

    # Decoy assignment with similar name
    final_diagnostic_temp = running_total * 3 - severity_level  # Not the answer

    # Key intermediate values
    aggregate_score = running_total + len(anomalies) * 5
    correction_factor = overlap_count * 12

    # Critical statement
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused but plausible-looking diagnostics
    diagnostic_log = {
        'entries': len(raw_readings),
        'filtered_count': len(filtered),
        'checksum': sum(temp_registry.values())
    }

    return final_diagnostic

# Simulate input data
sensor_readings = [105, 132, 88, 267, 144, 92, 301, 110, 75, 283]
calibration_profile = [101, 95, 88, 267, 150, 93, 302, 109, 77, 280]

# Execute function
result = analyze_sensor_data(sensor_readings, calibration_profile)