def calculate_score(elements, factors):
    score = 0
    for i, (val, weight) in enumerate(zip(elements, factors)):
        if i % 2 == 0:
            score += val * weight ** 0.5
        else:
            score -= val // (weight + 1)
    return score

# Simulate wave interference harmonics
phases = [12, 8, 15, 6]
weights = [4, 3, 9, 2]

# Irrelevant auxiliary variables (minor distraction, intervention=5)
baseline = 10
adjustment_factor = 0.5

# Key computation
total_harmony = calculate_score(phases, weights)

# Output result
print(f"Result: {total_harmony}")