from collections import defaultdict
import itertools

def preprocess_fluid_data(data):
    # Irrelevant preprocessing step with distractor logic
    stats = defaultdict(int)
    for val in data:
        stats['count'] += 1
        stats['sum'] += val
    avg = stats['sum'] / stats['count'] if stats['count'] > 0 else 0
    adjusted = [x - avg for x in data]
    return adjusted

def validate_matrix(matrix):
    # Semi-relevant validation that doesn't alter output but adds cognitive load
    if not matrix:
        return False
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True

def calculate_thermal_capacity(matrix, profile):
    n = len(matrix)
    capacity = 0
    temp_offset = sum(profile) / len(profile) if profile else 0
    
    # Distractor: tracking unused state
    max_flux = 0
    flux_count = 0
    
    for i, j in itertools.product(range(n), range(n)):
        if i == j:
            continue  # Skip diagonal
        diff = abs(matrix[i][j] - matrix[j][i])
        directional_bias = diff * (1 + (profile[(i + j) % len(profile)] / 100))
        capacity += directional_bias
        
        # Dead computation branch - never used
        flux_count += 1
        if diff > max_flux:
            max_flux = diff
    
    # Key transformation
    scaling_factor = 0.87
    capacity *= scaling_factor
    
    # Additional red herring calculation
    dummy_sum = 0
    for k in range(len(profile)):
        dummy_sum += profile[k] * profile[k]
    
    # Final adjustment based on valid logic chain
    if capacity > 100:
        capacity *= 0.95
    
    return int(capacity)

# Main execution block
fluid_matrix = [
    [4, 8, 3],
    [2, 5, 9],
    [7, 1, 6]
]

temperature_profile = [20, 35, 25, 40]

# Irrelevant preprocessing call
normalized_profile = preprocess_fluid_data(temperature_profile)

# Validation that does nothing consequential
is_valid = validate_matrix(fluid_matrix)

# State tracking with no impact
iteration_log = []
for step in range(2):
    iteration_log.append(f"Step {step}")

# Core assignment - target execution point
termal_capacity = calculate_thermal_capacity(fluid_matrix, temperature_profile)

# Typo in variable name is intentional distractor; correct one is printed
thermal_capacity = calculate_thermal_capacity(fluid_matrix, temperature_profile)

print(f"Result: {thermal_capacity}")