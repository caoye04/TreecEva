import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([sum(row) for row in data]) > 1000

# Misleading auxiliary computation
electrical_load = [[(i * j + 2) % 7 for j in range(5)] for i in range(5)]
efficiency_factor = 0.87
baseline_offset = 42

# Core data structures with mixed relevance
energy_matrix = [
    [3, 1, 4, 1, 5],
    [9, 2, 6, 5, 3],
    [5, 8, 9, 7, 9],
    [3, 2, 3, 8, 4],
    [6, 2, 6, 4, 3]
]

# Threshold map derived from non-obvious logic
threshold_map = {
    i: int(math.log(v[0] + 1) * 2) for i, v in enumerate(energy_matrix) if i % 2 == 0
}

# Another irrelevant variable (distractor)
optimal_phase_angle = [math.sin(x * 0.5) for x in range(10)]

# Decoy function that looks relevant but isn't used
def compute_entropy(matrix):
    total = 0
    for row in matrix:
        for val in row:
            if val > 0:
                total -= val * math.log(val)
    return total

# Bit manipulation red herring
bit_encoded = 0
for row in energy_matrix:
    for val in row[:3]:
        bit_encoded ^= (val << 2) | (val & 3)

# Conditional dead end (never executed due to logic)
if len(optimal_phase_angle) < 5:
    baseline_offset *= 2
else:
    pass  # Placeholder to mislead control flow analysis

# Primary calculation function with nested logic
def calculate_thermal_output(matrix, thresholds):
    aggregate = 0
    modifier = 1.5
    
    # List comprehension with filtering (relevant)
    filtered_rows = [row for idx, row in enumerate(matrix) if idx in thresholds]
    
    for idx, row in enumerate(filtered_rows):
        row_sum = sum(row)
        # Non-linear adjustment based on threshold map
        adj_idx = list(thresholds.keys())[idx]
        threshold_val = thresholds[adj_idx]
        
        # Complex conditional with short-circuit (relevant)
        if threshold_val > 0 and (row_sum // threshold_val) > 2:
            aggregate += int((row_sum * modifier) / (threshold_val + 1))
        else:
            aggregate += row_sum % 5
            
        # Nested loop with bit check red herring
        temp_shift = 0
        for val in row:
            if val & 1:  # Check oddness (partially relevant)
                temp_shift += (val ^ 3) >> 1
        aggregate -= temp_shift % 7  # Minor impact but not central
    
    # Final transformation involving decoy constant
    result = aggregate * efficiency_factor + baseline_offset
    return int(result)

# Execution point of interest
thermal_capacity = calculate_thermal_output(energy_matrix, threshold_map)

# Output the target result
print(f"Target result: {thermal_capacity}")