import heapq
from collections import defaultdict

def calculate_route_efficiency(urgencies):
    dp = [0] * (len(urgencies) + 1)
    for i in range(1, len(urgencies) + 1):
        dp[i] = max(dp[i-1], dp[i-2] + urgencies[i-1])
    return dp[len(urgencies)]

# Shipment data: (origin, urgency)
shipments = [
    ('NYC', 10),
    ('LA', 15),
    ('CHI', 7),
    ('SEA', 20),
    ('BOS', 5)
]

# Track unique origins
origins = frozenset(origin for origin, _ in shipments)

# Process urgencies with min-heap
urgency_heap = [u for _, u in shipments]
heapq.heapify(urgency_heap)

processed_urgencies = []
while urgency_heap:
    processed_urgencies.append(heapq.heappop(urgency_heap))

# Calculate efficiency score using dynamic programming
route_efficiency = calculate_route_efficiency(processed_urgencies)

# Final score combines route efficiency with origin count
final_score = route_efficiency + len(origins)
print(f'Result: {final_score}')