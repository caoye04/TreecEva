def main():
    # Simulate quantum system stability analysis
    energy_levels = [i**2 + 3*i - 10 for i in range(1, 8)]
    damping_factor = 0.85
    adjustment_rate = 1.2

    # Irrelevant thermodynamic computations (distractor)
    entropy_values = [abs(level) * 0.1 for level in energy_levels]
    temperature_gradient = sum(entropy_values) / len(entropy_values)
    hypothetical_pressure = temperature_gradient * 2.5 if temperature_gradient > 1 else 0

    # Core signal processing chain
    filtered_energies = list(map(lambda x: x * damping_factor, energy_levels))
    net_energy = sum(filtered_energies) - 5.5  # Baseline correction

    # Derive fluctuation pattern
    energy_fluctuations = []
    for i in range(1, len(filtered_energies)):
        delta = filtered_energies[i] - filtered_energies[i-1]
        energy_fluctuations.append(round(delta, 3))

    # Secondary irrelevant computation: coherence estimation (not used)
    coherence_pairs = [(a, b) for a, b in zip(filtered_energies, filtered_energies[1:])]
    coherence_index = sum([abs(a - b) for a, b in coherence_pairs]) / len(coherence_pairs)

    # Threshold logic with conditional expression
    base_threshold = 4.7
    dynamic_modifier = 0.3 if len(energy_fluctuations) > 5 else 0.1
    threshold_func = lambda x: abs(x) > (base_threshold - dynamic_modifier)

    # Evaluate system stability
    true_spikes = list(filter(threshold_func, energy_fluctuations))
    spike_magnitude = sum(abs(spike) for spike in true_spikes)

    # State tracking variables (some unused)
    state_history = []
    for mag in true_spikes:
        state_flag = 'CRITICAL' if mag > 6 else 'STABLE'
        state_history.append(state_flag)
        if mag > 7:
            break  # Early exit red herring

    # Final equilibrium score calculation (key result)
    adjustment = len(true_spikes) * adjustment_rate
    equilibrium_score = round(spike_magnitude - adjustment, 3)

    # Print final target result
    print(f"Result: {equilibrium_score}")

main()