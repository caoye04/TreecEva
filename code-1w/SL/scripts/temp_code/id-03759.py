def analyze_wave_pattern(samples, base_freq):
    # Preprocess signal samples using slicing and transformation
    filtered = samples[::2]  # Take even-indexed samples
    normalized = [x / max(filtered) for x in filtered]

    # Frequency-dependent phase adjustment (irrelevant to final result)
    dummy_phases = [base_freq * i % 4 for i in range(len(normalized))]
    temp_buffer = sum([p ** 1.5 for p in dummy_phases if p > 1])

    # Generate phase states based on threshold logic
    phase_states = []
    for val in normalized:
        if val > 0.75:
            phase_states.append(3)
        elif val > 0.5:
            phase_states.append(2)
        elif val > 0.25:
            phase_states.append(1)
        else:
            phase_states.append(0)

    # Frequency weights derived from sample distribution (some distraction here)
    freq_count = {}
    for s in samples:
        freq_count[s] = freq_count.get(s, 0) + 1
    frequency_weights = {k: v * base_freq for k, v in freq_count.items()}

    # Dead code path - never executed but looks relevant
    if False:
        fallback = list(map(lambda x: x * 0.1, phase_states))
        frequency_weights['correction'] = sum(fallback)

    # Core calculation occurs here
    def calculate_interference(phases, weights):
        total = 0
        weight_values = list(weights.values())
        for i, p in enumerate(phases):
            # Use modular indexing with weight cycle
            w = weight_values[i % len(weight_values)]
            total += p * (w % 3) - (i % 2)  # Complex interaction
        return total

    net_phase_shift = calculate_interference(phase_states, frequency_weights)
    
    # Irrelevant post-processing
    smoothed = [net_phase_shift / (i+1) for i in range(3)]
    checksum = sum(smoothed) * 1e-2

    # Final output
    print(f"Result: {net_phase_shift}")

# Input data
signal_samples = [12, 18, 24, 12, 30, 18, 24, 30]
base_frequency = 5

analyze_wave_pattern(signal_samples, base_frequency)