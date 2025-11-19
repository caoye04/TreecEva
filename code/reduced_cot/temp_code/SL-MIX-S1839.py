import heapq
from itertools import combinations
from functools import reduce

class Package:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.urgency_score = (weight * 17 + id * 23) % 100

packages_data = [
    (101, 15),
    (102, 22),
    (103, 8),
    (104, 35),
    (105, 19)
]

packages = [Package(pid, weight) for pid, weight in packages_data]
priority_queue = []

for pkg in packages:
    heapq.heappush(priority_queue, (-pkg.urgency_score, pkg.id))

batch_combinations = list(combinations(packages, 2))
combined_scores = {}

for combo in batch_combinations:
    score_sum = sum(p.urgency_score for p in combo)
    key = tuple(sorted([p.id for p in combo]))
    combined_scores[key] = score_sum % 50

highest_batch_key = max(combined_scores, key=combined_scores.get)
highest_batch_score = combined_scores[highest_batch_key]

processed_items = 0
final_priority_score = 0

while priority_queue and processed_items < 3:
    neg_score, pkg_id = heapq.heappop(priority_queue)
    score = -neg_score
    if pkg_id in highest_batch_key:
        score += highest_batch_score
    final_priority_score = (final_priority_score * 7 + score) % 100
    processed_items += 1

print(f"Result: {final_priority_score}")