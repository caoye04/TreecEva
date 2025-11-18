from heapq import heappush, heappop
from functools import reduce

def calculate_efficiency(weights, distances):
    scores = []
    for i in range(len(weights)):
        base_score = (weights[i] * 3 + distances[i] * 2) % 7
        if base_score == 0:
            return 0  # Early exit for optimal case
        heappush(scores, -base_score)  # Max heap using negative values
    
    top_scores = []
    while scores and len(top_scores) < 3:
        top_scores.append(-heappop(scores))
    
    adjusted_sum = sum(map(lambda x: x + 5 if x % 2 == 0 else x - 3, top_scores))
    return adjusted_sum

package_weights = [4, 7, 2, 9, 5]
delivery_distances = [10, 3, 8, 6, 1]

final_score = calculate_efficiency(package_weights, delivery_distances)
print(f'Result: {final_score}')