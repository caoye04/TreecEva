def calculate_compatibility(traits_a, traits_b):
    compatibility_scores = []
    for i, (a, b) in enumerate(zip(traits_a, traits_b)):
        score = (a + b) * (1 if a * b > 0 else -1)
        compatibility_scores.append(score)
    total_harmony = sum(compatibility_scores)
    return total_harmony

# Irrelevant baseline metrics (distractor variables)
baseline_avg = 7.5
sample_size = 10

traits_x = [3, -2, 5, 4]
traits_y = [1, -4, 2, -3]

result = calculate_compatibility(traits_x, traits_y)
total_harmony = result
print(f"Result: {total_harmony}")