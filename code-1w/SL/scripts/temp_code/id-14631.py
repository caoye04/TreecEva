def calculate_performance(scores):
    adjusted_scores = [max(0, s - 5) for s in scores]
    ranked = sorted(adjusted_scores, reverse=True)
    normalized_ranks = []
    for i, val in enumerate(ranked):
        if val == 0:
            continue
        normalized_ranks.append(val * (0.9 ** i))
    total_score = sum(normalized_ranks)
    return total_score

scores_input = [12, 8, 15, 3, 20, 7]
total_score = calculate_performance(scores_input)
print(f"Result: {total_score}")