def calculate_remaining_capacity(storage_map, allocation_list):
    total_capacity = sum(storage_map.values())
    reserved_space = 0
    temp_buffer = []

    # Simulate pre-allocation checks (distractor: not all are used)
    for key in storage_map:
        if len(key) % 2 == 0:
            temp_buffer.append(storage_map[key] * 0.1)

    # Actual allocation logic
    allocated = 0
    for item in allocation_list:
        node, size = item['node'], item['size']
        if node in storage_map and storage_map[node] >= size:
            allocated += size
            storage_map[node] -= size  # in-place update

    # Secondary validation pass (semi-relevant)
    available_nodes = {k: v for k, v in storage_map.items() if v > 0}
    fragmentation_score = len(available_nodes) / (len(storage_map) + 1e-5)

    # Red herring computation
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    projected_growth = allocated * 1.2 + avg_temp

    # Core result
    remaining = total_capacity - allocated

    # Final adjustment based on policy
    maintenance_reserve = 0.05 * total_capacity
    final_capacity = remaining - maintenance_reserve

    return int(final_capacity)

# Setup data
storage_map = {
    'server_alpha': 2000,
    'server_beta': 1500,
    'server_gamma': 3000,
    'server_delta': 1000
}

allocation_list = [
    {'node': 'server_alpha', 'size': 500},
    {'node': 'server_beta', 'size': 750},
    {'node': 'server_gamma', 'size': 1200},
    {'node': 'server_alpha', 'size': 300},
    {'node': 'server_delta', 'size': 900}
]

# Execution point
final_capacity = calculate_remaining_capacity(storage_map, allocation_list)
print(f"Target result: {final_capacity}")