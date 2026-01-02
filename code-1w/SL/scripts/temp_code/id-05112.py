def analyze_sensor_data(raw_readings, thresholds):
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in normalized if x > thresholds['noise_floor']]
    
    # Irrelevant transformation - red herring
    inverted_map = {i: 1.0 / (v + 1e-5) for i, v in enumerate(filtered)}
    decoy_stats = {
        'peak': max(filtered),
        'trough': min(filtered),
        'spread': max(filtered) - min(filtered)
    }

    # Distractor: unused function
    def calculate_entropy(values):
        from math import log
        total = sum(values)
        probabilities = [v / total for v in values]
        return -sum(p * log(p) for p in probabilities if p > 0)

    # Misleading intermediate aggregation
    shadow_index = 0
    temp_accumulator = 0
    for idx, val in enumerate(filtered):
        if idx % 2 == 0:
            temp_accumulator += val * 1.5
        else:
            temp_accumulator -= val * 0.5
        shadow_index += 1

    # Actual relevant logic buried here
    bucket_sums = [0] * 3
    for i, v in enumerate(filtered):
        bucket = i % 3
        bucket_sums[bucket] += v * v  # Emphasis on variance-like measure

    transformed = [round(x ** 0.5, 6) for x in bucket_sums]

    # Another distraction: complex but unused zip+enumerate combo
    paired_diagnostics = []
    for i, (a, b) in enumerate(zip(transformed, transformed[1:])):
        paired_diagnostics.append((i, a * b, abs(a - b)))

    # Dead code path - never executed but looks important
    emergency_override = False
    if len(filtered) > 100:
        emergency_override = True
        critical_load = sum([x**2 for x in raw_readings]) // len(raw_readings)

    # Core calculation chain
    rolling_adjustment = 0
    for i, val in enumerate(transformed):
        rolling_adjustment += val * (i + 1)

    baseline_reference = sum(transformed) / len(transformed)
    adjustment_delta = rolling_adjustment - baseline_reference

    # Simulated calibration sequence with distractors
    calibrations = [baseline_reference]
    for _ in range(4):
        new_cal = (calibrations[-1] + adjustment_delta) / 2
        calibrations.append(new_cal)

    # Red herring: bit manipulation that goes nowhere
    binary_fingerprint = 0
    for val in calibrations:
        shifted = int(val * 1000) << 2
        binary_fingerprint ^= shifted
        if binary_fingerprint > 10000:
            binary_fingerprint >>= 1

    # Actual signal extraction
    aggregate_metrics = [baseline_reference, rolling_adjustment]
    aggregate_metrics.extend(calibrations)
    aggregate_metrics.append(sum(bucket_sums))  # Key component

    # Noise injection - irrelevant but plausible
    noise_sequence = []
    for t in range(len(calibrations)):
        phase = t * 0.5
        noise_sequence.append(0.1 * (t % 3) * phase)

    # Final correction based on environmental factors (simulated)
    environment_code = 'STABLE'
    if environment_code == 'FLUCTUATING':
        correction_factor = -0.5 * baseline_reference
    elif environment_code == 'CRITICAL':
        correction_factor = -2.0 * baseline_reference
    else:
        correction_factor = 0.3 * len(filtered)  # Hidden dependency

    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Output required result
    print(f"Result: {final_diagnostic}")

# Execute with test data
data_stream = [127, 89, 144, 211, 95, 133, 178, 101, 156, 192, 77, 163]
config = {'noise_floor': 0.15, 'sensitivity': 2.1}
analyze_sensor_data(data_stream, config)