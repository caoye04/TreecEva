def calculate_network_load():
    weights = [12, -5, 8, 19, -22, 7, 14]
    filtered_indices = [i for i, w in enumerate(weights) if w > 0]
    scaled_values = [weights[i] * 0.5 for i in filtered_indices]
    processed = [round(v ** 2) for v in scaled_values]
    adjustment_factor = 3
    adjusted = [x - adjustment_factor for x in processed]
    optimized_weights = [x for x in adjusted if x > 0]
    total_load = sum(optimized_weights)
    return total_load

result = calculate_network_load()
print(f"Result: {result}")