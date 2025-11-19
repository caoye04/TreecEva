import heapq
from collections import deque
import itertools

# Package weights in kilograms
package_weights = [15, 23, 9, 31, 7]

# Priority calculation: (weight * 3 + 7) % 19
priority_queue = []
for weight in package_weights:
    priority = (weight * 3 + 7) % 19
    heapq.heappush(priority_queue, (-priority, weight))  # Max-heap using negative values

# Process packages: Select combinations of 3 packages
combinations = list(itertools.combinations(package_weights, 3))

# Calculate combination scores as sum of weights mod 13
combination_scores = [sum(combo) % 13 for combo in combinations]

# Use a min-heap to find the smallest combination score
heapq.heapify(combination_scores)
smallest_combo_score = heapq.heappop(combination_scores)

# Final checksum: (highest priority package weight + smallest combo score) * 5 - 11
_, highest_priority_weight = heapq.heappop(priority_queue)
final_checksum = (highest_priority_weight + smallest_combo_score) * 5 - 11

print(f"Result: {final_checksum}")