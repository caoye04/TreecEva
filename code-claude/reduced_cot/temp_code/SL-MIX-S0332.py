from collections import Counter, defaultdict
import itertools

def calculate_task_priority(tasks):
    # Distractor: Creating a complex defaultdict structure
    task_dependencies = defaultdict(list)
    for i in range(len(tasks)):
        if i % 2 == 0 and i < len(tasks) - 1:
            task_dependencies[tasks[i]].append(tasks[i+1])
        elif i % 3 == 0:
            task_dependencies[tasks[i]].append(tasks[i])
    
    # Distractor: Counting character frequencies
    char_counts = Counter(''.join(tasks))
    most_common_chars = char_counts.most_common(3)
    
    # Main logic: Calculate priority based on specific criteria
    unique_tasks = set(tasks)
    task_weights = {}
    
    # Distractor: Complex but irrelevant computation
    complexity_factor = sum(len(task) for task in unique_tasks) / max(1, len(unique_tasks))
    estimated_completion = complexity_factor * len(tasks) * 0.75
    
    # Calculate weights - this is the relevant part
    for task in unique_tasks:
        # Base priority from position (first tasks are more important)
        position_value = tasks.index(task) * 2
        # Priority from frequency (more frequent tasks are more important)
        frequency_value = tasks.count(task) * 5
        # Priority from task name length (shorter names get higher priority)
        length_value = 10 - len(task)
        
        # Distractor calculation
        if task.startswith('bug'):
            distractor_value = sum(ord(c) % 10 for c in task)
        else:
            distractor_value = len(task_dependencies[task]) * 3
        
        # Combine factors for final weight
        task_weights[task] = position_value + frequency_value + length_value
    
    # Distractor: Generate combinations
    task_combinations = list(itertools.combinations(unique_tasks, 2))
    potential_paths = len(task_combinations) + len(unique_tasks)
    
    # Distractor: Recursive function that doesn't affect the result
    def calculate_complexity(depth, task_list):
        if depth <= 0 or not task_list:
            return 1
        return 1 + (depth * len(task_list) / 10)
    
    complexity_score = calculate_complexity(2, list(unique_tasks)[:3])
    
    # Actual priority calculation
    base_priority = sum(task_weights.values())
    adjustment = len(unique_tasks) * 3
    
    # Distractor: Additional complex calculations
    if 'deploy' in ''.join(tasks).lower():
        deployment_factor = 1.5
    else:
        deployment_factor = 1.0
        
    # More distractors: These don't affect the final result
    risk_factor = sum(1 for task in tasks if 'risk' in task.lower())
    urgency_score = len(tasks) - len(unique_tasks)
    
    # The actual result calculation
    return int(base_priority - adjustment)

# Main execution
pending_tasks = ['fix_login', 'update_ui', 'fix_login', 'deploy_backend', 'update_ui', 'optimize_db']

# Distractor: Create a complex task queue
task_queue = []
for i, task in enumerate(pending_tasks):
    priority_class = 'high' if i < 2 else 'medium' if i < 4 else 'low'
    estimated_hours = len(task) / 3
    task_queue.append((task, priority_class, estimated_hours))

# Distractor: Calculate some metrics
total_estimated_hours = sum(hours for _, _, hours in task_queue)
average_task_length = sum(len(task) for task in pending_tasks) / len(pending_tasks)

# Distractor: Process some task statistics
task_stats = defaultdict(int)
for task in pending_tasks:
    task_stats[task[0]] += 1  # Count first letter occurrences
    
most_common_initial = max(task_stats.items(), key=lambda x: x[1])[0]

# The key statement that calculates the actual answer
final_priority = calculate_task_priority(pending_tasks)

# Distractor: Additional processing after the key calculation
scaled_priority = final_priority * 1.25
adjusted_for_team_size = final_priority + 10

print(f"Result: {final_priority}")