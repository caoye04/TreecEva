def calculate_equilibrium(states, limit):
    # Initialize tracking variables
    active_regions = set()
    suppressed_regions = set(range(len(states)))
    temp_buffer = [0] * len(states)
    equilibrium_score = 0
    decay_factor = 0.85
    growth_factor = 1.15

    # Precompute derived state metrics (some are distractions)
    max_state = max(states)
    min_state = min(states)
    state_range = max_state - min_state + 1e-9
    normalized_states = [(s - min_state) / state_range for s in states]

    # Simulate region activation cycles
    for cycle in range(3):
        for i, power in enumerate(states):
            if power > limit * (decay_factor ** cycle):
                active_regions.add(i)
                suppressed_regions.discard(i)
            else:
                temp_buffer[i] += 1

    # Secondary adjustment using conditional expression
    adjustment = sum([1 if i in active_regions else -1 for i in range(len(states))])
    adjustment = adjustment if adjustment > 0 else 0

    # Compute contribution from oscillating margins
    margin_flux = 0
    for i in range(len(states) - 1):
        margin_flux += abs(states[i] - states[i + 1])

    # Core equilibrium formula (depends only on active_regions and adjustment)
    base_score = len(active_regions) * 100
    bonus = adjustment * 10
    equilibrium_score = base_score + bonus

    # Dead code path - never executed but looks relevant
    if False:
        for i in range(len(temp_buffer)):
            temp_buffer[i] *= growth_factor
        equilibrium_score -= sum(temp_buffer)

    # Irrelevant metric calculation
    theoretical_capacity = sum(normalized_states) * len(states)
    efficiency_ratio = (equilibrium_score / 1000) / (theoretical_capacity + 1e-9)

    return equilibrium_score

# Main execution context
energy_states = [12, 45, 23, 67, 34, 89, 11, 73]
threshold = 30
equilibrium_score = calculate_equilibrium(energy_states, threshold)
print(f"Result: {equilibrium_score}")