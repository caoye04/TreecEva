def calculate_harmonic_weights(elements):
    indices = list(range(len(elements)))
    weighted_values = [i * val for i, val in enumerate(elements) if i % 2 == 0]
    harmonic_scores = [round(1 / (val + 1), 3) for val in weighted_values]
    total_harmonic_weight = sum(harmonic_scores)
    return total_harmonic_weight

items = [3, 7, 2, 8, 5, 1, 4, 6]
total_harmonic_weight = calculate_harmonic_weights(items)
print(f"Result: {total_harmonic_weight}")