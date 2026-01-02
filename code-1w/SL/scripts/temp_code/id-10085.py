from collections import defaultdict
import math

def preprocess_readings(sensor_log):
    processed = defaultdict(float)
    for key, value in sensor_log.items():
        if value > 0:
            processed[key] = math.log(value) * 1.5
    return processed

def generate_thermal_profile(base_readings):
    profile = []
    temp_offset = 0.7
    for i in range(len(base_readings)):
        adjusted = base_readings[i] + temp_offset
        if adjusted > 3.0:
            profile.append(adjusted ** 1.2)
        else:
            profile.append(adjusted)
        temp_offset *= -0.9
    return profile

def calculate_emissions(matrix, threshold):
    flux_values = []n    cumulative_shift = 0.0
    for row in matrix:
        row_sum = sum(r for r in row if r > threshold)
        if row_sum > threshold * 2:
            flux_values.append(row_sum * 1.8)
        else:
            flux_values.append(row_sum * 0.9)
        cumulative_shift += len([x for x in row if x < threshold])
    
    # Irrelevant transformation (distractor)
    normalized_flux = [f / (max(flux_values) or 1) for f in flux_values]
    sorted_indices = sorted(range(len(flux_values)), key=lambda i: flux_values[i])
    
    # Core computation path
    total_flux = int(sum(flux_values))
    
    # Dead code branch (misleading)
    if cumulative_shift > 100:
        fallback = 0
        for idx in sorted_indices:
            fallback += normalized_flux[idx] * idx
        total_flux = int(fallback * 10)
    
    return total_flux

# Simulated sensor data
sensor_data = {'sensor_A': 4.2, 'sensor_B': 0.0, 'sensor_C': 3.8, 'sensor_D': 2.1}
processed_data = preprocess_readings(sensor_data)

# Build thermal matrix
base_sequence = [processed_data[f'sensor_{k}'] for k in 'ABCD' if f'sensor_{k}' in processed_data]
thermal_matrix = [
    [base_sequence[0], base_sequence[1]*0.5, base_sequence[2]+0.3],
    [base_sequence[1], base_sequence[2]*1.1, base_sequence[3]-0.2],
    [base_sequence[2], base_sequence[0]*0.7, base_sequence[1]+0.6]
]

# Threshold logic
activation_threshold = 2.5

# Key computation
intermediate_checksum = 0
for i, row in enumerate(thermal_matrix):
    for j, val in enumerate(row):
        intermediate_checksum += int(val * (i + 1) * (j + 1))

# Target result calculation
total_flux = calculate_emissions(thermal_matrix, activation_threshold)

# Print result
print(f"Result: {total_flux}")