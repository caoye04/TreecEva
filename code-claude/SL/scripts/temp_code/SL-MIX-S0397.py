import itertools

def calculate_priority(tasks):
    # Calculate priority based on task urgency and importance
    if not tasks:
        return 0
    
    # Extract task metrics
    urgencies = [t[0] for t in tasks]
    importances = [t[1] for t in tasks]
    
    # Some processing metrics (not directly used)
    difficulty_metrics = [len(str(u * i)) for u, i in zip(urgencies, importances)]
    processing_factor = sum(difficulty_metrics) // len(difficulty_metrics)
    
    # Calculate base score with bitwise operations
    base_score = 0
    for u, i in zip(urgencies, importances):
        base_score |= (u & i) ^ (u | i) % 10
    
    # Apply weighting - this is the key calculation
    weighted_sum = sum(u * i for u, i in zip(urgencies, importances))
    return weighted_sum // len(tasks)

# Task management system simulation
task_list = [
    (5, 8, "Update documentation"),  # (urgency, importance, description)
    (7, 3, "Fix minor bugs"),
    (9, 9, "Resolve security issue"),
    (2, 4, "Refactor old code"),
    (6, 7, "Add new feature"),
    (8, 2, "Optimize database queries")
]

# Some processing on task descriptions (not directly relevant to final result)
descriptions = [task[2] for task in task_list]
description_lengths = [len(d) for d in descriptions]
avg_description_length = sum(description_lengths) / len(description_lengths)
long_descriptions = [d for d in descriptions if len(d) > avg_description_length]

# Filter tasks based on combined criteria
minimum_urgency = 4
minimum_importance = 6
filtered_tasks = [(u, i) for u, i, _ in task_list if u >= minimum_urgency and i >= minimum_importance]

# Generate combinations for team assignment (distractor operation)
team_members = ["Alice", "Bob", "Charlie"]
possible_assignments = list(itertools.combinations(team_members, 2))

# Calculate task priority score
priority_score = calculate_priority(filtered_tasks)

# Additional processing that doesn't affect the result
task_ids = [f"TASK-{100 + i}" for i in range(len(task_list))]
task_lookup = {tid: desc for tid, (_, _, desc) in zip(task_ids, task_list)}

print(f"Result: {priority_score}")