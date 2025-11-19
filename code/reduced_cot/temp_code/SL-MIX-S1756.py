import heapq

deliveries = [
    (3, 10),  # (urgency, distance)
    (1, 15),
    (2, 5),
    (1, 8),
    (3, 2),
    (2, 12),
    (1, 20)
]

# Create heap with tuples (urgency, distance)
heap = []
for item in deliveries:
    heapq.heappush(heap, (item[0], item[1]))

processed_distance = 0
for _ in range(3):
    if heap:
        urgency, dist = heapq.heappop(heap)
        processed_distance += dist
    else:
        break

print(f"Result: {processed_distance}")