import heapq
from collections import deque

def calculate_priority_depth(location_id, depth=0):
    if location_id <= 1:
        return depth + 1
    return calculate_priority_depth(location_id // 2, depth + 1) + (location_id % 3)

# Delivery requests with location IDs
requests = [24, 17, 9, 33, 12]
priority_heap = []

for idx, loc_id in enumerate(requests):
    priority = calculate_priority_depth(loc_id) * (idx + 1)
    heapq.heappush(priority_heap, (-priority, loc_id))  # Max heap using negative values

validated_scores = deque()
while priority_heap:
    neg_priority, loc = heapq.heappop(priority_heap)
    validated_scores.appendleft(-neg_priority)  # Convert back to positive

# Existing route efficiency data
route_efficiency = {loc_id: 0.75 for loc_id in [9, 12, 17]}
request_scores = {loc_id: score for score, loc_id in zip([100, 85, 95, 110, 80], requests)}

# Merge dictionaries with comprehension
final_scores = {k: v * route_efficiency.get(k, 1.0) for k, v in request_scores.items()}
sorted_final_scores = dict(sorted(final_scores.items(), key=lambda item: item[1], reverse=True))

top_priority_score = int(list(sorted_final_scores.values())[0])
print(f"Result: {top_priority_score}")