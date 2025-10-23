import math
from collections import defaultdict

def calculate_hub_efficiency(weights, distances):
    if not weights or not distances:
        return 0
    avg_weight = sum(weights) / len(weights)
    total_distance = sum(distances)
    efficiency = (avg_weight * len(weights)) / (total_distance + 1)  # +1 to avoid division by zero
    return math.floor(efficiency)

def distribute_packages(hub_data):
    # Divide and conquer approach - split hubs into groups of 2
    if len(hub_data) <= 2:
        efficiencies = [
            calculate_hub_efficiency(weights, distances) 
            for weights, distances in hub_data
        ]
        return sum(efficiencies) if efficiencies else 0
    
    mid = len(hub_data) // 2
    left_result = distribute_packages(hub_data[:mid])
    right_result = distribute_packages(hub_data[mid:])
    return left_result + right_result

# Hub data: list of tuples (weights, distances)
logistics_hubs = [
    ([120, 85, 200], [50, 30, 70]),
    ([95, 110], [40, 60]),
    ([75, 130, 90, 115], [25, 80, 45, 55]),
    ([200, 150], [90, 70]),
    ([60, 80, 100], [30, 40, 50])
]

# Process hub data using divide and conquer
base_distribution_score = distribute_packages(logistics_hubs)

# Apply optimization factors using list comprehension
optimization_factors = [1.2, 0.9, 1.1, 0.95, 1.05]
hub_efficiencies = [
    calculate_hub_efficiency(weights, distances) 
    for weights, distances in logistics_hubs
]

# Calculate weighted optimization
weighted_optimization = sum(
    eff * factor 
    for eff, factor in zip(hub_efficiencies, optimization_factors)
)

# Final calculation combining base score and weighted optimization
optimized_distribution_score = math.ceil(
    (base_distribution_score * 0.7) + (weighted_optimization * 0.3)
)

print(f"Result: {optimized_distribution_score}")