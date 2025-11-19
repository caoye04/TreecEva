from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

# Package data: (weight, priority)
packages = [
    (10, 60),
    (20, 100),
    (30, 120),
    (15, 80),
    (25, 90)
]

vehicle_capacity = 50
weights = [pkg[0] for pkg in packages]
values = [pkg[1] for pkg in packages]

# Dynamic programming solution
base_priority = knapsack(weights, values, vehicle_capacity)

day_of_week = 3
modular_factor = (day_of_week * 17) % 13
adjusted_priority = (base_priority + modular_factor) % 1000

# Geometry calculation for load distribution
radius = 5
area_circle = 3.14159 * radius ** 2
sector_angle = 60
sector_area = (sector_angle / 360) * area_circle

# Number theory component
numbers = [12, 18, 24]
lcm_value = reduce(lcm, numbers)

# Final score calculation
optimized_priority_score = int((adjusted_priority * sector_area) // lcm_value)

print(f"Result: {optimized_priority_score}")