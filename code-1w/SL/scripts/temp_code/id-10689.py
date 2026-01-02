def calculate_final_score(ranks, coeffs):
    total = 0
    offset = 7
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        adjusted_rank = (rank + offset) % 5
        contribution = adjusted_rank * weight
        total += contribution
    return total

# Irrelevant auxiliary variable (mild distraction)
baseline = [3, 1, 4, 1, 5]

rankings = [9, 2, 5, 8, 1]
weights = [2, 3, 1, 4, 2]

final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")