def calculate_final_score(ranks, coeffs):
    base_score = 0
    bonus = 0
    penalty = 0
    temp_result = [0] * len(ranks)

    # Irrelevant pre-processing: Normalize ranks (not used in final logic)
    normalized = {}
    total_rank = sum(ranks)
    for i, r in enumerate(ranks):
        normalized[i] = r / total_rank if total_rank != 0 else 0

    # Distractor: Simulate decay over iterations (dead computation)
    decay_factor = 1.0
    for step in range(3):
        decay_factor *= 0.95
        intermediate_decay = [r * decay_factor for r in ranks]

    # Real logic begins: Weighted scoring with enumerate and zip
    for idx, (rank, weight) in enumerate(zip(ranks, coeffs)):
        if rank < 5:
            bonus += 2
        elif rank > 20:
            penalty += 1

        temp_result[idx] = rank * weight * (idx + 1)

    base_score = sum(temp_result)

    # Additional distraction: unused sorting attempt
    sorted_pairs = sorted(enumerate(ranks), key=lambda x: x[1], reverse=True)
    displacement = 0
    for pos, (orig_idx, val) in enumerate(sorted_pairs):
        displacement += abs(pos - orig_idx)

    # Final score calculation - only this matters
    final_score = base_score + bonus - penalty
    return final_score

# Main execution
rankings = [3, 7, 12, 4, 19]
weights = [0.5, 1.0, 1.5, 0.8, 1.2]

dummy_data = {'init': 0, 'buffer': [0]*5}
for k in dummy_data:
    if k == 'buffer':
        for j, val in enumerate(dummy_data[k]):
            dummy_data[k][j] = j * 2

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")