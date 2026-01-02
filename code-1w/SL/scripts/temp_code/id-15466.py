def calculate_remaining_capacity(storage, allocations):
    base_capacity = 500
    overflow_buffer = 75
    
    # Initialize total used from allocation list
    total_used = 0
    for item in allocations:
        if item in storage:
            total_used += storage[item]
    
    # Compute effective capacity with buffer logic
    raw_capacity = base_capacity - total_used
    adjusted_capacity = raw_capacity + (overflow_buffer if raw_capacity < 100 else 0)
    
    final_capacity = max(adjusted_capacity, 0)
    return final_capacity

# Simulate warehouse storage map and recent allocations
storage_map = {
    'rack_A': 120,
    'rack_B': 85,
    'rack_C': 200,
    'rack_D': 60
}

allocation_list = ['rack_A', 'rack_C', 'rack_B', 'rack_A']

# Execute calculation
final_capacity = calculate_remaining_capacity(storage_map, allocation_list)
print(f"Result: {final_capacity}")