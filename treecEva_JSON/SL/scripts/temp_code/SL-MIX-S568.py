import heapq
from collections import namedtuple

delivery = namedtuple('Delivery', ['priority_score', 'delivery_id'])

# Initial delivery requests with their base scores
pending_deliveries = [
    delivery(85, 'DLV001'),
    delivery(92, 'DLV002'),
    delivery(78, 'DLV003'),
    delivery(95, 'DLV004'),
    delivery(88, 'DLV005'),
    delivery(82, 'DLV006'),
    delivery(90, 'DLV007'),
    delivery(76, 'DLV008')
]

# Convert to min-heap based on priority_score
heap = [(d.priority_score, d.delivery_id) for d in pending_deliveries]
heapq.heapify(heap)

# Apply adjustment factors using greedy approach
adjustment_factors = [1.1, 0.95, 1.05, 0.98, 1.02, 1.0, 0.99, 1.01]
adjusted_heap = []

for i, (score, delivery_id) in enumerate(heap):
    # Logical operation with short-circuit evaluation
    if score > 80 and (score % 5 == 0 or score % 3 == 0):
        adjusted_score = int(score * adjustment_factors[i])
    else:
        adjusted_score = score
    heapq.heappush(adjusted_heap, (adjusted_score, delivery_id))

# Process top 3 deliveries (remove from heap)
for _ in range(3):
    heapq.heappop(adjusted_heap)

# What is the priority score of the next delivery?
next_delivery_priority = adjusted_heap[0][0] if adjusted_heap else None
print(f"Result: {next_delivery_priority}")