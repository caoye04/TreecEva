def calculate_equilibrium(states):
    # Simulate thermodynamic equilibrium calculation with distractions
    total_energy = sum(states)
    normalized = [e / total_energy for e in states if e > 0]
    
    # Distractor: Entropy approximation (not used in final result)
    entropy = 0.0
    for p in normalized:
        if p > 0:
            entropy -= p * (p ** 0.5)  # Not actual entropy, misleading

    # Distractor: Unused transformation matrix
    transform = [[1.0 + i - j for j in range(3)] for i in range(3)]
    dummy_sum = sum(sum(row) for row in transform)

    # Real computation begins: find weighted index parity
    weighted_indices = []
    for i, energy in enumerate(states):
        if i % 2 == 0:
            weighted_indices.append(energy * (i + 1))
        else:
            weighted_indices.append(-energy * (i + 1))
    
    # Use dictionary to track state contributions (semi-relevant)
    contribution_map = {}
    for idx, val in enumerate(weighted_indices):
        contribution_map[f'state_{idx}'] = val * 0.1  # Scaled tracking

    # Actual answer derivation: sum of weighted indices mod 1000
    raw_score = sum(weighted_indices)
    adjusted_score = abs(raw_score) % 997
    
    # Conditional adjustment based on parity of length
    if len(states) % 2 == 1:
        adjusted_score += 13
    
    # Final equilibrium score
    return int(adjusted_score)

# Main execution
energy_states = [12, -5, 23, 8, -15, 4, 31]

# Distractor variables and computations
state_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
label_mapping = dict(zip(state_labels, enumerate(energy_states)))  # Semi-unused
offset_tracker = {i: v * 2 for i, v in enumerate(energy_states)}  # Dead code path

# Additional distraction: simulate unrelated optimization pass
for i, (label, energy) in enumerate(zip(state_labels, energy_states)):
    offset_tracker[label] = energy + (i * 0.5) - 1  # Overwrites previous, unused

# Key computational step
equilibrium_score = calculate_equilibrium(energy_states)

# Output result
print(f"Result: {equilibrium_score}")