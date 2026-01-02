def analyze_wave_pattern(wave_data, threshold=0.7):
    # Preprocess wave amplitudes and extract key features
    filtered_peaks = [amp for amp in wave_data if abs(amp) > threshold]
    normalized_peaks = [round(amp / max(filtered_peaks), 3) for amp in filtered_peaks] if filtered_peaks else [0]

    # Simulate phase state transitions based on peak polarity
    phase_states = []
    for val in normalized_peaks:
        if val > 0.5:
            phase_states.append(1)
        elif val < -0.5:
            phase_states.append(-1)
        else:
            phase_states.append(0)

    # Frequency weighting factors (simulated calibration constants)
    base_freq = len(normalized_peaks) + 1
    frequency_weights = [(i + 1) ** 0.5 for i in range(base_freq)]

    # Misleading distraction: energy dispersion calculation (not used in final result)
    total_energy = sum(p**2 for p in normalized_peaks)
    dispersion_factor = total_energy / len(normalized_peaks) if normalized_peaks else 0
    adjusted_dispersion = dispersion_factor * 1.618  # Golden ratio adjustment (unused)

    # Core logic: Calculate net phase interference from state-weighted interactions
    def calculate_interference(phases, weights):
        shift = 0.0
        for i, (phase, weight) in enumerate(zip(phases, weights)):
            if phase != 0:
                shift += phase * weight * (0.1 if i % 2 == 0 else -0.1)
        return round(shift, 4)

    net_phase_shift = calculate_interference(phase_states, frequency_weights)
    
    # Secondary unused analysis: harmonic symmetry check (distractor)
    symmetry_score = 0
    for i in range(len(phase_states)):
        if phase_states[i] == -phase_states[-i-1]:
            symmetry_score += 1

    # Irrelevant transformation chain
    temp_buffer = [x * 2 for x in frequency_weights]
    processed = temp_buffer[::-1]
    final_sum = sum(processed[:len(phase_states)])  # Unused

    return net_phase_shift

# Input data: simulated sensor wave readings
data_stream = [0.1, -1.2, 0.4, 0.8, -0.9, 0.3, 1.5]

# Execute main analysis
result = analyze_wave_pattern(data_stream)
print(f"Result: {result}")