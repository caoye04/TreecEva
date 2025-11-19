from functools import reduce

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    
    return selected

# Package data
package_weights = [10, 20, 30]
package_values = [60, 100, 120]
vehicle_capacity = 50

# Strategy 1: Standard loading
strategy_one_selection = knapsack_01(package_weights, package_values, vehicle_capacity)

# Strategy 2: Priority high-value items
high_value_packages = [i for i, v in enumerate(package_values) if v >= 100]
strategy_two_selection = knapsack_01(
    [package_weights[i] for i in high_value_packages], 
    [package_values[i] for i in high_value_packages], 
    vehicle_capacity
)
strategy_two_selection = [high_value_packages[i] for i in strategy_two_selection]

# Find common packages using set operations
common_packages = set(strategy_one_selection) & frozenset(strategy_two_selection)

# Count packages that are either in common or have high value
high_value_indices = {i for i, v in enumerate(package_values) if v >= 100}
qualified_packages = common_packages | high_value_indices

# Final count using functional programming
final_selection_count = reduce(lambda acc, idx: acc + 1 if idx in qualified_packages else acc, range(len(package_weights)), 0)

print(f"Result: {final_selection_count}")