def calculate_equilibrium(states):
    # Lambda to compute adjusted energy level
    adjust_energy = lambda e, t: e * (1 + 0.1 * t) if t > 0 else e

    total_weight = 0.0
    active_count = 0
    equilibrium_contributions = []

    # Misleading initialization - not used in final calculation
    dummy_reference = [0] * len(states)
    temp_accumulator = 0

    for idx, state in enumerate(states):
        energy = state['energy']
        temperature = state['temp']
        phase_flag = state['phase']

        # Irrelevant computation - simulates tracking but unused
        temp_accumulator += energy % (idx + 1) if idx % 2 == 0 else 0

        adjusted_energy = adjust_energy(energy, temperature)

        # Only consider gaseous states for equilibrium
        if phase_flag == 'gas':
            weight = adjusted_energy / (temperature + 10)
            total_weight += weight
            equilibrium_contributions.append(weight)
            active_count += 1

    # Distractor loop: computes average deviation but not used
    avg_contribution = total_weight / active_count if active_count > 0 else 0
    deviation_sum = 0
    for cont in equilibrium_contributions:
        deviation_sum += (cont - avg_contribution) ** 2

    # Real logic: equilibrium score is sum of contributions scaled by active count
    scaling_factor = active_count ** 0.5 if active_count > 0 else 0
    equilibrium_score = total_weight * scaling_factor

    return equilibrium_score


# Initialize thermodynamic states
thermodynamic_states = [
    {'energy': 120, 'temp': 25, 'phase': 'liquid'},
    {'energy': 200, 'temp': 30, 'phase': 'gas'},
    {'energy': 180, 'temp': 40, 'phase': 'gas'},
    {'energy': 95, 'temp': 15, 'phase': 'solid'},
    {'energy': 250, 'temp': 35, 'phase': 'gas'}
]

# Tracking variables with no impact
state_labels = ['A', 'B', 'C', 'D', 'E']
label_map = {k: v for k, v in zip(state_labels, range(len(state_labels)))}

# Key execution point
equilibrium_score = calculate_equilibrium(thermodynamic_states)

print(f"Result: {equilibrium_score}")