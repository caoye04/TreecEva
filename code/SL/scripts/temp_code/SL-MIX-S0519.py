from collections import namedtuple
from functools import reduce
import math

class VolatilityNode:
    def __init__(self, fluctuation, next_node=None):
        self.fluctuation = fluctuation
        self.next = next_node

def compute_weighted_deviations(node, cumulative_sum=0, weights=[]):
    if not node:
        return weights
    current_weight = abs(node.fluctuation) * (0.9 ** len(weights))
    weights.append(current_weight)
    return compute_weighted_deviations(node.next, cumulative_sum + node.fluctuation, weights)

# Build linked list: 5 -> -3 -> 8 -> -2 -> 4
head = VolatilityNode(5)
head.next = VolatilityNode(-3)
head.next.next = VolatilityNode(8)
head.next.next.next = VolatilityNode(-2)
head.next.next.next.next = VolatilityNode(4)

# Process fluctuations
deviations = compute_weighted_deviations(head)

# Apply functional transformations
squared_deviations = list(map(lambda x: x**2, deviations))
filtered_deviations = list(filter(lambda x: x > 1.0, squared_deviations))

# Dynamic programming: calculate cumulative maximum
if filtered_deviations:
    dp_max = [filtered_deviations[0]]
    for i in range(1, len(filtered_deviations)):
        dp_max.append(max(dp_max[-1], filtered_deviations[i]))
else:
    dp_max = [0]

# Statistical computation
if len(dp_max) > 1:
    mean_val = sum(dp_max) / len(dp_max)
    variance = sum((x - mean_val) ** 2 for x in dp_max) / len(dp_max)
    normalized_score = math.sqrt(variance) / (mean_val + 1e-8)
else:
    normalized_score = 0

# Final adjustment using reduce
final_score = reduce(lambda acc, val: acc + val * 0.1, dp_max, normalized_score)
print(f"Result: {round(final_score, 4)}")