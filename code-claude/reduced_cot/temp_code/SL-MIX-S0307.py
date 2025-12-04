import itertools

def calculate_priority(tasks):
    # Calculate priority score based on task characteristics
    if not tasks:
        return 0
    
    # Extract important task features
    urgency = sum(task['urgency'] for task in tasks)
    complexity = max(task['complexity'] for task in tasks)
    
    # Calculate priority metrics (only complexity is actually used)
    avg_urgency = urgency / len(tasks)
    max_complexity = complexity
    
    # This variable tracks dependencies but isn't used in final calculation
    dependency_count = sum(len(task.get('dependencies', [])) for task in tasks)
    
    # Calculate final score - only uses complexity
    return max_complexity * 10

# Task management system data
tasks = [
    {'id': 'T1', 'name': 'Database backup', 'urgency': 4, 'complexity': 3, 'dependencies': ['T5']},
    {'id': 'T2', 'name': 'Security audit', 'urgency': 5, 'complexity': 8, 'dependencies': []},
    {'id': 'T3', 'name': 'Code review', 'urgency': 3, 'complexity': 5, 'dependencies': ['T4']},
    {'id': 'T4', 'name': 'API testing', 'urgency': 2, 'complexity': 6, 'dependencies': []},
    {'id': 'T5', 'name': 'Documentation', 'urgency': 1, 'complexity': 2, 'dependencies': []}
]

# Task processing logic
def process_tasks(task_list):
    # Count tasks by urgency level (not used in final calculation)
    urgency_counts = {}
    for task in task_list:
        urgency = task['urgency']
        if urgency in urgency_counts:
            urgency_counts[urgency] += 1
        else:
            urgency_counts[urgency] = 1
    
    # Process task IDs (not relevant to final answer)
    task_ids = [task['id'] for task in task_list]
    task_id_pairs = list(itertools.combinations(task_ids, 2))[:3]
    
    # Filter tasks based on complexity
    filtered_tasks = []
    for idx, task in enumerate(task_list):
        # This filtering doesn't affect the answer since we slice later
        if idx % 2 == 0 or task['complexity'] > 2:
            filtered_tasks.append(task)
    
    # Calculate priority score for filtered tasks
    priority_score = calculate_priority(filtered_tasks[2:])
    
    return priority_score

# Execute task processing
result = process_tasks(tasks)
print(f"Result: {result}")