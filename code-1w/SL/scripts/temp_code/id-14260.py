import itertools

# Simulated sensor fusion system for environmental monitoring
base_offsets = [0.1, -0.3, 0.7, 0.2]
scaling_factors = [1.5, 0.8, 2.0, 1.1]

# Irrelevant calibration data (distractor)
calibration_log = {
    'sensor_a': {'version': '2.1', 'last_reset': '2023-05-10'},
    'sensor_b': {'version': '1.9', 'last_reset': '2023-04-22'},
    'maintenance_notes': 'No issues reported'
}

# Raw sensor inputs (simulated)
raw_readings = [
    [10, 12, 11, 13],
    [15, 14, 16, 15],
    [20, 18, 19, 21],
    [25, 27, 26, 24]
]

# Decoy function - looks important but unused
def compute_legacy_score(data):
    return sum(sum(row) for row in data) * 0.95

# Auxiliary transformation (used indirectly)
def apply_offset(value, idx):
    return value + base_offsets[idx % 4]

def apply_scaling(value, idx):
    return value * scaling_factors[idx % 4]

# Data normalization with red herring variables
normalization_counter = 0
temporary_buffer = []
invalid_flags = []  # Never actually used

processed_data = []
for i, row in enumerate(raw_readings):
    normalized_row = []
    for j, val in enumerate(row):
        # Apply compound transformation
        temp_val = apply_offset(val, i + j)
        temp_val = apply_scaling(temp_val, j - i)
        
        # Simulated noise filter (some distraction logic)
        if temp_val > 20 and j % 2 == 0:
            temp_val *= 0.9  # Minor adjustment
        elif temp_val < 10:
            temp_val += 0.5
            
        # Track side information (mostly irrelevant)
        normalization_counter += 1
        if temp_val < 0:
            invalid_flags.append((i, j))
            
        normalized_row.append(round(temp_val, 3))
    
    # Add transformed row
    processed_data.append(normalized_row)

# Dead code path - unreachable
if False:
    processed_data = [[x * 0 for x in row] for row in processed_data]

# Redundant aggregation (misleading intermediate result)
total_aggregate = 0
for row in processed_data:
    for v in row:
        total_aggregate += v

# Secondary decoy: complex but unused structure
aggregation_cube = []
for k in range(2):
    layer = []
    for i in range(2):
        layer.append([k * i + j for j in range(4)])
    aggregation_cube.append(layer)

# Core analysis function with recursive subcomponent
def recursive_smooth(data_list, depth=0):
    if depth >= 2 or len(data_list) <= 1:
        return data_list[0] if data_list else 0
    mid = len(data_list) // 2
    left = data_list[:mid] or [0]
    right = data_list[mid:] or [0]
    left_avg = sum(left) / len(left)
    right_avg = sum(right) / len(right)
    combined = [(left_avg + right_avg) / 2]
    return recursive_smooth(combined, depth + 1)

# Main diagnostic analyzer
def analyze_readings(grid):
    diagnostics = []
    
    # Use itertools to generate index combinations (real usage)
    for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
        if i == j:
            diagnostics.append(grid[i][j])
    
    # Real computation path
    base_diagnostic = sum(diagnostics)
    
    # Additional signal refinement
    refinement_key = 0
    for val in diagnostics:
        if val > 15:
            refinement_key += int(val % 4)
        else:
            refinement_key -= int(val % 3)
    
    # Final fusion
    final_component = base_diagnostic * (1 + refinement_key / 100)
    
    # Irrelevant logging
    debug_snapshot = {
        'timestamp': 'ignored',
        'diagnostics_trace': diagnostics,
        'refinement_factor': refinement_key
    }
    
    return round(final_component, 3)

# Execute main logic
temp_result = recursive_smooth([1, 2, 3])  # Side computation
final_diagnostic = analyze_readings(processed_data)

# Output the target result
print(f"Target result: {final_diagnostic}")