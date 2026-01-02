def calculate_harmony(sequence_a, sequence_b):
    indices = list(enumerate(sequence_a))
    paired = zip(sequence_a, sequence_b)
    base_weights = [a * b for a, b in paired]
    modulated_weights = []
    for i, val in indices:
        if i % 2 == 0:
            modulated_weights.append(base_weights[i] + (val % 3))
        else:
            modulated_weights.append(base_weights[i] - (val % 3))
    total_harmony = sum(modulated_weights)
    return total_harmony

sequence_x = [4, 7, 2, 9, 5]
sequence_y = [3, 1, 8, 2, 6]
result = calculate_harmony(sequence_x, sequence_y)
total_harmony = result
print(f"Result: {total_harmony}")