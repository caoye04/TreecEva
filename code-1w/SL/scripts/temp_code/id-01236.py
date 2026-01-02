from collections import defaultdict

# Simulate warehouse inventory optimization across zones
def optimize_distribution(inventories, limit):
    excess_zones = []
    deficit_zones = []
    transfer_units = defaultdict(int)
    
    # Classify zones based on capacity threshold
    for zone, level in inventories.items():
        if level > limit:
            excess_zones.append((zone, level - limit))
        elif level < limit:
            deficit_zones.append((zone, limit - level))
    
    # Sort to prioritize largest surplus and largest deficit
    excess_zones.sort(key=lambda x: x[1], reverse=True)
    deficit_zones.sort(key=lambda x: x[1], reverse=True)
    
    # Transfer logic: match surplus to deficit as efficiently as possible
    total_transferred = 0
    i = j = 0
    while i < len(excess_zones) and j < len(deficit_zones):
        zone_surplus, available = excess_zones[i]
        zone_deficit, needed = deficit_zones[j]
        
        transfer = min(available, needed)
        transfer_units[(zone_surplus, zone_deficit)] += transfer
        total_transferred += transfer
        
        excess_zones[i] = (zone_surplus, available - transfer)
        deficit_zones[j] = (zone_deficit, needed - transfer)
        
        if excess_zones[i][1] == 0:
            i += 1
        if deficit_zones[j][1] == 0:
            j += 1

    # Compute final system-wide effective capacity
    base_sum = sum(inventories.values())
    efficiency_bonus = len([v for v in inventories.values() if v == limit]) * 0.5
    final_capacity = int(base_sum - total_transferred + efficiency_bonus)
    
    return final_capacity

# Initial inventory state per storage zone
inventory_levels = {
    'A': 18, 'B': 12, 'C': 25, 'D': 8, 'E': 17
}
threshold = 15

# Execute optimization
final_capacity = optimize_distribution(inventory_levels, threshold)
print(f"Result: {final_capacity}")