import heapq
from functools import reduce

def calculate_route_efficiency(scores):
    # Using dynamic programming to calculate maximum efficiency
    n = len(scores)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = scores[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + scores[i-1])
    return dp[n]

# Initial priority queue of route efficiency scores
route_scores = [15, 10, 18, 9, 22, 12, 17]
heap = route_scores[:]
heapq.heapify(heap)

# Update scores with new values
updates = [3, -2, 7, 1]
for update in updates:
    if heap:
        current = heapq.heappop(heap)
        heapq.heappush(heap, current + update)

# Extract final scores from heap
final_scores = []
while heap:
    final_scores.append(heapq.heappop(heap))

# Apply dynamic programming to optimize route efficiency
optimized_efficiency = calculate_route_efficiency(final_scores)

# Apply a lambda-based transformation to adjust for fuel costs
adjustment_factor = lambda x: x * 0.95 if x > 20 else x * 1.05
adjusted_scores = list(map(adjustment_factor, final_scores))

# Combine adjusted scores using reduce
combined_score = reduce(lambda a, b: a + b, adjusted_scores, 0)

# Final efficiency is the max of optimized and combined scores
final_efficiency = max(optimized_efficiency, combined_score)
print(f"Result: {optimized_efficiency}")