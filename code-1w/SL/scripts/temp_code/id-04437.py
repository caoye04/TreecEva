def calculate_resource_allocation():
    total_nodes = 15
    utilized_nodes = 7
    node_capacity = 12
    reserved_nodes = 3

    # Calculate total and used capacity
    total_capacity = total_nodes * node_capacity
    used_capacity = utilized_nodes * node_capacity

    # Simulate resource fragmentation using set operations
    allocated_blocks = {i for i in range(0, used_capacity, 3)}
    free_blocks = {i for i in range(0, total_capacity, 3)} - allocated_blocks
    fragmented_units = len(free_blocks)

    # Reserved units based on safety policy
    reserved_units = reserved_nodes * node_capacity // 2

    # Available resources after accounting for usage and fragmentation
    available_resources = total_capacity - used_capacity + fragmented_units // 4

    # Final available capacity after reservations
    final_capacity = available_resources - reserved_units

    return final_capacity

result = calculate_resource_allocation()
print(f"Target result: {result}")