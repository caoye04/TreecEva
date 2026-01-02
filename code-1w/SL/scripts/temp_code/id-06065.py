def compute_weights(values, weights):
    weighted_sum = 0
    harmonic_factor = 0
    
    for i, (val, w) in enumerate(zip(values, weights)):
        if val > 0:
            weighted_sum += w / val
            harmonic_factor += 1 / val
    
    if harmonic_factor == 0:
        return 0
    
    total_harmonic_weight = weighted_sum / harmonic_factor
    return total_harmonic_weight

# Input data
dataset_a = [4, 8, 12, 0, 16]
scaling_factors = [2, 4, 6, 8, 10]

# Unused distractor variables
temp_buffer = [0] * len(dataset_a)
max_value = max(dataset_a)

# Computation
total_harmonic_weight = compute_weights(dataset_a, scaling_factors)

print(f"Result: {total_harmonic_weight}")