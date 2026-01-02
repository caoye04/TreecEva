def calculate_final_score(ranks, coeffs):
    total = 0
    offset = 3
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        adjusted_rank = rank + offset
        contribution = adjusted_rank * weight
        total += contribution
    
    bonus = 5 if sum(coeffs) > 1.5 else 0
    return total + bonus

# Competition rankings and weighting scheme
candidate_ranks = [1, 4, 2, 5]
weight_vector = [0.8, 1.2, 1.0, 0.5]

# Irrelevant distraction: unused variable
dummy_flag = len(candidate_ranks) > 3

final_score = calculate_final_score(candidate_ranks, weight_vector)
print(f"Result: {final_score}")