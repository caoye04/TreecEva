import math

# Simulated sensor grid data (5x5) representing environmental readings
dummy_fill = [0] * 25
grid_data = [[(i + j * 5) * 1.1 for i in range(5)] for j in range(5)]

# Irrelevant backup structure (dead code)
saved_snapshot = [row[:] for row in grid_data]

# Weight matrix for sensor importance (real computation uses only diagonal)
weights = [
    [0.1, 0.05, 0.02, 0.03, 0.04],
    [0.06, 0.12, 0.01, 0.02, 0.03],
    [0.04, 0.03, 0.15, 0.02, 0.01],
    [0.02, 0.04, 0.03, 0.11, 0.02],
    [0.03, 0.02, 0.04, 0.03, 0.13]
]

# Decoy function that looks important but is never called
def compute_legacy_score(data):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            total += data[i][j] * (0.9 ** (i + j))
    return total * 0.75

# Auxiliary transformation: normalize rows (only some results used)
def normalize_rows(matrix):
    result = []
    for row in matrix:
        norm = sum(x ** 2 for x in row) ** 0.5
        result.append([x / norm for x in row])
    return result

# Unused normalization (distractor)
normalized_grid = normalize_rows(grid_data)

# Real processing begins here — extract diagonal components for weighted fusion
def extract_diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]

def apply_temperature_compensation(value, temp=22.5):
    # Simulates physical compensation curve
    return value * math.exp((temp - 25) * 0.03)

# Secondary weights (unused — red herring)
equal_weights = [1/5] * 5

# Critical diagnostic function — combines diagonal sensors with temperature model and weight scaling
def aggregate_metrics(sensor_grid, weight_matrix):
    # Step 1: Extract main diagonal readings
    core_readings = extract_diagonal(sensor_grid)  # [0.0, 6.6, 13.2, 19.8, 26.4]
    
    # Step 2: Extract diagonal weights
    diag_weights = extract_diagonal(weight_matrix)  # [0.1, 0.12, 0.15, 0.11, 0.13]
    
    # Step 3: Apply temperature compensation to each reading
    compensated = [apply_temperature_compensation(val) for val in core_readings]
    
    # Step 4: Normalize weights
    weight_sum = sum(diag_weights)
    normalized_weights = [w / weight_sum for w in diag_weights]
    
    # Step 5: Compute weighted average
    weighted_sum = sum(compensated[i] * normalized_weights[i] for i in range(5))
    
    # Step 6: Apply system calibration offset (empirically derived constant)
    calibrated = weighted_sum + 0.37
    
    # Step 7: Round to nearest hundredth (required by protocol)
    final_value = round(calibrated, 2)
    
    # Distractor calculation: harmonic mean (computed but unused)
    harmonic_mean = 0
    if all(v > 0 for v in compensated):
        harmonic_mean = 5 / sum(1/v for v in compensated)
    
    # Another distractor: transform via slicing irrelevant portion
    sliced_tail = core_readings[3:]  # [19.8, 26.4]
    fake_dependency = sum(sliced_tail) * 0.01  # Not used
    
    # Use enumerate and zip as required
    adjustment_factor = 0
    for idx, (val, w) in enumerate(zip(compensated, normalized_weights)):
        if idx % 2 == 0:
            adjustment_factor += val * w * 0.05  # Minor even-index tweak
    
    final_value += adjustment_factor
    
    return round(final_value, 2)

# Spurious data transformation (dead path)
transposed = list(zip(*grid_data))

# Fake early aggregation (never used)
temp_aggregate = 0
for r, row in enumerate(transposed):
    for c, val in enumerate(row):
        temp_aggregate += val * r * c

# List of indices for no reason (distractor)
index_tracker = [i for i in range(5) if i != 2]

# Additional decoy: bitmask simulation (irrelevant to final result)
bit_flags = 0
for i in range(5):
    bit_flags ^= int(core_readings[i] if 'core_readings' in locals() else 0) & 0xFF

# Key execution point
final_diagnostic = aggregate_metrics(grid_data, weights)

# Print result as required
print(f"Target result: {final_diagnostic}")