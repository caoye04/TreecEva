import itertools

def calculate_thermal_output(matrix, limit):
    total_elements = len(matrix) * len(matrix[0])
    flat_stream = itertools.chain.from_iterable(matrix)
    filtered_flux = [x for x in flat_stream if x > limit]
    
    # Distractor: Energy dispersion metrics (not used in final result)
    dispersion_factor = sum([abs(a - b) for a, b in zip(filtered_flux, filtered_flux[1:])]) if len(filtered_flux) > 1 else 0
    peak_surge = max(filtered_flux) ** 0.5 if filtered_flux else 0
    decay_sequence = [x / (i + 1) for i, x in enumerate(filtered_flux)]  # unused
    
    # Core logic path
    base_integral = sum(filtered_flux)
    adjustment = 0
    for row in matrix:
        if sum(row) > limit * 2:
            adjustment += 1
    
    # Conditional expression with side relevance
    scaling_factor = 1.5 if adjustment >= 2 else (0.8 if adjustment == 1 else 1.0)
    
    # Secondary distractor block: Simulated sensor drift compensation (irrelevant)
    sensor_drift = [x * 0.98 + 0.5 for x in filtered_flux]
    normalized_drift = sum(sensor_drift) / len(sensor_drift) if sensor_drift else 0
    reference_anchor = normalized_drift * 0.1  # not used
    
    # Final computation
    thermal_capacity = int(base_integral * scaling_factor)
    return thermal_capacity

# Simulation parameters
energy_matrix = [
    [12, 45, 67, 34],
    [23, 15, 88, 91],
    [44, 52, 29, 73]
]
threshold = 40

# Execution point of interest
thermal_capacity = calculate_thermal_output(energy_matrix, threshold)

# Output result
print(f"Result: {thermal_capacity}")