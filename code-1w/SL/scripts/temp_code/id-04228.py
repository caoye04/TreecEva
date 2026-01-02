def calculate_remaining_capacity(storage, allocations):
    total_used = 0
    base_offset = 17
    
    for item in allocations:
        if item['name'] in storage:
            allocated_size = item['size']
            current_util = storage[item['name']] * 0.85
            total_used += min(allocated_size, current_util)
    
    raw_capacity = sum(storage.values())
    overhead = len(storage) * 2
    remaining = raw_capacity - total_used - overhead
    return int(remaining)

# System storage map (in GB)
storage_map = {
    'disk_a': 100,
    'disk_b': 200,
    'disk_c': 150
}

# Allocation requests
allocation_list = [
    {'name': 'disk_a', 'size': 80},
    {'name': 'disk_b', 'size': 180},
    {'name': 'disk_c', 'size': 100}
]

# Irrelevant auxiliary variable (minimal distraction)
temp_status = "active"

final_capacity = calculate_remaining_capacity(storage_map, allocation_list)
print(f"Result: {final_capacity}")