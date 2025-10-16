import math
from collections import defaultdict

# Package data: (weight, priority_factor)
packages = [(16, 2), (9, 3), (25, 1), (4, 4), (36, 2)]
truck_capacity = 30

# Initialize DP table
# dp[i][w] = maximum value achievable with first i packages and weight limit w
dp = defaultdict(lambda: defaultdict(float))

# Fill DP table
for i in range(1, len(packages) + 1):
    weight, priority = packages[i-1]
    value = math.sqrt(weight) * priority
    for w in range(truck_capacity + 1):
        # Don't take the current package
        dp[i][w] = dp[i-1][w]
        # Take the current package if it fits
        if weight <= w:
            dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)

# Find optimal load value
optimal_load_value = dp[len(packages)][truck_capacity]

# Apply a correction factor based on unused capacity
unused_capacity = truck_capacity - max(w for w in range(truck_capacity + 1) if dp[len(packages)][w] == optimal_load_value)
correction_factor = 1.0 + (unused_capacity / truck_capacity) * 0.1
optimal_load_value *= correction_factor

# Final adjustment using a lambda function
adjustment = lambda x: round(x, 2) if x % 1 != 0 else int(x)
optimal_load_value = adjustment(optimal_load_value)

print(f"Result: {optimal_load_value}")