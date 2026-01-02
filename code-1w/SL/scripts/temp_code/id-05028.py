def calculate_load_distribution(weights, threshold):
    adjusted_weights = []
    temp_offset = 0.5
    for i, val in enumerate(weights):
        if val > threshold:
            adjusted_weights.append(val * 1.1)
        else:
            adjusted_weights.append(val * 0.9)
    total_weight = sum(adjusted_weights)
    return total_weight

weights_input = [80, 120, 60, 150, 90]
threshold_limit = 100
evaluation_mode = True

result = calculate_load_distribution(weights_input, threshold_limit)
total_weight = result
print(f"Target result: {total_weight}")