from itertools import compress

def optimize_distribution(inventories, thresholds):
    # Calculate utilization ratio for each warehouse
    utilization = [inv / thresh for inv, thresh in zip(inventories, thresholds.values())]
    
    # Identify underutilized warehouses
    mask = [util < 0.8 for util in utilization]
    
    # Reallocate surplus from overutilized to underutilized
    surplus = sum(inv - (thresh * 0.8) for inv, thresh in zip(inventories, thresholds.values()) if inv / thresh >= 0.8)
    base_reallocation = surplus / sum(mask) if sum(mask) > 0 else 0
    
    # Apply reallocation with priority using compress
    adjustments = list(compress([base_reallocation] * len(inventories), mask))
    adjusted_inventories = [inv + adj for inv, adj in zip(inventories, adjustments)]
    
    # Final system capacity is average of adjusted inventories
    final_capacity = sum(adjusted_inventories) / len(adjusted_inventories)
    return final_capacity

# System configuration
inventory_levels = [120, 180, 95, 210, 140]
threshold_map = {'ware_A': 150, 'ware_B': 200, 'ware_C': 120, 'ware_D': 250, 'ware_E': 160}

# Critical execution point
final_capacity = optimize_distribution(inventory_levels, threshold_map)
print(f"Result: {final_capacity}")