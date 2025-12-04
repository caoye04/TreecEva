# Task Priority Calculator for Project Management System

def analyze_task_status(task_list):
    # Some preprocessing for statistics (not directly affecting result)
    task_types = set([task.split(':')[0] for task in task_list])
    task_count_by_type = {t_type: 0 for t_type in task_types}
    
    # Track valid tasks that match our criteria
    valid_tasks = []
    invalid_count = 0
    
    # Process each task
    for task in task_list:
        parts = task.split(':')
        task_type = parts[0]
        task_status = parts[1] if len(parts) > 1 else "unknown"
        task_count_by_type[task_type] += 1
        
        # Check if task is active and relevant
        if task_status.lower() in ["active", "pending"]:
            # Tasks with 'dev' or 'test' type get priority
            if task_type.lower() in ["dev", "test"]:
                valid_tasks.append(task)
            # Tasks with 'docs' are tracked but don't affect priority
            elif task_type.lower() == "docs":
                pass
        else:
            invalid_count += 1
    
    # Calculate base metrics
    total_tasks = len(task_list)
    total_valid_tasks = len(valid_tasks)
    
    # This doesn't affect the result but adds cognitive load
    efficiency_ratio = (total_tasks - invalid_count) / total_tasks if total_tasks > 0 else 0
    complexity_score = sum([len(task) for task in valid_tasks]) / total_valid_tasks if total_valid_tasks > 0 else 0
    
    # Determine priority multiplier based on task distribution
    dev_tasks = sum(1 for task in valid_tasks if task.startswith("dev:"))
    test_tasks = sum(1 for task in valid_tasks if task.startswith("test:"))
    
    # Priority calculation logic
    if dev_tasks > test_tasks:
        priority_multiplier = 3
    elif dev_tasks < test_tasks:
        priority_multiplier = 2
    else:
        priority_multiplier = 4
    
    # Calculate final priority score
    final_priority = total_valid_tasks * priority_multiplier
    
    # Return stats dict (not used for final answer)
    return {
        "valid_tasks": total_valid_tasks,
        "priority": final_priority,
        "efficiency": round(efficiency_ratio, 2)
    }

# Task list with type:status format
tasks = [
    "dev:active",
    "test:active",
    "dev:completed",
    "docs:pending",
    "test:pending",
    "dev:active",
    "test:active",
    "docs:active"
]

# Process the tasks
results = analyze_task_status(tasks)

# Calculate some additional metrics (not affecting the answer)
active_ratio = results["valid_tasks"] / len(tasks)
performance_index = results["efficiency"] * 100

# Get the final priority from our results
final_priority = results["priority"]
print(f"Result: {final_priority}")