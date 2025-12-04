def calculate_priority(tasks):
    # Calculate priority score based on task characteristics
    urgency_factor = 1.5
    complexity_sum = sum(task.get('complexity', 0) for task in tasks)
    
    # This tracking doesn't affect the result
    task_types = {}
    for task in tasks:
        category = task.get('category', 'general')
        if category in task_types:
            task_types[category] += 1
        else:
            task_types[category] = 1
    
    # Calculate weighted priority
    priority = 0
    for task in tasks:
        deadline_days = task.get('deadline_days', 30)
        importance = task.get('importance', 1)
        complexity = task.get('complexity', 1)
        
        # Experimental factor that isn't used
        effort_estimate = deadline_days * 0.8 - complexity * 1.2
        
        if deadline_days < 7:
            priority += (importance * 3) + complexity
        elif deadline_days < 14:
            priority += (importance * 2) + complexity
        else:
            priority += importance + (complexity * 0.5)
    
    return int(priority * urgency_factor)

# Task management system
tasks = [
    {'id': 1, 'name': 'Fix login bug', 'deadline_days': 3, 'importance': 4, 'complexity': 3, 'category': 'bugs'},
    {'id': 2, 'name': 'Update documentation', 'deadline_days': 10, 'importance': 2, 'complexity': 1, 'category': 'docs'},
    {'id': 3, 'name': 'Refactor API', 'deadline_days': 5, 'importance': 3, 'complexity': 4, 'category': 'development'},
    {'id': 4, 'name': 'Security audit', 'deadline_days': 7, 'importance': 5, 'complexity': 2, 'category': 'security'},
    {'id': 5, 'name': 'Performance testing', 'deadline_days': 15, 'importance': 3, 'complexity': 3, 'category': 'testing'}
]

# Filter tasks by criteria
min_importance = 3
max_complexity = 4

# These values are calculated but not used in filtering
avg_deadline = sum(task['deadline_days'] for task in tasks) / len(tasks)
most_common_category = max(set(task['category'] for task in tasks), 
                          key=lambda x: len([t for t in tasks if t['category'] == x]))

# Apply filters to tasks
filtered_tasks = [task for task in tasks if task['importance'] >= min_importance and task['complexity'] <= max_complexity]

# Calculate priority score
priority_score = calculate_priority(filtered_tasks)

# Some additional metrics that don't affect the result
total_tasks = len(tasks)
filtered_percentage = (len(filtered_tasks) / total_tasks) * 100
remaining_tasks = total_tasks - len(filtered_tasks)

print(f"Result: {priority_score}")