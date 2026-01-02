def analyze_wave_pattern(frequencies):
    base_reference = 7
    harmonic_sequence = [f % 13 for f in frequencies if f > 0]
    harmonic_sequence_length = len(harmonic_sequence)

    # Distractor: Amplitude analysis with no impact on final result
    amplitudes = []
    for f in frequencies:
        if f > 10:
            amplitude = (f * 0.33) + 1.5
            amplitudes.append(round(amplitude, 2))
    normalized_energy = sum(a**2 for a in amplitudes) if amplitudes else 0.0

    # Real computation begins
    weighted_sum = 0
    for i, h in enumerate(harmonic_sequence):
        weight = 2 if i % 3 == 0 else 1
        weighted_sum += h * weight

    # Secondary distractor: unused phase mapping
    phase_map = dict(zip(range(len(frequencies)), [f % 7 for f in frequencies]))
    temp_offset = 0
    for idx, val in enumerate(frequencies):
        if val % 4 == 0:
            temp_offset += idx * (val % 5)

    # Core logic with conditional expression and lambda
    adjust = (lambda x: x + 1 if x < 50 else x - 1)(weighted_sum % 40)
    activation_threshold = 25 if len(frequencies) > 5 else 30

    cycles = []
    for i in range(1, 4):
        cycle_value = (weighted_sum + i * adjust) % (harmonic_sequence_length + 1)
        if cycle_value >= activation_threshold - 20:
            cycles.append(cycle_value)

    active_cycle = cycles[-1] if cycles else 0

    # Key statement
    final_phase = (active_cycle ** 2) % harmonic_sequence_length

    # Print required output
    print(f"Target result: {final_phase}")

    return final_phase

# Execute with input
input_frequencies = [12, -5, 26, 39, 44, 13, 8]
analyze_wave_pattern(input_frequencies)