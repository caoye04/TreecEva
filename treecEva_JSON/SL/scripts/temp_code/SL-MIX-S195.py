import itertools

def max_non_adjacent_load(weights):
    n = len(weights)
    if n == 0:
        return 0
    elif n == 1:
        return weights[0]
    
    # Dynamic programming array
    dp = [0] * n
    dp[0] = weights[0]
    dp[1] = max(weights[0], weights[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + weights[i])
    
    return dp[-1]

# Package weights
package_weights = [2, 1, 4, 9, 3, 8, 6]

# Compute maximum non-adjacent load
base_load = max_non_adjacent_load(package_weights)

# Dictionary comprehension for adjustment factors
adjustments = {i: (0.9 if w > 5 else 1.1) for i, w in enumerate(package_weights)}

# Merge with default adjustments
default_adjustments = {i: 1.0 for i in range(len(package_weights))}
final_adjustments = {**default_adjustments, **adjustments}

# Apply adjustment using ternary operator
adjusted_load = base_load * (0.95 if len(package_weights) > 6 else 1.05)

# Final optimization
optimized_load = int(adjusted_load) if adjusted_load > 20 else int(adjusted_load) + 5

print(f"Result: {optimized_load}")