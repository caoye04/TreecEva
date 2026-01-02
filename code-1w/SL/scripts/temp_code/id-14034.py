def analyze_wave_pattern(spectrum):
    base_amplitudes = [abs(x) for x in spectrum if x != 0]
    normalized = [round(a / max(base_amplitudes), 3) for a in base_amplitudes]

    # Misleading intermediate: power distribution (not used later)
    total_power = sum([n**2 for n in normalized])
    avg_power = total_power / len(normalized) if normalized else 0
    power_peaks = [p for p in normalized if p > avg_power]

    # Generate phase states using index tracking
    phase_states = []
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            phase_states.append(int(val * 360) % 180)
        else:
            phase_states.append(-(int(val * 200) % 90))

    # Frequency weights with distractor logic
    weights = [i + 1 for i in range(len(normalized))]
    scaling_factor = sum(weights) / len(weights) if weights else 1
    frequency_weights = [w * scaling_factor for w in weights]

    # Dead code path - simulates alternate model but never invoked
    def legacy_compensation(data):
        return [d * 0.95 for d in data]

    # Core interference calculation
    def calculate_interference(phases, weights):
        weighted_sum = 0
        for p, w in zip(phases, weights):
            contribution = p * w
            if contribution > 0:
                weighted_sum += contribution * 0.8
            else:
                weighted_sum -= abs(contribution) * 0.3
        return int(weighted_sum)  # Final deterministic scalar

    net_phase_shift = calculate_interference(phase_states, frequency_weights)
    
    # Extraneous post-calculation transformations
    shifted_spectrum = [s * 0.5 for s in spectrum]
    residual_energy = sum([abs(se) for se in shifted_spectrum])
    
    # Output target result
    print(f"Result: {net_phase_shift}")

# Input signal with physical interpretation
input_spectrum = [-0.7, 0.3, 0.0, -0.5, 0.8, 0.2]
analyze_wave_pattern(input_spectrum)