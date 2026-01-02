def process_phase_data(data, threshold):
    filtered = [x for x in data if x > threshold]
    normalized = [x / max(filtered) for x in filtered] if filtered else [0]
    return sum(normalized) * 1.5


def calculate_thermal_output(matrix, shift):
    rows = len(matrix)
    cols = len(matrix[0])
    accumulator = 0
    
    # Irrelevant preprocessing (distractor)
    temp_buffer = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            temp_buffer[i][j] = matrix[i][j] + (i * j) % 3
    
    # Actual computation path
    for i in range(rows):
        for j in range(cols):
            val = matrix[i][j]
            shifted_val = val << shift if val > 0 else val >> abs(shift)
            if shifted_val & 1:
                accumulator += (val * (i + 1)) ** 0.5
    
    # Additional irrelevant state tracking
    checksum = 0
    for row in matrix:
        for elem in row:
            checksum ^= int(elem)
    
    # Conditional expression with side relevance
    scaling_factor = 2.5 if shift > 1 else 1.8
    accumulator *= scaling_factor
    
    # Dead code path (never executed due to logic)
    if len(matrix) < 0:  # Impossible condition
        backup = process_phase_data([item for row in matrix for item in row], 0)
        accumulator = backup
    
    return int(accumulator)

# Simulated sensor readings (real input data)
energy_matrix = [
    [4, -2, 8],
    [3, 7, 1],
    [-5, 6, 9]
]
phase_shift = 2

# Misleading preliminary calculations
baseline_energy = sum(sum(row) for row in energy_matrix)
adjusted_baseline = baseline_energy * 0.75 if baseline_energy > 0 else 0
placeholder_result = process_phase_data([elem for row in energy_matrix for elem in row], 5)

# Key statement
thermal_capacity = calculate_thermal_output(energy_matrix, phase_shift)

print(f"Result: {thermal_capacity}")