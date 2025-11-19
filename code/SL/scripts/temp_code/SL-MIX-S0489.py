import heapq
from collections import deque

# Define blacklisted zones as a frozenset for immutable and fast lookup
blacklisted_zones = frozenset([3, 7, 11])

# Package records: (priority, zone_id)
packages_queue = [(2, 5), (4, 3), (1, 9), (5, 7), (3, 11), (6, 2)]

# Initialize max-heap using negative priorities (Python heapq is min-heap by default)
max_heap = []
for priority, zone in packages_queue:
    adjusted_priority = priority * 2 if zone in blacklisted_zones else priority
    heapq.heappush(max_heap, (-adjusted_priority, zone))

# Process packages from the heap
processed_priorities = []
while max_heap:
    neg_priority, zone = heapq.heappop(max_heap)
    current_priority = -neg_priority
    # Apply ternary-based conditional adjustment
    current_priority = current_priority + 10 if zone % 2 == 0 else current_priority - 5
    processed_priorities.append(current_priority)

# Final step: apply reduction using functional approach
final_priority = processed_priorities[0] if len(processed_priorities) <= 1 else (
    processed_priorities[0] - sum(processed_priorities[1:])
)

print(f"Result: {final_priority}")