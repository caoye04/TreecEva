def calculate_final_score(ranks, coeffs):
    base_score = 0
    temp_offset = 7  # Irrelevant variable (minimal distraction)
    for i, (rank, weight) in enumerate(zip(ranks.values(), coeffs)):
        base_score += (5 - rank) * weight
    
    bonus = 0
    if base_score > 20:
        bonus = 5
    final_score = base_score + bonus
    return final_score

# Input data
candidate_rankings = {
    'Alice': 1,
    'Bob': 3,
    'Charlie': 2,
    'Diana': 4
}

importance_weights = [2, 1, 3, 2]

final_score = calculate_final_score(candidate_rankings, importance_weights)
print(f"Result: {final_score}")