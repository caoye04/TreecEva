def analyze_system_metrics():
    # Simulated sensor readings (irrelevant initializations)
    pressure_readings = [101.3, 102.1, 99.7, 100.5, 103.4]
    humidity_levels = [45, 48, 53, 61, 57]
    vibration_data = [0.02, 0.03, 0.05, 0.07, 0.04]

    # Distractor: Unused function for unrelated computation
    def compute_wind_chill(temp, wind):
        return 13.12 + 0.6215*temp - 11.37*(wind**0.16) + 0.3965*temp*(wind**0.16)

    # Core variables with mixed relevance
    base_temperature = 23.5
    calibration_offset = -1.2
    temperature_samples = [22.1, 24.3, 23.8, 25.0, 22.9]
    sample_weights = [0.1, 0.2, 0.4, 0.2, 0.1]  # weighted average factors

    # Irrelevant transformation (dead code path)
    processed_vibration = list(map(lambda x: x ** 2 if x > 0.04 else 0, vibration_data))

    # Compute effective temperature (used later)
    weighted_temp = sum(t * w for t, w in zip(temperature_samples, sample_weights))
    adjusted_temp = weighted_temp + calibration_offset

    # Distractor: unused statistical calculation
    temp_mean = sum(temperature_samples) / len(temperature_samples)
    temp_variance = sum((t - temp_mean)**2 for t in temperature_samples) / len(temperature_samples)

    # Phase and operational state logic (nested conditionals)
    system_phase = 'active'
    phase_code = 7 if system_phase == 'standby' else 9
    phase_modulator = phase_code % 4

    # Multiple assignments and decoy unpacking
    status_flags = [True, False, True]
    flag_a, flag_b, flag_c = status_flags  # Unpacked but only one used

    # Conditional expression with distractors
    anomaly_detected = any(v > 0.06 for v in vibration_data)
    safety_multiplier = 0.8 if anomaly_detected else 1.0

    # Red herring: complex but unused bitwise operation chain
    security_key = 0b110101
    encrypted_flag = (security_key ^ 0b101010) >> 2 & 0b1111

    # Aggregate score from multiple sources (only some are relevant)
    base_score = 150
    temp_penalty = abs(adjusted_temp - base_temperature) * 3
    noise_bonus = len([v for v in vibration_data if v < 0.05]) * 5
    aggregate_score = base_score - temp_penalty + noise_bonus

    # Decoy loop with no effect on final result
    for _ in range(3):
        temp_penalty += 1  # This does not affect the earlier used value

    # Key computational step involving conditional logic and float arithmetic
    if adjusted_temp > 24.0:
        temperature_factor = 1.75
    elif adjusted_temp < 22.0:
        temperature_factor = 2.25
    else:
        temperature_factor = 2.0

    # Critical assignment: this is where the answer comes from
    final_diagnostic = aggregate_score + temperature_factor * phase_modulator

    # Final red herring: enumerate used in irrelevant context
    for i, reading in enumerate(pressure_readings):
        pressure_readings[i] = reading * (1 + 0.01 * (i % 2))

    print(f"Result: {final_diagnostic}")

analyze_system_metrics()