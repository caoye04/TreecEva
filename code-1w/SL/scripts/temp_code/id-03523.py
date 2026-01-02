def calculate_remaining_capacity(stores, limit):
    temp_loads = []
    critical_count = 0
    total_used = 0
    overflow_flags = set()

    for key, data in stores.items():
        raw_value = data['base'] * data['multiplier']
        adjusted = raw_value + data.get('offset', 0)
        temp_loads.append(adjusted)

        if adjusted > 100:
            overflow_flags.add(key)

        if adjusted > limit:
            critical_count += 1

        total_used += adjusted

    sorted_loads = sorted(temp_loads, reverse=True)
    redundancy_buffer = sum(sorted_loads[:2]) // 2

    estimated_peak = sum(temp_loads) * 1.1
    hypothetical_savings = 0

    for load in temp_loads:
        if load > 90:
            hypothetical_savings += load * 0.05

    final_utilization = total_used - hypothetical_savings
    system_efficiency = (final_utilization / estimated_peak) if estimated_peak > 0 else 0

    base_capacity = 500
    safety_margin = 75
    dynamic_adjustment = len(overflow_flags) * 10

    # Irrelevant aggregation
    stats_summary = {
        'max_temp': max(temp_loads) if temp_loads else 0,
        'min_temp': min(temp_loads) if temp_loads else 0,
        'range_temp': len([x for x in temp_loads if x > 80])
    }

    # Dead computation branch
    if critical_count > 10:
        safety_margin += 50
        stats_summary['alert_level'] = 'high'
    else:
        stats_summary['alert_level'] = 'normal'

    final_capacity = base_capacity - final_utilization + safety_margin - dynamic_adjustment

    return final_capacity

# Main execution block
storage_map = {
    'sector_A': {'base': 45, 'multiplier': 1.8, 'offset': 5},
    'sector_B': {'base': 60, 'multiplier': 1.5, 'offset': -3},
    'sector_C': {'base': 30, 'multiplier': 2.2, 'offset': 10},
    'sector_D': {'base': 50, 'multiplier': 1.9, 'offset': 0},
    'sector_E': {'base': 40, 'multiplier': 2.0, 'offset': 8}
}

initial_snapshot = storage_map.copy()
overflow_threshold = 95

# Tracking variables with no impact on result
consistency_check = len(initial_snapshot) == len(storage_map)
system_tag = "DIAG-2024"
diag_log = [f"{system_tag}: Initiated at level {len(storage_map)}"]

final_capacity = calculate_remaining_capacity(storage_map, overflow_threshold)

print(f"Result: {final_capacity}")