def calculate_final_score(ranks, coeffs):
    total = 0
    adjustments = [0.1, -0.2, 0.3, -0.1, 0.0]
    temp_buffer = []

    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        if rank < 4:
            bonus = 5
        else:
            bonus = 0
        weighted_rank = (rank * weight + bonus)
        temp_buffer.append(weighted_rank)

    sorted_buffer = sorted(temp_buffer)
    for val in sorted_buffer:
        total += val

    return round(total, 3)

# Main data
contestant_ranks = [2, 5, 1, 4, 3]
importance_weights = [1.5, 0.8, 2.0, 1.2, 1.0]

intermediate_result = sum([x * 2 for x in importance_weights])  # Irrelevant calculation

final_score = calculate_final_score(contestant_ranks, importance_weights)
print(f"Target result: {final_score}")