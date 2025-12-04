def calculate_complexity(task_details):
    # Complexity calculation based on task attributes
    word_count = len(task_details.split())
    unique_chars = len(set(task_details.lower()))
    complexity = (word_count * 0.6) + (unique_chars * 0.4)
    
    # Misleading calculation that isn't used
    advanced_score = sum([ord(c) for c in task_details[:5]]) / 100
    return int(complexity)

def analyze_dependencies(dependencies):
    # This function looks important but its result is never used meaningfully
    if not dependencies:
        return 0
    
    dependency_score = len(dependencies) * 5
    critical_paths = [d for d in dependencies if d.startswith('critical-')]
    
    if critical_paths:
        dependency_score += len(critical_paths) * 10
    
    return dependency_score

def calculate_priority(task):
    # Extract task components with misleading variable names
    task_id, description, urgency, importance, dependencies = task
    
    # Distractor calculation that looks important
    task_hash = sum([ord(c) for c in task_id]) % 100
    
    # Actual priority calculation
    base_priority = urgency * 2 + importance * 3
    
    # Misleading calculation that isn't used
    dependency_factor = analyze_dependencies(dependencies)
    
    # Complexity is calculated but not used in final priority
    complexity = calculate_complexity(description)
    
    return base_priority

def filter_tasks(task_list, min_urgency=0, min_importance=0):
    # Filter tasks based on criteria
    filtered = []
    for idx, task in enumerate(task_list):
        # Unnecessary conversion and operation
        binary_idx = bin(idx)[2:].zfill(4)
        hex_idx = hex(idx)[2:]
        
        task_id, description, urgency, importance, dependencies = task
        
        # Distractor code path that's never taken with our data
        if urgency > 10 and 'impossible' in description.lower():
            continue
            
        if urgency >= min_urgency and importance >= min_importance:
            filtered.append(task)
    
    # Misleading sorting that isn't used
    sorted_filtered = sorted(filtered, key=lambda x: x[0])
    
    return filtered

def calculate_final_priority(filtered_tasks):
    # Set up tracking variables
    total_priority = 0
    max_priority = -1
    min_priority = 100
    
    # Misleading variables
    priority_weights = {'high': 3, 'medium': 2, 'low': 1}
    weighted_priorities = []
    
    for task in filtered_tasks:
        # Calculate individual task priority
        current_priority = calculate_priority(task)
        
        # Update tracking variables
        total_priority += current_priority
        max_priority = max(max_priority, current_priority)
        min_priority = min(min_priority, current_priority)
        
        # Distractor calculation
        task_id, _, _, _, _ = task
        if task_id.startswith('A'):
            weighted_priorities.append(current_priority * priority_weights['high'])
        elif task_id.startswith('B'):
            weighted_priorities.append(current_priority * priority_weights['medium'])
        else:
            weighted_priorities.append(current_priority * priority_weights['low'])
    
    # The actual calculation that determines the answer
    if filtered_tasks:
        priority_score = total_priority // len(filtered_tasks)
    else:
        priority_score = 0
    
    # More distractor calculations that don't affect the result
    priority_range = max_priority - min_priority if max_priority > -1 else 0
    priority_variance = sum((p - (total_priority/len(filtered_tasks)))**2 for p in [calculate_priority(t) for t in filtered_tasks]) / len(filtered_tasks) if filtered_tasks else 0
    
    return priority_score

# Task data: (id, description, urgency, importance, dependencies)
tasks = [
    ('A123', 'Update user interface components', 4, 3, ['B456']),
    ('B456', 'Fix database connection issue', 5, 5, []),
    ('C789', 'Implement new search feature', 3, 4, ['A123']),
    ('D012', 'Optimize image loading algorithm', 2, 5, ['E345']),
    ('E345', 'Update API documentation', 1, 2, [])
]

# Distractor tasks that aren't used
unused_tasks = [
    ('F678', 'Refactor authentication module', 5, 4, ['G901']),
    ('G901', 'Add unit tests for payment processing', 4, 5, [])
]

# Filter tasks with minimum requirements
filtered_tasks = filter_tasks(tasks, min_urgency=3, min_importance=3)

# Distractor operation
task_ids = {task[0] for task in tasks}
task_descriptions = [task[1] for task in tasks]

# Calculate final priority score
priority_score = calculate_final_priority(filtered_tasks)

# Misleading operation that doesn't affect the answer
for idx, (task_id, description) in enumerate(zip([t[0] for t in filtered_tasks], [t[1] for t in filtered_tasks])):
    complexity = calculate_complexity(description)
    if complexity > 10:
        print(f"Complex task found: {task_id}")

# Print the result
print(f"Result: {priority_score}")