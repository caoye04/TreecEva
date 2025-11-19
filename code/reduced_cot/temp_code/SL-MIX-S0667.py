import heapq
from functools import reduce

class CurrencyNode:
    def __init__(self, rate, left=None, right=None):
        self.rate = rate
        self.left = left
        self.right = right

def collect_rates_dfs(node):
    if not node:
        return []
    return [node.rate] + collect_rates_dfs(node.left) + collect_rates_dfs(node.right)

def calculate_compound_rate(rates):
    return reduce(lambda x, y: x * y if x > 0 and y > 0 else -1, rates, 1)

# Build binary tree of currency conversion rates
root = CurrencyNode(1.05)
root.left = CurrencyNode(0.98)
root.right = CurrencyNode(1.02)
root.left.left = CurrencyNode(1.01)
root.left.right = CurrencyNode(0.99)
root.right.left = CurrencyNode(1.03)
root.right.right = CurrencyNode(0.97)

# Collect all rates via DFS traversal
all_rates = collect_rates_dfs(root)

# Process through min-heap
rate_heap = all_rates[:]
heapq.heapify(rate_heap)

# Extract minimum rates and apply compound calculation
min_rates = [heapq.heappop(rate_heap) for _ in range(3)]
compound_min_rate = calculate_compound_rate(min_rates)

# Apply logical conditions for arbitrage detection
is_arbitrage_opportunity = compound_min_rate > 1.02 and all(r > 0.95 for r in min_rates)

# Calculate final gain with conditional logic
base_investment = 10000
final_arbitrage_gain = base_investment * (compound_min_rate - 1) if is_arbitrage_opportunity else 0

print(f"Result: {int(final_arbitrage_gain)}")