def analyze_thermal_phases():
    # Simulate multi-phase thermal system analysis with noise filtering
    temperatures = [23.5, 24.1, 19.8, 25.6, 22.3, 20.1, 26.7, 27.3]
    threshold = 24.0
    high_temp_phases = set()
    low_temp_phases = set()

    for i, temp in enumerate(temperatures):
        if temp >= threshold:
            high_temp_phases.add(i)
        else:
            low_temp_phases.add(i)

    # Misleading computation: calculate average deviation (not used later)
    avg = sum(temperatures) / len(temperatures)
    dev_sum = 0
    for t in temperatures:
        dev_sum += abs(t - avg)
    avg_deviation = dev_sum / len(temperatures)

    # Signal processing simulation
    phase_data = [0] * 8
    for i in range(8):
        if i in high_temp_phases:
            phase_data[i] = (i * 3 + 7) % 23

    # Noise injection and cleanup (some steps irrelevant)
    noise_mask = {2, 5, 6}
    clean_phases = high_temp_phases - noise_mask

    # Key control flow with early exit red herring
    if len(clean_phases) > 10:
        return -1  # Dead code path

    # Core logic hidden among distractions
    base_yield = 0
    for idx in clean_phases:
        base_yield += idx * 2

    # Distractor: unused bitwise rotation
    rotated = (base_yield << 3) | (base_yield >> 5)
    rotated &= 0xFF

    # Another distraction: simulate calibration offset
    calibration_sequence = [1, 0, 1, 1]
    offset = 0
    for bit in calibration_sequence:
        offset = (offset << 1) | bit
    offset %= 9

    # Critical statement embedded in noise
    phase_shift = len(low_temp_phases) * 3
    thermal_capacity = base_yield ^ (phase_shift & 15)

    # Additional misleading operation
    efficiency_ratio = (base_yield + phase_shift) / (thermal_capacity + 1)
    normalized_efficiency = round(efficiency_ratio * 100, 3)

    # Final output
    print(f"Result: {thermal_capacity}")

analyze_thermal_phases()