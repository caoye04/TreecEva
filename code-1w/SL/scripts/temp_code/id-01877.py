def calculate_remaining_capacity(storages, allocations):
    # Track used and available space across multiple warehouses
    capacity_map = {zone: 1000 for zone in 'ABCDE'}
    used_space = {zone: 0 for zone in 'ABCDE'}
    temp_buffer = []

    # Simulate redundant preprocessing (distractor)
    for item in allocations:
        item_size = len(item['name']) * item['count']
        category_key = item['type'][0].upper()
        if category_key in capacity_map:
            temp_buffer.append((category_key, item_size))

    # Actual allocation logic with interference from unused paths
    transfer_log = []  # logged but not used
    overflow_flags = set()
    safety_margin = 50

    for alloc in allocations:
        zone = alloc['zone']
        size = alloc['size']
        priority = alloc.get('priority', 1)

        # Red herring computation: priority adjustment (not actually affecting result)
        adjusted_priority = priority + (len(alloc['name']) % 3)
        dummy_score = adjusted_priority * size

        if zone in storages:
            projected = used_space[zone] + size
            if projected <= capacity_map[zone] - safety_margin:
                used_space[zone] += size
                transfer_log.append(f"Transferred {size} to {zone}")
            else:
                overflow_flags.add(zone)

    # Secondary processing with set operations (relevant)
    available_zones = set(capacity_map.keys())
    occupied_zones = set(used_space.keys())
    active_zones = occupied_zones.intersection(available_zones)

    # Compute final remaining capacity using dictionary reduction
    total_remaining = 0
    for z in active_zones:
        free = capacity_map[z] - used_space[z]
        total_remaining += max(free, 0)

    # Distractor: complex sorting of irrelevant data
    sorted_buffer = sorted(temp_buffer, key=lambda x: (x[1], x[0]))
    cumulative_shift = 0
    for i, (k, v) in enumerate(sorted_buffer):
        cumulative_shift += (v % (i + 1)) if i + 1 != 0 else 0

    # Final calculation (answer depends only on actual usage)
    final_capacity = total_remaining - safety_margin * len(overflow_flags)

    # Print required output
    print(f"Result: {final_capacity}")
    return final_capacity

# Setup inputs
storage_map = {'A': 1000, 'B': 1000, 'C': 1000, 'D': 1000, 'E': 1000}
allocation_list = [
    {'name': 'widget_alpha', 'zone': 'A', 'size': 120, 'count': 3, 'type': 'mechanical'},
    {'name': 'gasket_large', 'zone': 'B', 'size': 85, 'count': 4, 'type': 'sealant'},
    {'name': 'valve_core', 'zone': 'A', 'size': 200, 'count': 2, 'type': 'plumbing'},
    {'name': 'cable_harness', 'zone': 'C', 'size': 310, 'count': 1, 'type': 'electrical'},
    {'name': 'sensor_unit', 'zone': 'D', 'size': 95, 'count': 5, 'type': 'diagnostic'},
    {'name': 'pump_assembly', 'zone': 'A', 'size': 350, 'count': 1, 'type': 'hydraulic'}
]

# Execute function
final_capacity = calculate_remaining_capacity(storage_map, allocation_list)