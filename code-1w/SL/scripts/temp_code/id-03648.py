from collections import defaultdict

# Simulate employee task tracking and performance evaluation
task_logs = [
    {'employee': 'Alice', 'tasks_completed': 8, 'errors': 1, 'overtime_hours': 5},
    {'employee': 'Bob', 'tasks_completed': 12, 'errors': 3, 'overtime_hours': 9},
    {'employee': 'Charlie', 'tasks_completed': 6, 'errors': 0, 'overtime_hours': 2},
    {'employee': 'Diana', 'tasks_completed': 15, 'errors': 5, 'overtime_hours': 12}
]

# Irrelevant summary for distraction
hours_worked = defaultdict(int)
for log in task_logs:
    hours_worked[log['employee']] += (8 + log['overtime_hours'])  # Assume 8-hour base

# Distractor: Compute average tasks (not used in final logic)
avg_tasks = sum(log['tasks_completed'] for log in task_logs) / len(task_logs)

# Primary metrics calculation
productivity = []
risk_factor = []
penalty_weights = {0: 0.0, 1: 0.1, 2: 0.25, 3: 0.45, 4: 0.7, 5: 1.0}  # Error-based penalty curve

for log in task_logs:
    base_productivity = log['tasks_completed'] * (1 + log['overtime_hours'] * 0.05)
    error_penalty = penalty_weights.get(log['errors'], 1.0)
    adjusted_productivity = base_productivity * (1 - error_penalty)
    
    productivity.append(adjusted_productivity)
    risk_factor.append(log['errors'] * 2 + log['overtime_hours'] // 3)

# Distractor: Sort unrelated list
task_errors = [log['errors'] for log in task_logs]
task_errors.sort(reverse=True)

# Helper function with semi-relevant logic
def compute_efficiency_index(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return mean_val - variance * 0.1

# Secondary distractor computation
efficiency_noise = compute_efficiency_index([10, 20, 30])

# Core evaluation logic
baseline = sum(productivity) / len(productivity)
scaled_risk = sum(risk_factor) / len(risk_factor)

# Conditional adjustment based on risk threshold
risk_adjustment = 1.2 if scaled_risk > 4 else 0.9

# Final performance score with conditional expression
temp_result = baseline * risk_adjustment
final_score = temp_result if temp_result > 10 else temp_result * 1.5

# Additional red herring: unused transformation
transformed = [round(p * (1.1 - r * 0.05), 2) for p, r in zip(productivity, risk_factor)]

print(f"Result: {final_score}")