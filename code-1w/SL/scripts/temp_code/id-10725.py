def simulate_system_stability(base_frequency, input_pulses):
    # Simulate a dynamic system with damping and feedback
    peak_magnitude = 0
    cumulative_phase = 0
    harmonic_series = []

    for pulse in input_pulses:
        if pulse % 3 == 0:
            peak_magnitude += pulse * 0.1
        elif pulse % 5 == 0:
            cumulative_phase += (pulse % 7) * 0.05
        
        # Generate harmonic overtones based on pulse
        overtone = (pulse ** 0.5) * base_frequency
        harmonic_series.append(overtone)

    # Misleading intermediate calculation (not used in final result)
    average_harmonic = sum(harmonic_series) / len(harmonic_series) if harmonic_series else 0
    instability_factor = abs(peak_magnitude - cumulative_phase) * 100

    # Core state variables
    system_potential = sum(h ** 2 for h in harmonic_series if h > 10) * 0.01
    feedback_loop = list(map(lambda x: x * 0.1 + 5, harmonic_series))

    # State accumulation with tuple unpacking
    temp_states = [(i, fb, system_potential) for i, fb in enumerate(feedback_loop)]
    active_nodes, corrections, _ = zip(*temp_states[:5]) if len(temp_states) >= 5 else ((0,), (0,), (0,))

    correction_sum = sum(corrections)

    # Real contribution path
    raw_balance = system_potential - correction_sum
    equilibrium_score = int(raw_balance + len(active_nodes))

    # Distractor: unused signal processing chain
    noise_floor = 0
    for i in range(len(harmonic_series) - 1):
        noise_floor += abs(harmonic_series[i] - harmonic_series[i+1])
    normalized_noise = noise_floor / (len(harmonic_series) if harmonic_series else 1)

    # Final adjustment function (defined inline to increase complexity)
    apply_damping = lambda score, forces: score - int(forces * 0.01) if score > 50 else score + 10

    # Key statement
    final_adjustment = apply_damping(equilibrium_score, instability_factor)

    # Output target result
    print(f"Result: {equilibrium_score}")

# Inputs
frequency = 440
pulses = [12, 15, 18, 20, 24, 25, 30]

# Execute
simulate_system_stability(frequency, pulses)