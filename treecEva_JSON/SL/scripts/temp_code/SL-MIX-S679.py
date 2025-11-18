from math import factorial
from itertools import combinations

def compute_interaction_score(marker_set):
    if len(marker_set) == 1:
        return marker_set[0] * 2
    else:
        mid = len(marker_set) // 2
        left_score = compute_interaction_score(marker_set[:mid])
        right_score = compute_interaction_score(marker_set[mid:])
        return left_score + right_score + (marker_set[0] & marker_set[-1])

genetic_markers = [3, 7, 7, 15]
subset_scores = []

for r in range(1, len(genetic_markers) + 1):
    for subset_tuple in combinations(genetic_markers, r):
        subset_list = list(subset_tuple)
        score = compute_interaction_score(subset_list)
        subset_scores.append(score)

# Normalize using variance adjustment
mean_score = sum(subset_scores) / len(subset_scores)
squared_differences = [(x - mean_score) ** 2 for x in subset_scores]
variance = sum(squared_differences) / len(subset_scores)

final_diversity_score = int(mean_score + variance)
print(f"Result: {final_diversity_score}")