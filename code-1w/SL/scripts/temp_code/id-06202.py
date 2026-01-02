def compute_system_allocation():
    total_nodes = 25
    active_nodes = 17
    standby_nodes = 3
    
    # Calculate available computational resources
    base_resource_pool = total_nodes * 4
    used_resources = active_nodes * 3
    reserved_resources = standby_nodes * 2
    available_resources = base_resource_pool - used_resources - reserved_resources
    
    # Track allocated tasks using set
    running_tasks = {f'task_{i}' for i in range(5)}
    failed_tasks = {f'task_{i}' for i in [1, 9, 11]}
    pending_tasks = {f'task_{i}' for i in range(5, 10)}
    
    # Determine critical reserved set based on overlap
    reserved_set = running_tasks.intersection(pending_tasks.difference(failed_tasks))
    
    # Final allocation depends on remaining capacity after reservations
    final_capacity = available_resources - len(reserved_set)
    
    return final_capacity

result = compute_system_allocation()
print(f"Result: {result}")