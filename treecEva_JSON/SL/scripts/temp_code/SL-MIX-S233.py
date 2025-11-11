import heapq
from collections import defaultdict

def compute_fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

returns_data = [0.05, -0.02, 0.03, 0.07, -0.01, 0.04, 0.06]
fib_weights = [compute_fibonacci(i+1) for i in range(len(returns_data))]

weighted_returns = [r * w for r, w in zip(returns_data, fib_weights)]

# Compute mean of weighted returns
mean_return = sum(weighted_returns) / len(weighted_returns)

# Compute variance
variance = sum((x - mean_return) ** 2 for x in weighted_returns) / len(weighted_returns)

# Hash table to store metrics
metrics = defaultdict(float)
metrics['mean'] = mean_return
metrics['variance'] = variance

# Use a max heap (negate values) to find top 3 weighted returns
heap = [-x for x in weighted_returns]
heapq.heapify(heap)
top_three_sum = sum(-heapq.heappop(heap) for _ in range(3))

# Statistical adjustment factor using a lambda
adjustment_factor = (lambda m, v, top: (m + top) / (1 + v) if v > 0 else m)(mean_return, variance, top_three_sum)

# Final portfolio score calculation
risk_free_rate = 0.01
sharpe_ratio = (adjustment_factor - risk_free_rate) / (variance ** 0.5) if variance > 0 else 0

# Apply set-based filtering for positive contributions
positive_contributions = {r for r in weighted_returns if r > 0}
filtered_mean = sum(positive_contributions) / len(positive_contributions) if positive_contributions else 0

final_score = round(sharpe_ratio * filtered_mean * 1000)
print(f"Result: {final_score}")