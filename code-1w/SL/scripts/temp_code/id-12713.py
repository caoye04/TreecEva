def analyze_sensor_data(raw_readings, calibration_factor=1.05):
    # Irrelevant preprocessing: Normalize readings (not used in final path)
    normalized = [round(r * calibration_factor, 3) for r in raw_readings if r > 0]
    outliers = [r for r in raw_readings if r < -100 or r > 1000]

    # Distractor: Simulate redundant diagnostic pass
    diagnostics = []
    temp_flags = []
    for i, val in enumerate(raw_readings):
        if i % 5 == 0:
            temp_flags.append(f"CHK{i}")
        status = "OK" if val >= 0 else "ERR"
        diagnostics.append({"index": i, "status": status})

    # Real processing begins: filter valid telemetry
    valid_telemetry = list(filter(lambda x: 50 <= x <= 950, raw_readings))

    # Compute rolling checksum with bitwise manipulation (used later)
    checksum = 0
    for idx, val in enumerate(valid_telemetry):
        if idx % 2 == 0:
            checksum ^= (val & 255)  # Use lower byte
        else:
            checksum ^= (val >> 4)   # Use shifted nibble

    # Distractor: unused recursive function
    def integrate_signal(data, acc=0.0):
        if not data:
            return acc
        return integrate_signal(data[1:], acc + data[0] * 0.1)

    # Distractor: dead code path with misleading accumulation
    peak_magnitude = max(valid_telemetry, default=0)
    signal_envelope = []
    for v in valid_telemetry:
        if v > peak_magnitude * 0.9:
            signal_envelope.append(v * 1.05)

    # Actual critical transformation chain
    baseline_shift = sum(valid_telemetry) // len(valid_telemetry) if valid_telemetry else 0
    adjusted_readings = [x - baseline_shift for x in valid_telemetry]

    # Generate metrics using conditional expression and zip
    metric_a = sum(adjusted_readings) * 1.1
    metric_b = sum(x ** 2 for x in adjusted_readings) ** 0.5
    metric_c = len([x for x in adjusted_readings if x > 0]) * 100

    # Hidden dependency: system_bias derived from checksum property
    system_bias = checksum % 77 if checksum > 0 else -checksum % 77

    # Aggregate using enumerate and conditional logic
    aggregate_metrics = []
    for i, m in enumerate([metric_a, metric_b, metric_c]):
        adjustment = system_bias if i % 2 == 0 else -system_bias
        aggregate_metrics.append(int(m + adjustment))

    # Dead code: simulated fault injection (never executed)
    fault_mode = False
    if fault_mode:
        aggregate_metrics = [m * 2 for m in aggregate_metrics]

    # Key execution point
    final_diagnostic = aggregate_metrics[-1] + system_bias

    # Red herring: unrelated string encoding
    encoded = ''.join([chr((i + 77) % 26 + 97) for i, _ in enumerate(temp_flags[:3])])

    # Output required result
    print(f"Result: {final_diagnostic}")

# Input data with mixed characteristics
input_readings = [120, -5, 600, 450, 900, 30, 750, 880, 1005, -200, 550]
analyze_sensor_data(input_readings)