def analyze_flow_dynamics(base_sequence, modifiers):
    # Irrelevant transformation (distractor)
    transformed = [x * 1.5 + 2 for x in base_sequence]
    shifted = [abs((x - 1) % 17) for x in transformed]

    # Semi-relevant pre-processing
    adjusted = [(x + modifier % 9) for x, modifier in zip(base_sequence, modifiers)]

    # Core data used later
    flow_matrix = []
    for i, val in enumerate(adjusted):
        row = []
        for j in range(5):
            # Bitwise mixing with modular arithmetic
            mixed = (val ^ j) % 13
            if i % 2 == 0:
                mixed = (mixed + i // 2) % 11
            row.append(mixed)
        flow_matrix.append(row)

    # Dead code path - never accessed
    if len(flow_matrix) > 100:
        cleanup = [sum(r) for r in flow_matrix]
        return cleanup

    # Another distractor: combinatorics-like count with no impact
    pair_count = 0
    for a in adjusted:
        for b in adjusted:
            if (a + b) % 7 == 0 and a != b:
                pair_count += 1

    # Threshold calculation - looks important but only one value is used
    threshold_stats = {
        'min': min(adjusted),
        'max': max(adjusted),
        'range': max(adjusted) - min(adjusted),
        'pivot': (min(adjusted) + max(adjusted)) // 3  # Used later
    }

    # Unused helper array
    dummy_weights = [i * threshold_stats['pivot'] // (j + 1) 
                     for i, j in enumerate([x % 4 for x in base_sequence])]

    thresholds = [threshold_stats['pivot'] + k % 5 for k in range(5)]

    # Key call
    equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)
    return equilibrium_score


def calculate_equilibrium(matrix, thres):
    score = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            # Only entries where index parity matches contribute
            if i % 2 == j % 2:
                # Scoring rule: val mod threshold determines contribution
                t = thres[j] if thres[j] != 0 else 1
                contribution = (val % t) * ((i + 1) // 2 + 1)
                score += contribution
    # Final adjustment based on matrix dimensions
    penalty = len(matrix) * len(matrix[0]) // 7
    score -= penalty
    return score

# Input data
sequence = [8, 3, 12, 5, 7]
modifications = [6, 1, 9, 4, 2]

# Entry point
result = analyze_flow_dynamics(sequence, modifications)
equilibrium_score = result
print(f"Result: {equilibrium_score}")