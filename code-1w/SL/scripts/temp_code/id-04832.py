import math

# Simulated geospatial fluid dynamics with noise filtering and equilibrium calculation
def preprocess_signals(sensor_data, calibration_factor):
    filtered = []
    noise_floor = 0.003
    for i, val in enumerate(sensor_data):
        if abs(val) < noise_floor:
            adjusted = 0.0
        else:
            adjusted = val * calibration_factor + math.sin(i % 4)
        filtered.append(round(adjusted, 6))
    return filtered

# Irrelevant helper: computes unused spectral centroid (red herring)
def compute_spectral_centroid(magnitudes):
    total_power = sum(m ** 2 for m in magnitudes)
    if total_power == 0:
        return 0.0
    return sum(i * (m ** 2) for i, m in enumerate(magnitudes)) / total_power

# Decoy function that's defined but not used in main logic
def legacy_normalization(vec):
    norm = sum(x ** 2 for x in vec) ** 0.5
    return [x / norm for x in vec] if norm != 0 else vec

# Core transformation: applies directional weighting based on gradient flow
def apply_flow_weights(grid, weights):
    result_grid = []
    for row_idx, row in enumerate(grid):
        weighted_row = []
        for col_idx, cell in enumerate(row):
            position_factor = (row_idx + 1) * (col_idx + 1)
            weight = weights[row_idx % len(weights)]
            # Apply non-linear amplification
            amplified = cell * weight * math.log(2 + position_factor)
            weighted_row.append(round(amplified, 6))
        result_grid.append(weighted_row)
    return result_grid

# Main equilibrium solver with combinatorial path analysis
def calculate_equilibrium(matrix, thresholds):
    rows, cols = len(matrix), len(matrix[0])
    
    # Step 1: Compute cumulative diagonal contributions (relevant)
    diag_sum = 0.0
    for i in range(min(rows, cols)):
        diag_sum += matrix[i][i]
    
    # Step 2: Calculate off-grid harmonics (distractor)
    harmonic_trace = 0.0
    for i in range(rows):
        for j in range(cols):
            if i != j:
                harmonic_trace += math.cos(matrix[i][j])
    
    # Step 3: Process threshold-gated interactions (critical path)
    active_couplings = 0
    coupling_energy = 0.0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if abs(val) > thresholds.get((i % 3, j % 3), 0.1):  # periodic threshold map
                active_couplings += 1
                coupling_energy += val ** 2
    
    # Step 4: Apply combinatorial correction factor based on active pairs
    if active_couplings > 0:
        combination_factor = math.factorial(min(active_couplings, 10)) // (math.factorial(max(active_couplings - 3, 1)))
    else:
        combination_factor = 1
    
    # Step 5: Integrate with secondary modulation from off-diagonals (partially relevant)
    secondary_mod = 0.0
    for i in range(rows):
        for j in range(cols):
            if i != j and i + j < rows:
                secondary_mod += matrix[i][j] * matrix[j][i]
    
    # Step 6: Final equilibrium score computation (ANSWER DEPENDS ON THIS)
    base_score = diag_sum * coupling_energy
    mod_penalty = abs(secondary_mod) * 0.1
    raw_equilibrium = base_score - mod_penalty
    
    # Final non-linear scaling
    equilibrium_score = math.tanh(raw_equilibrium / (combination_factor + 1e-6)) * combination_factor
    
    # Dead code branch: never executed due to fixed condition (distractor)
    if False and harmonic_trace > 10:
        fallback = sum(math.exp(-abs(x)) for row in matrix for x in row)
        equilibrium_score = fallback
    
    return round(equilibrium_score, 6)

# --- Simulation Setup ---

data_stream = [-0.002, 0.15, -0.001, 0.42, 0.005, -0.31, 0.000, 0.18]
sensor_grid = [
    [1.0, -0.3, 0.7],
    [0.4, 1.2, -0.6],
    [-0.2, 0.9, 1.1]
]

# Irrelevant pre-processing chain (creates distraction)
cleaned_data = preprocess_signals(data_stream, calibration_factor=1.05)
spectral_focus = compute_spectral_centroid(cleaned_data)  # Unused result

# Weighting scheme for flow transformation (some values are distractions)
flow_weights = [0.85, 1.15, 0.92, 1.08]
processed_grid = apply_flow_weights(sensor_grid, flow_weights)

# Define dynamic threshold map based on positional patterns
threshold_map = {
    (0,0): 0.15, (0,1): 0.25, (0,2): 0.1,
    (1,0): 0.3,  (1,1): 0.05, (1,2): 0.2,
    (2,0): 0.18, (2,1): 0.12, (2,2): 0.08
}

# Critical execution point
equilibrium_score = calculate_equilibrium(processed_grid, threshold_map)

# Additional red herring computations (no impact on answer)
decoy_vector = [1.0, 2.0, 1.5]
normalized_decoy = legacy_normalization(decoy_vector)
aggregate_entropy = -sum(p * math.log(abs(p)+1e-6) for p in cleaned_data if p != 0)

# Output the target result
print(f"Result: {equilibrium_score}")