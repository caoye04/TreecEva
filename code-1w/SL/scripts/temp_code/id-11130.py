def analyze_system_efficiency(states):
    base_efficiency = 0
    correction_factor = 1.0
    for i, state in enumerate(states):
        if i % 2 == 0:
            base_efficiency += sum([s % 3 for s in state if s > 0])
        else:
            temp = [s ** 0.5 for s in state if s % 2 == 1]
            correction_factor *= (sum(temp) / len(temp)) if temp else 1.0

    return base_efficiency * correction_factor


def calculate_stability_index(states):
    total_weight = 0
    stability_score = 0
    auxiliary_data = []

    for idx, (a, b) in enumerate(zip(states[::2], states[1::2])):
        diff = sum(abs(x - y) for x, y in zip(a, b))
        weight = (idx + 1) ** 2
        total_weight += weight
        
        # Distractor: irrelevant computation
        outlier_check = [x for x in a if x > 50]
        if len(outlier_check) > 2:
            adjustment = len(outlier_check) * 0.1
            stability_score -= adjustment  # Not actually impactful due to final override

        stability_score += diff * weight

    # Real computation overrides prior minor adjustments
    normalized = stability_score / total_weight if total_weight else 0
    
    # Additional distractor variables
    calibration_offset = 0.05 * len(states)
    hypothetical_max = 100 * len(states)
    energy_threshold = int(normalized * 100)  # Final key result

    # Dead code path (never executed unless states are modified)
    if False:
        fallback = sum(sum(row) for row in states) // 10
        energy_threshold = fallback

    return energy_threshold

# Simulated quantum-like state vectors (deterministic input)
quantum_states = [
    [12, 15, 23, 8],
    [10, 18, 20, 9],
    [25, 30, 35, 40],
    [24, 31, 36, 42],
    [7, 14, 21, 28],
    [6, 13, 20, 27]
]

# Irrelevant preprocessing (distractor)
sorted_pairs = [sorted(pair) for pair in zip(quantum_states, quantum_states[::-1])]
avg_first_elements = sum(sub[0][0] for sub in sorted_pairs) / len(sorted_pairs)

# Actual target computation
energy_threshold = calculate_stability_index(quantum_states)

# Print result as required
print(f"Target result: {energy_threshold}")