def manage_work_schedule():
    # Initial task sets
    all_tasks = {'meeting', 'coding', 'testing', 'documentation', 'review', 'deployment', 'planning'}
    completed_tasks = {'coding', 'testing', 'review'}
    priority_tasks = {'meeting', 'documentation', 'deployment', 'planning'}
    
    # Calculate remaining tasks
    remaining_tasks = all_tasks - completed_tasks
    
    # Create priority set (distractor - not used in final calculation)
    priority_set = set(priority_tasks)
    
    # Calculate intersection (this is the key operation)
    final_schedule = remaining_tasks & priority_set
    
    # Some intermediate calculations (distractors)
    total_tasks_count = len(all_tasks)
    completed_count = len(completed_tasks)
    percentage_complete = (completed_count / total_tasks_count) * 100
    
    # Print the result
    print(f"Result: {len(final_schedule)}")
    return len(final_schedule)

# Execute the function
result = manage_work_schedule()