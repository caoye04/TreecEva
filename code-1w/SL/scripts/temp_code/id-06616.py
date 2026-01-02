def calculate_final_score(ranks, weights):
    weighted_sum = sum([r * w for r, w in zip(ranks, weights)])
    rank_set = set(ranks)
    weight_set = set(weights)
    adjustment_factor = len(rank_set.intersection(weight_set))
    normalized_sum = weighted_sum / len(ranks)
    final_score = int(normalized_sum + adjustment_factor)
    return final_score

rank_list = [3, 1, 4, 1, 5]
base_weights = [2, 7, 1, 8, 2]

# Extraneous variable (minor distraction)
dummy_metric = sum([x**2 for x in base_weights]) // 10

final_score = calculate_final_score(rank_list, base_weights)
print(f"Result: {final_score}")