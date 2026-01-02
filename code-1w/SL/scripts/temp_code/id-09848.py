def optimize_distribution(stock, limit):
    excess_zones = [i for i, amount in enumerate(stock) if amount > limit]
    balanced = []
    for i, amount in enumerate(stock):
        if i in excess_zones:
            transferred = amount - limit
            balanced.append(limit + transferred // 2)
        else:
            balanced.append(amount + sum(1 for x in excess_zones if x < i))
    
    packed_data = list(zip(stock, balanced))
    adjustment_factor = sum(balanced[i] - stock[i] for i in excess_zones)
    
    # Irrelevant tracking variable (minor interference)
    log_entries = [f'Zone {i}: {change}' for i, change in enumerate(balanced)]
    
    result = sum(balanced[:len(balanced)//2]) + adjustment_factor * 0.5
    return int(result)

# Main execution
inventory_levels = [120, 180, 90, 200, 130, 85]
threshold = 150
temp_coverage = [zone for zone in inventory_levels if zone < 100]
baseline_total = sum(inventory_levels)

final_capacity = optimize_distribution(inventory_levels, threshold)
print(f"Result: {final_capacity}")