def calculate_equilibrium(states):
    total = sum(states)
    weighted_sum = sum(i * val for i, val in enumerate(states))
    center_of_mass = weighted_sum / total if total != 0 else 0
    
    # Determine symmetry adjustment using slicing
    left_half = states[:len(states)//2]
    right_half = states[len(states)//2:]
    symmetry_score = len(left_half) - len(right_half)
    
    # Conditional expression to adjust balance based on symmetry
    harmonic_balance = center_of_mass + (symmetry_score if symmetry_score > 0 else -1 / (abs(symmetry_score) + 1))
    
    return harmonic_balance

# Define energy distribution across quantum levels (simulated data)
energy_states = [1, 4, 6, 8, 6, 4, 1]

# Irrelevant auxiliary variable (minor distraction)
dummy_marker = len(energy_states) % 2

# Key computation
harmonic_balance = calculate_equilibrium(energy_states)

print(f"Result: {harmonic_balance}")