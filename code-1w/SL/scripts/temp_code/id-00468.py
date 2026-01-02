import itertools

# Simulate a complex fluid dynamics grid analysis with red herrings
def analyze_flow_regimes(velocity_field):
    regimes = []
    for i in range(len(velocity_field)):
        for j in range(len(velocity_field[i])):
            if velocity_field[i][j] > 15:
                regimes.append('turbulent')
            elif velocity_field[i][j] > 5:
                regimes.append('transitional')
            else:
                regimes.append('laminar')
    return regimes

# Misleading auxiliary function that is never called
def deprecated_pressure_gradient(grid):
    total = 0
    for row in grid:
        for val in row:
            total += abs(val) ** 0.5
    return total * 0.01  # decoy computation

# Unused helper to create confusion
def generate_combinations(n):
    return list(itertools.combinations(range(n), 2))

# Core logic masked among distractions
def compute_vorticity_influence(matrix):
    influence = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            center = matrix[i][j]
            neighbors = [
                matrix[i-1][j], matrix[i+1][j],
                matrix[i][j-1], matrix[i][j+1]
            ]
            gradient = sum(abs(center - n) for n in neighbors)
            if gradient > 10:
                influence += 1
    return influence

# Real target function buried in noise
def calculate_equilibrium(flow_matrix, thresholds):
    # Irrelevant pre-processing (distractor)
    temp_data = [row[:] for row in flow_matrix]
    normalization_factor = 0
    for row in temp_data:
        for k in range(len(row)):
            if row[k] != 0:
                normalization_factor += 1 / row[k]
    normalization_factor = max(normalization_factor, 1e-8)

    # Key transformation: apply threshold mask
    masked_values = []
    for i, row in enumerate(flow_matrix):
        for j, val in enumerate(row):
            if i % 2 == 0:
                masked_values.append(val * 0.9)
            else:
                masked_values.append(val * 1.1)

    # Summation and accumulation with filtering
    filtered_sum = 0
    for v in masked_values:
        if v > thresholds['primary']:
            filtered_sum += v * 0.7
        elif v > thresholds['secondary']:
            filtered_sum += v * 0.3

    # Secondary effect: interaction pairs (use of itertools)
    interactions = 0
    for pair in itertools.combinations(masked_values[:8], 2):  # limit to first 8
        if abs(pair[0] - pair[1]) < 5:
            interactions += 1

    # Final equilibrium formula (critical step)
    base_score = filtered_sum * 0.5
    adjustment = interactions * 2.5
    final_score = base_score - adjustment

    # Dead code path (never executed due to logic)
    if False and normalization_factor > 100:
        final_score *= 0.1

    return int(final_score)

# Main execution with decoy variables
if __name__ == '__main__':
    # Simulated sensor data grid (4x4)
    flow_matrix = [
        [12, 18, 7, 22],
        [9, 16, 5, 20],
        [11, 14, 8, 23],
        [6, 19, 4, 21]
    ]

    # Unused matrices to distract
    pressure_grid = [[v**0.5 for v in row] for row in flow_matrix]
    temperature_profile = [[v + 273 for v in row] for row in flow_matrix]

    # Threshold configuration (used in real logic)
    thresholds = {
        'primary': 15,
        'secondary': 8,
        'baseline': 5
    }

    # Spurious analysis calls (distractors)
    flow_regimes = analyze_flow_regimes(flow_matrix)
    combo_list = generate_combinations(6)

    # Critical vorticity calculation (partially relevant but not decisive)
    vorticity_impact = compute_vorticity_influence(flow_matrix)

    # --- KEY STATEMENT ---
    equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)
    
    # Output required result
    print(f"Target result: {equilibrium_score}")