def evaluate_system_load():
    base_capacity = 512
    overhead = 17
    system_capacity = base_capacity - overhead

    allocations = [45, 67, 32, 89, 54]
    pending_tasks = {23, 67, 12, 45}  # Active task IDs (set for fast lookup)

    # Identify which allocations correspond to active tasks
    active_allocations = set()
    for task_id in pending_tasks:
        if task_id in allocations:
            active_allocations.add(task_id)

    used_resources_sum = sum(active_allocations)
    
    # Key computation point
    residual_capacity = system_capacity - used_resources_sum
    return residual_capacity

result = evaluate_system_load()
print(f"Result: {result}")