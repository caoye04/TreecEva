import math
from collections import defaultdict

def calculate_priority(package_id, weight, distance):
    base_score = (weight << 2) & 0xFF
    adjustment = int(math.log(distance + 1) * 10)
    return base_score ^ adjustment

def get_optimal_loading_score(packages):
    n = len(packages)
    if n == 0:
        return 0
    
    dp = [0] * (n + 1)
    dp[1] = packages[0][2]
    
    for i in range(2, n + 1):
        current_package = packages[i-1]
        priority = calculate_priority(current_package[0], current_package[1], current_package[2])
        dp[i] = max(dp[i-1], dp[i-2] + priority)
        if i > 3 and priority < 50:
            break
    
    return dp[n]

# Package data: (package_id, weight, distance)
shipment_manifest = [
    ('PKG001', 12, 150),
    ('PKG002', 8, 200),
    ('PKG003', 15, 90),
    ('PKG004', 5, 300),
    ('PKG005', 10, 120)
]

# Precompute priorities
for i in range(len(shipment_manifest)):
    pkg = shipment_manifest[i]
    priority = calculate_priority(pkg[0], pkg[1], pkg[2])
    shipment_manifest[i] = (pkg[0], pkg[1], priority)

optimal_loading_score = get_optimal_loading_score(shipment_manifest)
print(f"Result: {optimal_loading_score}")