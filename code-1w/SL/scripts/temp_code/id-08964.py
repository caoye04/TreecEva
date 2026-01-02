import math

# Simulated sensor array data (irrelevant initial setup)
sensor_ids = [f'SEN-{i}' for i in range(1, 17)]
activation_log = {sid: False for sid in sensor_ids}

# Irrelevant calibration constants
calibration_factor = 0.873
reference_offset = -0.042
baseline_noise = [0.012, -0.008, 0.015, -0.011]

# Real data input for processing
raw_readings = [
    [3, 1, 4, 1], [5, 9, 2, 6],
    [5, 3, 5, 8], [9, 7, 9, 3]
]

# Decoy transformation (never used)
def transform_legacy(data):
    return [[x * 1.05 + 2 for x in row] for row in data]

# Unused recursive sum function (red herring)
def recursive_sum(matrix, i=0, j=0):
    if i == len(matrix):
        return 0
    if j == len(matrix[i]):
        return recursive_sum(matrix, i+1, 0)
    return matrix[i][j] + recursive_sum(matrix, i, j+1)

# Signal processing begins
weight_matrix = [
    [1, -1, 1, -1],
    [-1, 2, -2, 1],
    [1, -2, 2, -1],
    [-1, 1, -1, 1]
]

# Apply weighted convolution filter
filtered_blocks = []
for i in range(2):
    row_block = []
    for j in range(2):
        block_sum = 0
        for di in range(2):
            for dj in range(2):
                val = raw_readings[i*2 + di][j*2 + dj]
                weight = weight_matrix[i*2 + di][j*2 + dj]
                block_sum += val * weight
        row_block.append(block_sum)
    filtered_blocks.append(row_block)

# Intermediate transformation using list comprehension (relevant)
processed_data = [
    [round(cell ** 0.5, 3) if cell > 0 else round(-(-cell) ** 0.5, 3)
     for cell in row]
    for row in filtered_blocks
]

# Dummy normalization (looks important, unused)
normalized_data = [
    [(cell - min(min(row) for row in processed_data)) / 
     (max(max(row) for row in processed_data) - min(min(row) for row in processed_data) + 1e-9)
     for cell in row]
    for row in processed_data
]

# Threshold configuration map with bit-encoded rules
threshold_map = {
    'low':  (-1.5, 1.5),
    'high': (2.0, -2.0),  # Note: intentionally inverted
    'mode': 0b1010  # Bit flags for processing logic
}

# Auxiliary diagnostic function (partially dead code)
def auxiliary_scan(data):
    count = 0
    for row in data:
        for x in row:
            if abs(x) > 1.0 and x % 1 == 0:  # Only integers
                count += 1
    return count * 0.5  # Never used result

# Main analysis function with mixed logic
def analyze_signal(grid, config):
    # Extract thresholds
    low_lim, up_lim = config['low']
    mode_flags = config['mode']
    
    # Bitwise condition check
    strict_mode = bool(mode_flags & 0b1000)
    use_abs = bool(mode_flags & 0b0010)
    
    # Accumulate values based on dynamic conditions
    accumulator = 0
    outlier_count = 0
    
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            # Conditional logic with short-circuiting
            if use_abs:
                comp_val = abs(val)
                lim_check = comp_val >= abs(low_lim)
            else:
                comp_val = val
                lim_check = (comp_val <= low_lim or comp_val >= up_lim)
            
            # Complex nested condition (core logic)
            if (i + j) % 2 == 0:
                if strict_mode:
                    if comp_val > 1.8:
                        accumulator += comp_val * 1.2
                    elif lim_check:
                        accumulator += comp_val * 0.8
                else:
                    if comp_val > 2.0:
                        accumulator += comp_val * 1.5
                    elif comp_val < -2.0:
                        accumulator += comp_val * 0.5
                    elif lim_check:
                        accumulator += comp_val * 1.1
            else:
                # Secondary path
                if comp_val > 1.0:
                    accumulator += math.log(comp_val + 1, 2) * 0.9
    
            # Outlier detection (dead-end counter)
            if abs(val) > 3.0:
                outlier_count += 1
    
    # Final adjustment with lambda-transform (relevant)
    scale_func = lambda x: x * 1.05 if x > 0 else x * 0.95
    adjusted_acc = scale_func(accumulator)
    
    # Red herring: entropy calculation (unused)
    if outlier_count > 0:
        entropy = -sum(
            (p * math.log(p, 2)) for p in [0.25, 0.25, 0.25, 0.25]
        )
    
    return round(adjusted_acc, 3)

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")