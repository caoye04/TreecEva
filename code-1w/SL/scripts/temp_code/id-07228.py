from collections import defaultdict

# Simulate warehouse inventory optimization across zones
def optimize_distribution(levels, limit):
    excess_zones = []
    deficit_zones = []
    transfer_units = 0

    # Categorize zones based on stock levels
    for zone, level in levels.items():
        if level > limit:
            excess_zones.append(level - limit)
        elif level < limit:
            deficit_zones.append(limit - level)

    # Calculate net redistribution capacity
    total_excess = sum(excess_zones)
    total_deficit = sum(deficit_zones)
    
    # Determine final system-wide capacity after reallocation
    final_capacity = min(total_excess, total_deficit) * 2  # Round-trip efficiency factor

    # Irrelevant metric: count how many zones had exact threshold match (distractor)
    exact_match_count = sum(1 for lvl in levels.values() if lvl == limit)
    
    return final_capacity

# Initialize inventory data across storage zones
inventory_levels = {
    'A': 18, 'B': 12, 'C': 25, 'D': 8, 'E': 15, 'F': 30
}
threshold = 15

# Execute optimization
final_capacity = optimize_distribution(inventory_levels, threshold)

print(f"Result: {final_capacity}")