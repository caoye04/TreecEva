def calculate_remaining_capacity(storage_map, allocation_list):
    total_storage = sum(storage_map.values())
    reserved_space = 0
    temp_buffer = {}
    
    for key, value in storage_map.items():
        temp_buffer[key] = value * 0.1  # reserve 10% per region
        reserved_space += temp_buffer[key]
    
    allocated = 0
    priority_bonus = 0
    fallback_tracker = []
    
    for item in allocation_list:
        region = item['region']
        size = item['size']
        if region in storage_map and storage_map[region] >= size:
            allocated += size
            storage_map[region] -= size
            if item.get('priority'):
                priority_bonus += size * 0.05
        else:
            fallback_tracker.append(size)
    
    # Irrelevant aggregation
    total_fallback = sum(fallback_tracker)
    average_fallback = total_fallback / len(fallback_tracker) if fallback_tracker else 0
    
    # Distractor computation: system overhead estimation (not used)
    system_overhead = 0
    for val in storage_map.values():
        if val > 50:
            system_overhead += val * 0.02
        else:
            system_overhead += val * 0.01
    
    remaining = sum(storage_map.values())
    final_capacity = int(remaining - priority_bonus)  # Final effective capacity
    
    return final_capacity

# Setup data
storage_map = {
    'east': 200,
    'west': 150,
    'central': 180,
    'north': 90
}

allocation_list = [
    {'region': 'east', 'size': 50, 'priority': True},
    {'region': 'west', 'size': 70, 'priority': False},
    {'region': 'east', 'size': 30, 'priority': True},
    {'region': 'south', 'size': 40, 'priority': False},  # Invalid region
    {'region': 'central', 'size': 100, 'priority': False},
    {'region': 'north', 'size': 20, 'priority': True}
]

final_capacity = calculate_remaining_capacity(storage_map, allocation_list)
print(f"Result: {final_capacity}")