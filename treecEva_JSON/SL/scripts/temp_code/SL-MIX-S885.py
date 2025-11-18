from collections import defaultdict

class Package:
    def __init__(self, priority, volume):
        self.priority = priority
        self.volume = volume

def optimize_deliveries(packages, capacity):
    n = len(packages)
    # dp[i][w] represents the maximum priority achievable with first i packages and weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current package fits
            if packages[i-1].volume <= w:
                # Max of including or excluding the current package
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - packages[i-1].volume] + packages[i-1].priority)
            else:
                # Can't include the current package
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Define packages with their priority scores and volumes
shipment_manifest = [
    Package(60, 10),
    Package(100, 20),
    Package(120, 30),
    Package(80, 15),
    Package(40, 5)
]

vehicle_capacity = 50
max_priority_score = optimize_deliveries(shipment_manifest, vehicle_capacity)
print(f'Result: {max_priority_score}')