import math

# Simulate environmental sensor grid with diagnostic metrics
def generate_sensor_grid(size):
    grid = [[(i + j) * 0.1 for j in range(size)] for i in range(size)]
    return grid

# Misleading auxiliary function - appears relevant but unused in final calculation
def compute_entropy(matrix):
    entropy = 0.0
    for row in matrix:
        for val in row:
            if val > 0:
                entropy -= val * math.log(val)
    return entropy

# Decoy transformation - looks sophisticated but not part of critical path
def apply_fourier_shift(data):
    shifted = []
    for i, row in enumerate(data):
        temp_row = []
        for j, x in enumerate(row):
            temp_row.append(x * math.cos(i) + (j % 3))
        shifted.append(temp_row)
    return shifted

# Auxiliary normalization that seems important but is bypassed
def normalize_rows(matrix):
    normalized = []
    for row in matrix:
        max_val = max(row)
        norm_row = [x / max_val if max_val != 0 else 0 for x in row]
        normalized.append(norm_row)
    return normalized

# Core metric processor - actually used
def extract_diagnostic_features(grid):
    feature_map = []
    for i, row in enumerate(grid):
        row_features = []
        for j, val in enumerate(row):
            # Apply non-linear response curve
            if i % 2 == 0:
                transformed = math.sin(val) * 1.5
            else:
                transformed = math.sqrt(abs(val) + 0.1) * 0.8
            # Add positional modulation
            modulated = transformed * (1 + 0.1 * (i + j))
            row_features.append(modulated)
        feature_map.append(row_features)
    return feature_map

# Weight matrix for sensor fusion - some values are red herrings
weights = [
    [0.1, 0.3, 0.2, 0.4],
    [0.4, 0.1, 0.5, 0.2],
    [0.2, 0.6, 0.1, 0.3],
    [0.3, 0.2, 0.4, 0.1]
]

# Another decoy: complex bit manipulation on float indices (never called)
def scramble_indices(indices):
    result = 0
    for idx in indices:
        result ^= int(idx * 100) << 2
        result = (result * 7) % 97
    return result

# Main aggregation logic with distractors
def aggregate_metrics(sensor_data, importance_weights):
    # Step 1: Extract non-trivial features
    processed = extract_diagnostic_features(sensor_data)
    
    # Step 2: Initialize multiple accumulators (some are distractions)
    sum_weighted = 0.0
    sum_abs = 0.0
    peak_value = -float('inf')
    entropy_proxy = 0.0
    temporal_trace = 0.0
    
    # Step 3: Process with nested dependencies and zipped iteration
    for i, (data_row, weight_row) in enumerate(zip(processed, importance_weights)):
        row_sum = 0
        for j, (val, weight) in enumerate(zip(data_row, weight_row)):
            contribution = val * weight
            sum_weighted += contribution
            sum_abs += abs(val)
            if val > peak_value:
                peak_value = val
            if contribution > 0:
                entropy_proxy -= contribution * math.log(contribution + 1e-8)
            # Temporal trace adds irrelevant accumulation
            temporal_trace += math.sin(i * j + 0.1)
    
    # Step 4: Apply corrective scaling based on system calibration
    calibration_factor = 1.85
    if sum_weighted < 0:
        calibration_factor = 2.1
    elif sum_weighted > 5:
        calibration_factor = 1.6
    else:
        calibration_factor = 1.85  # This branch is taken
    
    # Step 5: Compute secondary index that looks important but isn't final
    health_index = (sum_weighted * 0.7 + sum_abs * 0.2 + peak_value * 0.1)
    
    # Step 6: Final diagnostic uses only sum_weighted and calibration
    final_score = sum_weighted * calibration_factor
    
    # Dead code path - never reached but looks like error handling
    if math.isnan(final_score):
        fallback = 0
        for i in range(len(processed)):
            fallback += processed[i][i % len(processed[i])]
        final_score = fallback
    
    return final_score

# Unused data structure - creates visual noise
historical_snapshots = {
    'baseline': [0.1, 0.2, 0.15],
    'thresholds': {'low': 0.05, 'high': 0.8},
    'version': '2.1a'
}

# Execution flow
grid_data = generate_sensor_grid(4)

# Red herring: this seems like it should be used
entropy_measure = compute_entropy(grid_data)

# Another distraction: transform but don't use
shifted_data = apply_fourier_shift(grid_data)

# Critical statement
final_diagnostic = aggregate_metrics(grid_data, weights)

print(f"Result: {final_diagnostic}")