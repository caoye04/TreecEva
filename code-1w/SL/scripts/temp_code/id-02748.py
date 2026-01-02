import math

# Simulate a precision agriculture grid with sensor readings (hypothetical moisture levels)
grid_data = [
    [0.45, 0.52, 0.61, 0.39, 0.72],
    [0.58, 0.63, 0.59, 0.67, 0.54],
    [0.71, 0.69, 0.73, 0.66, 0.62],
    [0.51, 0.55, 0.53, 0.57, 0.60],
    [0.49, 0.47, 0.50, 0.56, 0.58]
]

# Irrelevant baseline calibration data (distractor)
calibration_offsets = [0.01, -0.02, 0.03, -0.01, 0.02]

# Misleading transformation: looks important but unused in final calculation
def apply_noise_correction(grid):
    corrected = []
    for i, row in enumerate(grid):
        adjusted = [val + calibration_offsets[i % 5] for val in row]
        corrected.append(adjusted)
    return corrected

# Fake secondary processing path (dead code - distractor)
def compute_erosion_risk(grid):
    risk_score = 0
    for row in grid:
        for val in row:
            if val < 0.5:
                risk_score += 1.2
            elif val > 0.7:
                risk_score += 0.5
    return risk_score * 0.8

# Auxiliary function that seems relevant but is not used in main flow (decoy)
def normalize_grid(grid):
    max_val = max(max(row) for row in grid)
    return [[val / max_val for val in row] for row in grid]

# Real processing begins here — complex transformation with key logic hidden among noise

def calculate_local_gradient(row, idx):
    length = len(row)
    left = row[(idx - 1) % length]
    right = row[(idx + 1) % length]
    return abs(right - left)

# Extract edge-enhanced features using gradients (used in actual logic)
def extract_edge_features(grid):
    edges = []
    for i, row in enumerate(grid):
        edge_row = [calculate_local_gradient(row, j) for j in range(len(row))]
        edges.append(edge_row)
    return edges

# Secondary feature: curvature approximation via second difference (actually used)
def compute_curvature_profile(grid):
    profiles = []
    for row in grid:
        profile = []
        for j in range(len(row)):
            prev = row[j - 1] if j > 0 else row[-1]
            curr = row[j]
            nxt = row[j + 1] if j < len(row) - 1 else row[0]
            curvature = curr - 0.5 * (prev + nxt)  # Approximate second derivative
            profile.append(abs(curvature))
        profiles.append(profile)
    return profiles

# Weight matrix for yield estimation (domain-specific heuristic)
yield_weights = {
    'moisture_base': 85,
    'edge_factor': 12,
    'curvature_penalty': 5
}

# Main yield prediction model combining multiple derived signals
def harvest_result(field_grid):
    # Step 1: Base moisture contribution (average across all cells)
    base_values = [val for row in field_grid for val in row]
    moisture_avg = sum(base_values) / len(base_values)

    # Step 2: Compute edge features (spatial variation indicator)
    edge_map = extract_edge_features(field_grid)
    edge_contrib = sum(sum(row) for row in edge_map) * yield_weights['edge_factor']

    # Step 3: Compute curvature penalties (instability in moisture distribution)
    curvature_map = compute_curvature_profile(field_grid)
    curvature_total = sum(sum(row) for row in curvature_map)
    penalty_deduction = curvature_total * yield_weights['curvature_penalty']

    # Step 4: Aggregate contributions
    base_yield = moisture_avg * yield_weights['moisture_base']
    total_yield = base_yield + edge_contrib - penalty_deduction

    # Step 5: Apply nonlinear response curve (sigmoid-like dampening at extremes)
    dampened_yield = 100 * (1 / (1 + math.exp(-0.5 * (total_yield - 50))))

    # Step 6: Adjust for central zone bonus (middle 3x3 region gets premium)
    center_zone = [row[1:4] for row in field_grid[1:4]]  # Slice out center 3x3
    center_avg = sum(sum(row) for row in center_zone) / 9.0
    bonus = (center_avg * 15) if center_avg > 0.55 else 0

    # Final adjustment
    final = dampened_yield + bonus

    return round(final, 4)

# Unused intermediate results (distractors)
applied_correction = apply_noise_correction(grid_data)
erosion_index = compute_erosion_risk(grid_data)
normalized_data = normalize_grid(grid_data)

# Key execution point
final_yield = harvest_result(grid_data)

# Print result as required
print(f"Result: {final_yield}")