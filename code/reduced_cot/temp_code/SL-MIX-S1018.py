from collections import defaultdict

def calculate_loading_score(weights, priorities, capacity):
    n = len(weights)
    # Dynamic programming table for optimal priorities
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill DP table using 0-1 knapsack approach
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + priorities[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Package data: (weight, priority)
package_manifest = [
    (10, 60), (20, 100), (30, 120), 
    (15, 80), (25, 90), (5, 30)
]

# Extract weights and priorities
package_weights = [pkg[0] for pkg in package_manifest]
package_priorities = [pkg[1] for pkg in package_manifest]

# Truck capacity
max_load_capacity = 50

# Calculate optimal loading score using dynamic programming
optimal_loading_score = calculate_loading_score(package_weights, package_priorities, max_load_capacity)

# Apply greedy adjustment for high-priority packages
high_priority_bonus = sum(p for w, p in package_manifest if p > 90 and w <= max_load_capacity//3)

# Final calculation with ternary operator
final_priority_score = optimal_loading_score + (high_priority_bonus if high_priority_bonus > 0 else 0)

print(f"Result: {final_priority_score}")