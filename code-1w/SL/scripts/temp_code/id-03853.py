def analyze_fleet_efficiency(capacity_map, allocation_log):
    # Simulate fleet logistics optimization with distractors
    total_units = 0
    efficiency_tracker = {}
    temp_buffer = []

    for idx, (zone, cap) in enumerate(capacity_map.items()):
        if cap <= 0:
            continue
        scaled_cap = cap * (idx + 1)
        temp_buffer.append(scaled_cap)

        # Real computation: accumulate valid capacities
        total_units += cap

        # Distractor: irrelevant transformation
        transformed = [x ** 0.5 for x in temp_buffer if x > 10]
        efficiency_tracker[f'zone_{idx}'] = len(transformed)

    # Secondary structure: grouping allocations by region (semi-relevant)
    region_summary = {}
    for entry in allocation_log:
        region, amount = entry['region'], entry['allocated']
        if region not in region_summary:
            region_summary[region] = 0
        region_summary[region] += amount

    # Use of zip: align zone names with dummy scores (distractor)
    zone_names = list(capacity_map.keys())
    dummy_scores = [abs(hash(z)) % 100 for z in zone_names]
    for name, score in zip(zone_names, dummy_scores):
        efficiency_tracker[name] = efficiency_tracker.get(name, 0) + (score // 10)

    # Use of set operations: find unused zones (not affecting final result)
    all_zones = set(capacity_map.keys())
    active_zones = {entry['region'] for entry in allocation_log}
    unused_zones = all_zones - active_zones

    # Core logic: adjust total capacity based on utilization rate
    total_allocated = sum(entry['allocated'] for entry in allocation_log)
    utilization_rate = total_allocated / total_units if total_units else 0

    adjustment_factor = 1.0
    if utilization_rate > 0.75:
        adjustment_factor = 1.15
    elif utilization_rate < 0.3:
        adjustment_factor = 0.9

    projected_growth = total_units * adjustment_factor

    # Final calculation - this is the answer
    final_capacity = int(projected_growth - len(unused_zones) * 5)

    return final_capacity

# Input data
fleet_data = {
    'north': 40,
    'east': 35,
    'west': 20,
    'south': 50,
    'central': 60
}

allocation_records = [
    {'region': 'north', 'allocated': 25},
    {'region': 'east', 'allocated': 30},
    {'region': 'south', 'allocated': 40},
    {'region': 'north', 'allocated': 15},
    {'region': 'west', 'allocated': 5}
]

# Execute
final_capacity = analyze_fleet_efficiency(fleet_data, allocation_records)
print(f"Result: {final_capacity}")