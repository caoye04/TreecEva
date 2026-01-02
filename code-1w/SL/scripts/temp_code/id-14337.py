def calculate_equilibrium(phases):
    # Simulate thermodynamic equilibrium calculation with distractions
    base_temperatures = [p['temp'] for p in phases]
    pressure_coefficients = [p['pressure'] * 0.02 for p in phases]
    phase_weights = [p['mass'] / 10.0 for p in phases if p['mass'] > 5]

    # Distractor: unused variable and irrelevant computation
    specific_heats = [(t + 273) * 1.005 for t in base_temperatures]  # Not used later
    entropy_proxy = sum([t ** 0.5 for t in base_temperatures if t > 0])  # Dead end

    # Real logic begins: find weighted oscillation damping
    damping_factors = []
    for i, temp in enumerate(base_temperatures):
        adjustment = 1.0
        if i > 0:
            delta = abs(temp - base_temperatures[i-1])
            adjustment = (delta / (temp + 1)) * 0.8
        damping_factors.append(adjustment)

    # Use lambda and zip together (required features)
    paired_data = list(zip(damping_factors, pressure_coefficients))
    adjusted_scores = list(map(lambda x: x[0] * 120 + x[1] * 40, paired_data))

    # Secondary distractor: complex but unused structure
    critical_thresholds = {i: val * 0.95 for i, val in enumerate(adjusted_scores)}
    trigger_events = [idx for idx, s in enumerate(adjusted_scores) if s > 50 and idx % 2 == 0]

    # Actual accumulation determining answer
    raw_sum = sum(adjusted_scores)
    penalty = len([df for df in damping_factors if df < 0.3]) * 15
    final_score = raw_sum - penalty

    # Additional red herring: conditional expression not affecting outcome
    status_flag = 'STABLE' if final_score > 100 else 'VARIABLE'
    _ = 'System ' + ('online' if status_flag == 'STABLE' else 'degraded')  # No effect

    return int(final_score)

# Experimental data setup
thermal_phases = [
    {'temp': 80, 'pressure': 120, 'mass': 8},
    {'temp': 85, 'pressure': 130, 'mass': 12},
    {'temp': 70, 'pressure': 110, 'mass': 6},
    {'temp': 65, 'pressure': 105, 'mass': 15},
    {'temp': 90, 'pressure': 140, 'mass': 10}
]

# Irrelevant pre-processing
normalization_factor = sum(p['pressure'] for p in thermal_phases) / len(thermal_phases)
scaled_masses = [p['mass'] * normalization_factor / 100 for p in thermal_phases]

# Key execution point
equilibrium_score = calculate_equilibrium(thermal_phases)

# Output result as required
print(f"Result: {equilibrium_score}")