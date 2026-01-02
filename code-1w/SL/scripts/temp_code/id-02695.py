def analyze_storage_efficiency(inventory_levels, threshold=50):
    overstocked = {item for item, level in inventory_levels.items() if level > threshold}
    return len(overstocked)


def detect_overlap(zones_a, zones_b):
    # Irrelevant helper: computes overlap but not used in final result
    return len(set(zones_a) & set(zones_b))


def calculate_zone_utilization(facility_map):
    # Semi-relevant computation: used to mislead about importance of layout details
    total_used = sum(len(zone) for zone in facility_map.values())
    total_slots = sum(max(zone) for zone in facility_map.values() if zone) or 1
    return round(total_used / total_slots, 4)

# Main data structures
warehouse_layout = {
    'A': [1, 3, 4, 7, 8],
    'B': [2, 3, 5, 7, 9],
    'C': [1, 2, 5, 6, 8],
    'D': [4, 5, 6, 7]
}

damaged_zones = ['B', 'D']
inventory_status = {
    'A': 67, 'B': 45, 'C': 89, 'D': 52
}

# Tracking variables (some irrelevant)
inspection_log = []
utilization_rate = calculate_zone_utilization(warehouse_layout)
inspection_log.append(('initial_scan', utilization_rate))

# Misleading intermediate calculation
overlap_count = detect_overlap(warehouse_layout['A'], warehouse_layout['C'])
inspection_log.append(('overlap_found', overlap_count))

# Core logic disguised among other operations
active_zones = set(warehouse_layout.keys()) - set(damaged_zones)

# Compute base capacity (sum of lengths of undamaged zones)
base_capacity = sum(len(warehouse_layout[zone]) for zone in active_zones)

# Adjust based on inventory thresholds (only zones above 60 are fully counted)
partial_zones = set()
for zone_id, level in inventory_status.items():
    if level < 60 and zone_id in active_zones:
        partial_zones.add(zone_id)

# Final adjustment: reduce capacity by half for underperforming zones
adjusted_loss = sum(len(warehouse_layout[z]) // 2 for z in partial_zones)
final_capacity = base_capacity - adjusted_loss

# Distractor: unused metric
efficiency_score = analyze_storage_efficiency(inventory_status, threshold=55)

# Print required result
print(f"Result: {final_capacity}")