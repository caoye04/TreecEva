from collections import defaultdict

# Simulate employee task tracking with some irrelevant metrics
task_logs = [
    {'employee': 'Alice', 'tasks': [1, 1, 0, 1], 'lateness': 2},
    {'employee': 'Bob', 'tasks': [1, 0, 1, 1], 'lateness': 0},
    {'employee': 'Charlie', 'tasks': [0, 1, 1, 1], 'lateness': 5}
]

# Distractor: Unused metric calculation
bonus_eligibility = defaultdict(lambda: False)
for log in task_logs:
    bonus_eligibility[log['employee']] = sum(log['tasks']) >= 3 and log['lateness'] < 3

# Core productivity metric (relevant)
productivity = 0
for log in task_logs:
    productivity += sum(log['tasks'])

# Intermediate distractor variables
total_lateness = sum(log['lateness'] for log in task_logs)
avg_completion = productivity / (len(task_logs) * 4)  # 4 tasks each

# Risk factor based on incomplete tasks
incomplete_tasks = 0
for log in task_logs:
    incomplete_tasks += log['tasks'].count(0)
risk_factor = incomplete_tasks * 2.5

# Irrelevant bitwise manipulation (distraction)
temp_flag = 0b1010
mask = 0b1100
obfuscated = temp_flag ^ mask | 0b0010  # Used nowhere

# Conditional logic with red herring function
def analyze_trend(data):
    return sum(data) > len(data) * 0.7

# Evaluate performance using lambda (python idiom)
evaluate_performance = lambda prod, risk: int((prod * 1.5) - risk) if prod > 5 else 0

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")