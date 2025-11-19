from functools import reduce
from itertools import combinations

def calculate_batch_score(markers):
    if len(markers) < 2:
        return 0
    # Calculate sum of products of all unique pairs
    pair_products = [a * b for a, b in combinations(markers, 2)]
    return sum(pair_products)

def process_marker_batches(batch_list):
    scores = []
    for batch in batch_list:
        # Apply divide and conquer: split batch in half if size > 3
        if len(batch) > 3:
            mid = len(batch) // 2
            left_score = calculate_batch_score(batch[:mid])
            right_score = calculate_batch_score(batch[mid:])
            combined = left_score + right_score
            scores.append(combined)
        else:
            scores.append(calculate_batch_score(batch))
    return scores

# Genetic marker data for different patient groups
marker_batches = [
    [2, 3, 5],
    [7, 11, 13, 17],
    [19, 23],
    [29, 31, 37, 41, 43]
]

batch_scores = process_marker_batches(marker_batches)
final_score = reduce(lambda x, y: x + y if x % 2 == 0 else x * y, batch_scores, 1)
print(f"Result: {final_score}")