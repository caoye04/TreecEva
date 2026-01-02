def calculate_equilibrium(states):
    # Filter active states with non-zero magnitude
    active_states = list(filter(lambda x: abs(x) > 0.1, states))
    
    # Compute weighted contributions (distractor: not used in final result)
    weights = [abs(s) ** 0.5 for s in states]
    total_weight = sum(weights) if weights else 1
    weighted_avg = sum(abs(s) * w for s, w in zip(states, weights)) / total_weight if total_weight else 0
    
    # Core logic: count transitions crossing zero threshold
    transitions = 0
    for i in range(1, len(states)):
        if states[i-1] * states[i] < 0:  # Sign change detected
            transitions += 1
    
    # Apply correction based on transition parity (relevant)
    correction = 1.5 if transitions % 2 == 0 else 0.8
    
    # Secondary distractor: simulate decay (unused)
    decay_factor = 0.95
    damped_states = [s * (decay_factor ** i) for i, s in enumerate(states)]
    avg_damped = sum(damped_states) / len(damped_states) if damped_states else 0
    
    # Final score computation (only this matters)
    base_score = sum(1 for s in active_states if s > 0) - sum(1 for s in active_states if s < 0)
    equilibrium_score = base_score * correction
    
    return equilibrium_score

# Simulated quantum energy state readings over time
time_points = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
energy_states = [0.15, -0.32, 0.41, -0.08, -0.23, 0.67, -0.51]

# Extraneous pre-processing (distractor)
drift_correction = sum(energy_states) / len(time_points)
corrected_energies = [e - drift_correction for e in energy_states]
smoothed = [(corrected_energies[i] + corrected_energies[i-1]) / 2 for i in range(1, len(corrected_energies))]

# Key computation
equilibrium_score = calculate_equilibrium(energy_states)

print(f"Result: {equilibrium_score}")