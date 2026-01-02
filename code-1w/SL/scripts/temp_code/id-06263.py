import math

# System calibration parameters (mostly irrelevant)
calibration_sequence = [0.1, 0.3, 0.5, 0.9, 1.2]
baseline_threshold = sum([math.log(x + 1) for x in calibration_sequence])
reference_frame = {'x': 128, 'y': 256, 'z': 512}

# Real-time sensor inputs (some useful, some not)
sensor_readings = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# Irrelevant signal processing chain
temporal_weights = []
for i, reading in enumerate(sensor_readings):
    weight = (i + 1) * 0.25
    if weight > 1.0:
        weight = 1.0
    temporal_weights.append(weight)

# Decoy transformation - looks important but unused later
transformed_grid = []
for row in sensor_readings:
    transformed_row = []
    for val in row:
        transformed_row.append((val + 1) ** 2 % 3)
    transformed_grid.append(transformed_row)

# Actual relevant data: pattern masks
def generate_pattern_mask(size):
    mask = []
    for i in range(size):
        mask.append([1 if (i + j) % 2 == 0 else 0 for j in range(size)])
    return mask

generated_mask = generate_pattern_mask(4)

# Bit manipulation red herring
effective_flags = 0
for i in range(len(sensor_readings)):
    flag_val = 1 << i
    if i % 3 == 0:
        effective_flags |= flag_val

# Set-based interference
duplicate_indices = set()
all_positions = set()
for i, row in enumerate(sensor_readings):
    for j, val in enumerate(row):
        pos_key = (i, j)
        if pos_key in all_positions:
            duplicate_indices.add(j)
        all_positions.add(pos_key)

# Core logic hidden among noise
phase_offset = 0
for idx, (reading, mask_row) in enumerate(zip(sensor_readings, generated_mask)):
    match_count = 0
    for r_val, m_val in zip(reading, mask_row):
        if r_val == m_val:
            match_count += 1
    if match_count >= 2:
        phase_offset += idx * match_count

# Unused recursive distraction
def compute_depth_score(data, depth=0):
    if depth >= 3 or not data:
        return depth
    return compute_depth_score(data[1:], depth + 1)

_ = compute_depth_score(calibration_sequence, 0)

# Real computation buried in middle
grid_patterns = []
for i, row in enumerate(sensor_readings):
    pattern = []
    for j, val in enumerate(row):
        # Apply bitwise decoy that doesn't affect final result
        bit_shifted = (val ^ 1) << 1
        restored = (bit_shifted >> 1) ^ 1
        pattern.append(restored and generated_mask[i][j])
    grid_patterns.append(pattern)

# Final aggregation with multiple layers of logic
running_diagnostics = []
for i, (grid_row, gen_row) in enumerate(zip(grid_patterns, generated_mask)):
    score = 0
    for g_val, gen_val in zip(grid_row, gen_row):
        if g_val == gen_val:
            score += 3
        elif g_val > gen_val:
            score += 1
        else:
            score -= 2
    # Only every even index contributes to real path
    if i % 2 == 0:
        running_diagnostics.append(score + phase_offset)

# Critical statement — answer depends on this
final_diagnostic = aggregate_metrics(grid_patterns, phase_offset)

# True implementation hidden from immediate view
def aggregate_metrics(grids, offset):
    total = 0
    for i, row in enumerate(grids):
        row_sum = sum(row)
        if i % 2 == 1:
            total += row_sum * 2
        else:
            total += row_sum - offset // 4
    # Inject deterministic but non-obvious adjustment
    adjustment = len(grids) * (offset % 5)
    return int(total + adjustment)

# Print result as required
print(f"Target result: {final_diagnostic}")