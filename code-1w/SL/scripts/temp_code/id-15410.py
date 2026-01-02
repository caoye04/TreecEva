def evaluate_performance(rate, faults):
    base = 100 if rate >= 75 else 70
    penalty = 10 if faults > 5 else 0
    bonus = 5 if rate > 85 and faults <= 2 else 0
    return base - penalty + bonus

# Simulate daily task tracking
hours_worked = 8
tasks_completed = 42
avg_completion_time = 2.3  # hours per task

# Productivity calculation (percentage)
productivity = (tasks_completed / (hours_worked * 5.25)) * 100  # 5.25 max tasks/hour

# Distraction: irrelevant metric computation
idle_time = hours_worked * 0.15
context_switches = 12
theoretical_max = hours_worked * 6  # hypothetical

# Error tracking
errors = 0
for i in range(tasks_completed):
    if i % 7 == 0 and i > 0:
        errors += 1

# More distraction: unused helper logic
def analyze_trend(data):
    return sum(data) / len(data) if data else 0

task_history = [6, 7, 5, 8, 6]
trend = analyze_trend(task_history)

# Key execution point
final_score = evaluate_performance(productivity, errors)

# Output result
print(f"Result: {final_score}")