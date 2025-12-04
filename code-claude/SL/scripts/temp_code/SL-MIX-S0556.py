from collections import Counter

# Task management system priority calculator
project_status = {
    'completed': 12,
    'in_progress': 8,
    'not_started': 5
}

# Count task statuses
task_statuses = ['completed', 'in_progress', 'not_started', 'completed', 'in_progress']
status_counter = Counter(task_statuses)

# Calculate task metrics
task_complexity = 3  # On scale 1-5
task_urgency = 6     # On scale 1-10

# Determine if task needs attention
needs_attention = status_counter['not_started'] > status_counter['completed']

# Calculate priority based on urgency and complexity
# Higher values indicate higher priority
priority_level = task_urgency ^ task_complexity  # Bitwise XOR operation

# Adjust priority if needed
final_priority = priority_level * 2 if needs_attention else priority_level

print(f"Result: {priority_level}")