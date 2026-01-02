def optimize_allocation(resources, demands):
    # Preprocessing: normalize resource names and filter active ones
    normalized_keys = {k.lower().replace('_', ''): v for k, v in resources.items()}
    active_resources = {k: v for k, v in normalized_keys.items() if 'backup' not in k}

    # Misleading intermediate: calculate unused capacity (not directly used)
    total_capacity = sum(resources.values())
    reserved_capacity = sum(v for k, v in resources.items() if 'reserved' in k)
    unused_capacity = total_capacity - reserved_capacity  # red herring

    # Core logic: match demand categories to available resources
    demand_map = {d[:3].lower(): val for d, val in demands.items()}
    allocation_efficiency = []

    for key in active_resources:
        prefix = key[:3]
        if prefix in demand_map:
            allocated = min(active_resources[key], demand_map[prefix] * 1.2)
            efficiency = allocated / demand_map[prefix] if demand_map[prefix] > 0 else 0
            allocation_efficiency.append(round(efficiency, 4))

    # Use lambda to filter high-efficiency allocations
    is_efficient = lambda x: x >= 0.85
    efficient_count = len(list(filter(is_efficient, allocation_efficiency)))

    # Secondary distraction: combinatorics on possible backup configurations
    backup_options = [v for k, v in resources.items() if 'backup' in k]
    from math import comb
    config_combinations = 0
    for r in range(1, len(backup_options) + 1):
        config_combinations += comb(len(backup_options), r)  # irrelevant to final result

    # Final calculation: base capacity adjusted by efficiency rate
    base_output = sum(active_resources.values())
    efficiency_rate = efficient_count / len(allocation_efficiency) if allocation_efficiency else 0
    final_capacity = int(base_output * (0.7 + 0.3 * efficiency_rate))

    return final_capacity

# Input data setup
demand_forecast = {
    'North': 80,
    'South': 120,
    'East': 95,
    'West': 110
}

resource_pool = {
    'primary_north': 100,
    'primary_south': 130,
    'backup_east': 45,
    'primary_west': 115,
    'reserved_north': 30,
    'spare_south': 25
}

# Execution point
final_capacity = optimize_allocation(resource_pool, demand_forecast)
print(f"Result: {final_capacity}")