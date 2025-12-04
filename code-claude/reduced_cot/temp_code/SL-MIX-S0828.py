import itertools

# Task priority calculator for a project management system
# Higher score = higher priority task

# Define task data: (task_name, category, deadline_days)
tasks = [
    ("Database migration", "backend", 3),
    ("UI redesign", "frontend", 5),
    ("API documentation", "documentation", 2)
]

# Character weight mapping for priority calculation
char_weights = {'a': 2, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
               'p': 3, 'r': 2, 't': 2, 'd': 2, 'c': 2}

# Select the task to analyze
current_task = tasks[2][0].lower()

# Calculate priority based on character weights
priority_score = sum(char_weights.get(c, 0) for c in current_task)

# Adjust priority based on deadline (not relevant for the question)
final_priority = priority_score * (1 + 1/tasks[2][2])

# Display results
print(f"Task: {tasks[2][0]}")
print(f"Character-based priority: {priority_score}")
print(f"Final adjusted priority: {final_priority}")
