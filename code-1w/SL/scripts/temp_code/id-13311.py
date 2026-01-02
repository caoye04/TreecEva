def compute_weights(values, limit):
    weighted_sum = 0.0
    temp_buffer = []
    for i, val in enumerate(values):
        if val <= limit:
            weight = 1 / (i + 1) if i % 2 == 0 else 0.5 / (i + 1)
            adjusted_val = val * weight
            temp_buffer.append(adjusted_val)
            weighted_sum += adjusted_val
    return weighted_sum

factors = [12, 8, 15, 4, 20]
threshold = 10
scaling_factor = 2.0
unused_intermediate = [x ** 0.5 for x in factors if x > 5]

total_harmonic_weight = compute_weights(factors, threshold)
total_harmonic_weight *= scaling_factor

print(f"Result: {total_harmonic_weight}")