from collections import defaultdict

def calculate_remaining_capacity(storage, allocations):
    base_capacity = 1000
    reserved = 50
    total_used = 0

    # Initialize storage usage map with default value
    usage = defaultdict(int, storage)

    # Simulate data allocation process
    for item, size in allocations:
        if usage[item] + size <= base_capacity:
            usage[item] += size
            total_used += size

    # Extraneous calculation - not directly related to final result
    avg_usage = total_used / len(allocations) if allocations else 0

    # Determine remaining global capacity
    max_possible = base_capacity * len(storage)
    leftover = max_possible - total_used - (reserved * len(storage))

    # Final computation
    scaling_factor = 0.9
    final_capacity = int((leftover * scaling_factor) // 1)

    return final_capacity

# Setup input data
storage_map = {'node_a': 200, 'node_b': 300, 'node_c': 150}
allocation_list = [('node_a', 80), ('node_b', 120), ('node_c', 90), ('node_a', 60)]

# Execute function and print result
target_result = calculate_remaining_capacity(storage_map, allocation_list)
print(f"Result: {target_result}")