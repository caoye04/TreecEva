import itertools

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.003
NOISE_FLOOR = 17
BASELINE_DRIFT = [0.1, -0.05, 0.2]

# Simulated quantum lattice parameters
dim_x, dim_y = 12, 12
lattice_state = [[(i * j + i) % 8 for j in range(dim_y)] for i in range(dim_x)]

# Irrelevant signal processing chain
def apply_filter(signal):
    return [x * 0.95 + 0.1 for x in signal if x > 3]

filtered_data = apply_filter([lattice_state[i][i] for i in range(dim_x)])
smoothed_signal = sum(filtered_data) * CALIBRATION_OFFSET  # Red herring computation

# Decoy function that appears related but is unused
def compute_entropy(matrix):
    total = 0
    for row in matrix:
        for val in row:
            if val > 0:
                total -= val * __import__('math').log(val)
    return total

# Real data: fusion reaction simulation matrix
fusion_matrix = [
    [2, 3, 5, 7, 11, 13, 17, 19],
    [1, 4, 9, 16, 25, 36, 49, 64],
    [1, 8, 27, 64, 125, 216, 343, 512],
    [0, 1, 1, 2, 3, 5, 8, 13],
    [2, 4, 8, 16, 32, 64, 128, 256],
    [3, 9, 27, 81, 243, 729, 2187, 6561],
    [1, 2, 4, 8, 16, 32, 64, 128],
    [5, 10, 15, 20, 25, 30, 35, 40]
]

# Auxiliary transformation (partially relevant, partially noise)
transformed_layers = []
for idx, layer in enumerate(fusion_matrix):
    shifted = [(x + idx) % 64 for x in layer]
    if idx % 2 == 0:
        shifted = [x * 2 for x in shifted]  # Some distortion
    transformed_layers.append(shifted)

# Dead code path - never executed but looks important
if __name__ != '__main__':
    backup_state = [row[:] for row in fusion_matrix]
    correction_factor = 1.0
    for i in range(len(backup_state)):
        for j in range(len(backup_state[i])):
            backup_state[i][j] *= correction_factor

# Core calculation: thermal integral over fusion matrix
def calculate_thermal_integral(matrix):
    accumulated = 0
    # Use itertools to generate index combinations
    for i, j in itertools.product(range(len(matrix)), range(len(matrix[0]))):
        value = matrix[i][j]
        if i == j:
            accumulated += value * 3
        elif i < j:
            accumulated += value * 2
        else:
            accumulated += value * 1
    
    # Nested conditional adjustments (critical path)
    temp_sum = 0
    for row in matrix:
        for val in row:
            if val % 2 == 0:
                temp_sum += val // 4
            else:
                temp_sum += val % 7
    
    # Final integration step
    accumulated += temp_sum // 2
    return accumulated

# Misleading intermediate diagnostic
matrix_trace = sum(fusion_matrix[i][i] for i in range(len(fusion_matrix)))
trace_diagnostic = matrix_trace * NOISE_FLOOR  # Looks important, unused later

# Key statement
thermal_capacity = calculate_thermal_integral(fusion_matrix)

# Output target result
print(f"Target result: {thermal_capacity}")