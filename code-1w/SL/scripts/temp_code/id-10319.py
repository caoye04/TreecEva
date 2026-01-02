def analyze_pattern(data, limit):
    # Track cumulative energy and phase shifts
    energy_levels = []
    total_energy = 0
    phase_shift = 0
    
    for i in range(len(data)):
        if data[i] > limit:
            total_energy += data[i] ** 0.5
            phase_shift += (i % 3) - 1
        else:
            total_energy -= data[i] * 0.1
    
        energy_levels.append(round(total_energy, 3))

    # Compute rolling window average (irrelevant to final result)
    window_size = 3
    rolling_avg = [sum(energy_levels[i:i+window_size]) / window_size 
                  for i in range(len(energy_levels) - window_size + 1)]

    # Distractor: simulate harmonic resonance (unused)
    harmonic_resonance = 0
    for val in energy_levels[::2]:
        if val > 5:
            harmonic_resonance += val * 0.05

    # Key computation: pattern stability index
    stability_index = 0
    for j in range(1, len(energy_levels)):
        if energy_levels[j] > energy_levels[j-1]:
            stability_index += 1
        elif energy_levels[j] < energy_levels[j-1]:
            stability_index -= 0.5

    # Secondary distractor: reverse slice analysis with no impact
    reversed_core = energy_levels[::-1][:len(energy_levels)//2]
    decay_rate = sum(reversed_core) / len(reversed_core) if reversed_core else 0

    # Final score based on stability and total energy
    final_score = int(stability_index + total_energy)
    return final_score

# Initialize sequence with Fibonacci-like progression
sequence = [1, 2, 3, 5, 8, 13, 21, 34]
threshold = 6

# Irrelevant transformations
transformed_seq = [x * 2 + 1 for x in sequence]
decay_mask = [0.9**i for i in range(len(sequence))]
applied_decay = [sequence[i] * decay_mask[i] for i in range(len(sequence))]

# Primary state tracker (distractor)
current_state = {"active": True, "mode": "scan", "counter": 0}
for _ in range(len(sequence) * 2):
    current_state["counter"] += 1

# Critical execution point
equilibrium_score = analyze_pattern(sequence, threshold)

# Output result
print(f"Result: {equilibrium_score}")