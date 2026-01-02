def evaluate_performance(output, risk):
    base_score = 50
    if output > 80:
        base_score += 20
    elif output > 60:
        base_score += 10
    else:
        base_score -= 5

    if risk < 0.3:
        base_score += 15
    elif risk < 0.7:
        base_score += 5
    else:
        base_score -= 10

    return base_score

# Simulated employee data
team_data = [
    {'name': 'Alice', 'hours_worked': 160, 'tasks_completed': 45, 'errors': 2},
    {'name': 'Bob', 'hours_worked': 140, 'tasks_completed': 38, 'errors': 8},
    {'name': 'Charlie', 'hours_worked': 180, 'tasks_completed': 50, 'errors': 12}
]

# Irrelevant aggregate calculations (distractors)
total_hours = sum(emp['hours_worked'] for emp in team_data)
avg_tasks = sum(emp['tasks_completed'] for emp in team_data) / len(team_data)
error_rate = sum(emp['errors'] for emp in team_data) / total_hours

# Focus on Alice's performance
alice = team_data[0]
productivity = (alice['tasks_completed'] * 100) / 50  # Normalize to percentage

# Dummy transformation chain (semi-relevant but not used directly)
normalized_output = productivity * 1.1 if alice['errors'] < 5 else productivity * 0.9
adjusted_for_overtime = normalized_output + (alice['hours_worked'] - 160) * 0.05

# Risk assessment based on error frequency
error_ratio = alice['errors'] / alice['tasks_completed']
risk_factor = 1.0 if error_ratio > 0.2 else (0.6 if error_ratio > 0.1 else 0.2)

# Additional distraction: unused helper logic
def calculate_efficiency(tasks, hours, err):
    speed = tasks / (hours / 40)
    accuracy = 1 - (err / tasks)
    return speed * accuracy * 100

efficiency_scores = [calculate_efficiency(e['tasks_completed'], e['hours_worked'], e['errors']) for e in team_data]

# Core evaluation (critical step)
final_score = evaluate_performance(productivity, risk_factor)

# Distraction: secondary metric not used in final answer
consistency_bonus = 5 if all(emp['hours_worked'] >= 140 for emp in team_data) else 0

# Output target result
print(f"Result: {final_score}")