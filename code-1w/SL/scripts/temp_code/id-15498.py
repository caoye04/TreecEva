from collections import defaultdict

# Simulate employee task logs with timestamps and actions
task_logs = [
    ('08:15', 'start', 'data_entry'),
    ('08:30', 'complete', 'data_entry'),
    ('08:35', 'start', 'email_response'),
    ('09:05', 'complete', 'email_response'),
    ('09:10', 'start', 'report_generation'),
    ('09:55', 'complete', 'report_generation'),
    ('10:00', 'start', 'meeting'),
    ('10:45', 'complete', 'meeting'),
    ('10:50', 'start', 'code_review'),
    ('11:20', 'complete', 'code_review')
]

# Track time spent per task category
time_spent = defaultdict(float)
previous_time = None

for timestamp, action, task in task_logs:
    hour, minute = map(int, timestamp.split(':'))
    current_minutes = hour * 60 + minute
    
    if previous_time is not None and action == 'complete':
        duration = current_minutes - previous_time
        time_spent[task] += duration
    
    if action == 'start':
        previous_time = current_minutes

# Calculate total productive minutes (exclude meetings)
total_productive = sum(time_spent[task] for task in time_spent if 'meeting' not in task)
total_idle = 480 - sum(time_spent.values())  # Assuming 8-hour workday in minutes

# Distractor: Irrelevant string processing for log formatting
task_summary = []
for task in time_spent:
    formatted_task = task.replace('_', ' ').title()
    padded_name = formatted_task.ljust(20)
    task_summary.append(f"{padded_name}: {time_spent[task]:.1f} min")

summary_string = "\n".join(task_summary)
digest_flag = summary_string.lower().count('e') > 10

# Productivity metric based on focused work ratio
if total_productive > 0:
    focus_ratio = time_spent['code_review'] / total_productive
else:
    focus_ratio = 0

productivity = int((total_productive / 480) * 100)

# Risk factor from irregular patterns
long_tasks = [t for t in time_spent if time_spent[t] > 40]
short_tasks = [t for t in time_spent if time_spent[t] < 15]
risk_factor = len(long_tasks) - len(short_tasks)

# Misleading intermediate calculation (not used in final logic)
avg_duration = sum(time_spent.values()) / len(time_spent) if time_spent else 0
disruption_index = abs(total_idle - avg_duration)

# Core evaluation function combining productivity and risk
def evaluate_performance(efficiency, risk):
    base_score = efficiency * 1.5
    
    # Apply risk penalties or bonuses
    if risk < 0:
        adjusted_score = base_score * 0.8
    elif risk == 0:
        adjusted_score = base_score * 1.0
    else:
        adjusted_score = base_score * 1.2
    
    # Final adjustment based on focus behavior
    if focus_ratio > 0.3:
        adjusted_score += 5
    
    return int(adjusted_score)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Output result
print(f"Result: {final_score}")