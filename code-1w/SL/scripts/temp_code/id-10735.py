def analyze_sensor_data():
    # Simulated sensor readings (real data)
    base_readings = [127, 255, 64, 192, 32, 160]
    calibration_offsets = [8, -4, 12, -16, 6, -10]

    # Apply calibration using zip and list comprehension (relevant)
    calibrated = [b + c for b, c in zip(base_readings, calibration_offsets)]

    # Irrelevant: Historical thresholds (distractor)
    historical_min = [50, 100, 30, 80, 20, 70]
    historical_max = [200, 300, 150, 250, 100, 200]
    compliance_flags = [1 if hmin <= val <= hmax else 0 for val, hmin, hmax in zip(calibrated, historical_min, historical_max)]

    # Decoy function: Never called (dead code path)
    def deprecated_analysis(x):
        return sum(v ** 0.5 for v in x) // len(x)

    # Bit manipulation for noise filtering (relevant)
    filtered = []
    for val in calibrated:
        processed = val & 0xFF  # Ensure 8-bit range
        processed = processed ^ 0xAA  # XOR scramble pattern
        processed = (processed >> 2) & 0x3F  # Shift and mask
        filtered.append(processed)

    # Compute aggregate score using lambda and enumerate (relevant)
    weight_func = lambda i: 1.5 - (i * 0.1)
    weighted_sum = sum(weight_func(i) * v for i, v in enumerate(filtered))
    aggregate_score = int(weighted_sum)

    # Environmental compensation (relevant)
    ambient_temperature = 23.5
    temperature_factor = ambient_temperature - 20.0
    stability_log = [abs(ambient_temperature - t) for t in [22.1, 23.0, 24.5, 25.0, 22.8]]
    avg_stability = sum(stability_log) / len(stability_log)

    # Red herring: Unused complex structure (irrelevant)
    system_status = {
        'nodes': ['A', 'B', 'C'],
        'active': {1, 2, 3, 4},
        'failed': set(),
        'diagnostics': [(x, x % 10) for x in range(100, 110)]
    }
    system_status['version'] = '2.1.0'
    _ = [system_status.pop('version') for _ in range(1)]  # Useless mutation

    # Linear search for threshold breach (irrelevant due to no action)
    threshold_breaches = 0
    for temp in [21.0, 22.5, 23.5, 24.0, 26.0]:
        if temp > 25.0:
            threshold_breaches += 1

    # Key computational chain (relevant)
    baseline_correction = 42
    signal_quality = len([f for f in filtered if f > 30])
    correction_ratio = signal_quality / len(filtered)
    intermediate_flag = any(f < 10 for f in filtered)

    # Final diagnostic calculation (critical execution point)
    final_diagnostic = aggregate_score + temperature_factor * correction_ratio

    # Output required result
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()