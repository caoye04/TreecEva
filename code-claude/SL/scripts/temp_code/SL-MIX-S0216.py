# Task Management System - Priority Calculator

def calculate_urgency(days_left):
    # Lower days means higher urgency (inverse relationship)
    base_urgency = 10 if days_left <= 0 else max(1, 10 - days_left)
    return base_urgency

# Project tasks with their deadlines (days remaining) and importance (1-5)
tasks = [
    ("Database migration", 2, 5),
    ("API documentation", 7, 3),
    ("Security audit", 1, 5),
    ("UI redesign", 4, 4),
    ("Performance testing", 3, 4)
]

# Weights for different factors
urgency_weight = 0.6
importance_weight = 0.4

# Track highest priority task
highest_priority = 0
highest_task = ""

# Configuration parameters
team_capacity = 8  # Team capacity (hours/day)
difficulty_factors = {"low": 0.8, "medium": 1.0, "high": 1.2}
effort_multiplier = difficulty_factors["medium"]

# Process each task
for i, (task_name, deadline, importance) in enumerate(tasks):
    # Calculate base priority
    urgency = calculate_urgency(deadline)
    raw_priority = (urgency * urgency_weight) + (importance * importance_weight)
    
    # Apply team-specific adjustments
    adjustment = lambda x: x * 1.5 if deadline <= 2 else x
    adjusted_priority = adjustment(raw_priority)
    
    # Track task for reporting
    if adjusted_priority > highest_priority:
        highest_priority = adjusted_priority
        highest_task = task_name
    
    # Only process the third task (index 2) for final calculation
    if i == 2:
        base_priority = raw_priority
        # Calculate effort required
        effort_hours = importance * 2 * effort_multiplier
        # Apply deadline pressure
        deadline_factor = 10 / (deadline + 1)
        # Normalize priority
        actual_priority = base_priority * deadline_factor
        # Apply final multiplier
        multiplier = 1.25
        final_priority = actual_priority * multiplier

# Display results
print(f"Highest priority task: {highest_task} ({highest_priority:.2f})")
print(f"Security audit final priority: {final_priority:.2f}")
