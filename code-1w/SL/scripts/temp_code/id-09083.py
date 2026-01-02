from collections import defaultdict

# Simulate employee task logs with metadata
task_logs = [
    {'id': 1, 'type': 'bugfix', 'effort': 3, 'priority': 'high', 'completed': True},
    {'id': 2, 'type': 'feature', 'effort': 7, 'priority': 'medium', 'completed': True},
    {'id': 3, 'type': 'refactor', 'effort': 5, 'priority': 'low', 'completed': False},
    {'id': 4, 'type': 'bugfix', 'effort': 2, 'priority': 'high', 'completed': True},
    {'id': 5, 'type': 'feature', 'effort': 8, 'priority': 'high', 'completed': True},
    {'id': 6, 'type': 'docs', 'effort': 1, 'priority': 'low', 'completed': True}
]

# Irrelevant distractor: unused function
def calculate_risk_factor(logs):
    risk = 0
    for log in logs:
        if log['priority'] == 'high' and not log['completed']:
            risk += log['effort'] * 2
    return risk + 10  # red herring

# Another distractor variable
temporary_buffer = [0] * 10
for i in range(len(temporary_buffer)):
    temporary_buffer[i] = i ** 2 % 7

# Track task counts by type
task_counter = defaultdict(int)
for log in task_logs:
    task_counter[log['type']] += 1

# Compute productivity score based on completed high/medium priority tasks
productivity = 0
complexity = 0
priority_weights = {'low': 1, 'medium': 2, 'high': 3}

for log in task_logs:
    if log['completed']:
        weight = priority_weights[log['priority']]
        productivity += log['effort'] * weight
        if log['type'] in ['feature', 'refactor']:
            complexity += log['effort'] * weight

# Distractor: unused intermediate calculation
idle_time_estimate = sum([1 for log in task_logs if log['type'] == 'docs']) * 0.5

# Conditional logic with nested expressions
if productivity > 30:
    bonus_factor = 1.2
else:
    bonus_factor = 1.0

# Simulate experience multiplier (not actually used but looks relevant)
experience_levels = {'junior': 1, 'mid': 1.3, 'senior': 1.7}
current_experience = experience_levels['mid']

# Real evaluation function
prev_score = 0
for i in range(2):
    prev_score += productivity * (0.9 + i * 0.1)

# Final performance evaluation combining productivity and complexity
def evaluate_performance(prod, comp):
    base = prod * 0.8
    adjustment = comp * 0.3
    # Nested conditional to increase logic depth
    if comp > 20:
        adjustment *= 1.1
    elif comp > 10:
        adjustment *= 1.05
    else:
        adjustment *= 0.95
    return int(base + adjustment)  # deterministic integer result

# Key statement
final_score = evaluate_performance(productivity, complexity)

# Print result as required
print(f"Result: {final_score}")