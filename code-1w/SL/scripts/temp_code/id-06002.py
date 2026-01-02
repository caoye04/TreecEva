def calculate_remaining_capacity(sets):
    base_load = 150
    peak_buffer = 0
    efficiency_sets = sets.copy()
    
    # Simulate fluctuating demand patterns (distractor: not used in final)
    for hour in range(24):
        if hour % 6 == 0:
            peak_buffer += 12
        else:
            peak_buffer -= 3
    
    # Real computation starts: capacity allocation logic
    total_capacity = 1000
    reserved_margin = total_capacity * 0.1
    available_capacity = total_capacity - reserved_margin
    
    # Distractor: unused historical tracking
    historical_loads = []
    for i in range(5):
        historical_loads.append(base_load - i * 8)
    
    # Core logic: filter and aggregate efficient zones
    valid_zones = set()
    for s in efficiency_sets:
        if len(s) >= 3:
            valid_zones.update(s)
    
    # Use set operations to eliminate overlapping inefficiencies
    critical_zones = {1, 3, 5, 7}
    optimized_zones = valid_zones - critical_zones
    
    # Accumulate usage based on zone count
    usage_accumulator = 0
    for zone in optimized_zones:
        if zone % 2 == 0:
            usage_accumulator += zone * 9
        else:
            usage_accumulator += zone * 5
    
    # Secondary distractor: unused cost simulation
    cost_per_unit = 0.05
    projected_cost = 0
    for unit in range(int(usage_accumulator)):
        if unit % 100 == 0:
            projected_cost *= 1.02
        projected_cost += cost_per_unit
    
    # Final adjustment based on optimization level
    optimization_factor = len(optimized_zones) / (len(valid_zones) + 1)
    adjusted_usage = usage_accumulator * (1 - optimization_factor)
    
    final_capacity = int(available_capacity - adjusted_usage)
    return final_capacity

# Define input
zone_set_1 = {2, 4, 6}
zone_set_2 = {4, 5, 6, 8}
zone_set_3 = {1, 2}
efficiency_sets = [zone_set_1, zone_set_2, zone_set_3]

# Execute
final_capacity = calculate_remaining_capacity(efficiency_sets)
print(f"Result: {final_capacity}")