def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    for entry in logs:
        start, end, status = entry
        duration = end - start
        total_hours += duration
        if status == 'idle':
            idle_periods += 1
    avg_duration = total_hours / len(logs) if logs else 0
    return total_hours, avg_duration, idle_periods

logs_data = [(8, 10, 'active'), (10, 11, 'idle'), (11, 14, 'active'), (14, 15, 'idle')]

hours, mean_time, idles = analyze_productivity(logs_data)

# Simulate task contributions with complexity levels
tasks = ['bug_fix', 'feature_dev', 'docs', 'refactor']
complexity = [2, 5, 1, 4]
contributions = {task: comp for task, comp in zip(tasks, complexity)}

# Efficiency metric based on work-to-idle ratio
efficiency = (hours - idles * 1.5) / hours if hours > 0 else 0

# Distractor: Unused backup calculation
baseline_projection = sum(complexity) * 0.75
project_risk = 'low' if idles < 3 else 'high'

# Secondary distractor: character analysis in task names (not used)
char_count = 0
for task in tasks:
    char_count += len(task)
case_normalized = [t.upper() for t in tasks]

# Core logic hidden among other operations
def calculate_rating(contribs, eff):
    base = 0
    weights = {'bug_fix': 1.2, 'feature_dev': 1.8, 'docs': 0.8, 'refactor': 1.5}
    for task, level in contribs.items():
        if task in weights:
            base += level * weights[task]
    # Apply efficiency multiplier and scale
    scaled = base * eff
    bonus = 5 if 'feature_dev' in contribs and contribs['feature_dev'] >= 5 else 0
    return int(scaled + bonus)

# Key statement
final_score = calculate_rating(contributions, efficiency)

# Output required format
print(f"Target result: {final_score}")