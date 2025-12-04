def calculate_task_metrics(tasks, priorities):
    # Mapping task IDs to their completion status (0=pending, 1=in-progress, 2=completed)
    task_status = {101: 0, 102: 1, 103: 2, 104: 0, 105: 2}
    
    # Calculate average completion percentage
    status_values = list(task_status.values())
    avg_completion = sum(status_values) / len(status_values) * 50
    
    # Process task urgency based on priority and status
    urgency_factors = []
    relevant_tasks = []
    
    # Combine tasks with their priorities using zip
    for i, (task, priority) in enumerate(zip(tasks, priorities)):
        # Calculate urgency factor (higher for pending tasks)
        status = task_status.get(task, 0)
        urgency = priority * (3 - status)  # 3-status gives higher weight to pending tasks
        
        # Track task processing order for debugging
        process_order = i ^ (priority & 3)  # Bitwise operations for task scheduling simulation
        urgency_factors.append(urgency)
        
        # Only consider tasks with odd-numbered priorities or status < 2
        if priority % 2 == 1 or status < 2:
            relevant_tasks.append(task)
    
    # Filter priorities based on task relevance
    filtered_priorities = []
    for i, task in enumerate(tasks):
        if task in relevant_tasks:
            # Apply a modifier based on task position
            modifier = i % 3
            filtered_priorities.append(priorities[i] + modifier)
    
    # Calculate final priority score
    priority_score = sum(filtered_priorities)
    
    # Additional metrics (not directly used in final result)
    complexity_factor = max(priorities) * min(priorities)
    weighted_avg = sum(p * (i+1) for i, p in enumerate(priorities)) / sum(priorities)
    
    print(f"Task metrics: {avg_completion:.2f}% completion, {len(relevant_tasks)} relevant tasks")
    print(f"Result: {priority_score}")
    return priority_score

# Test with sample data
tasks = [101, 103, 104, 105, 102]
priorities = [5, 2, 8, 3, 4]
result = calculate_task_metrics(tasks, priorities)
