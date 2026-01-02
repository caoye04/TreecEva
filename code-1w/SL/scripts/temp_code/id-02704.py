from itertools import cycle

# Simulate daily work metrics over a biweekly period
daily_hours = [8.5, 7.2, 9.0, 8.0, 6.5, 0, 0, 8.8, 7.9, 9.1, 8.2, 7.6, 0, 0]
urgent_tasks = [3, 1, 4, 2, 0, 0, 0, 5, 2, 3, 1, 4, 0, 0]
errors_logged = [1, 0, 2, 1, 0, 0, 0, 3, 1, 1, 0, 2, 0, 0]

# Helper: calculate rolling average
def moving_avg(data, window=3):
    smoothed = []
    for i in range(len(data)):
        if i < window - 1:
            smoothed.append(round(sum(data[:i+1]) / (i+1), 2))
        else:
            smoothed.append(round(sum(data[i-window+1:i+1]) / window, 2))
    return smoothed

# Apply smoothing to key metrics
smoothed_hours = moving_avg(daily_hours)
scaled_errors = [e * 1.5 for e in errors_logged]  # Weighted error impact
efficiency_ratio = [round(smoothed_hours[i] / (1 + scaled_errors[i]), 2) for i in range(len(smoothed_hours))]

# Simulate team rotation using itertools
team_roster = ['Alice', 'Bob', 'Charlie']
rotator = cycle(team_roster)
staff_schedule = [next(rotator) for _ in range(14)]  # Two-week schedule

# Distractor: irrelevant string processing
task_labels = [f"Task-{i}" for i in range(len(urgent_tasks))]
capitalized_labels = [label.upper() for label in task_labels]
label_checksum = sum(ord(char) for label in capitalized_labels for char in label if char.isdigit())

# Core logic variables
base_productivity = sum(efficiency_ratio) / len(efficiency_ratio)
absent_days = daily_hours.count(0)
adjusted_productivity = base_productivity * (1 - absent_days * 0.05)

# Risk increases non-linearly with error frequency and absences
error_frequency = sum(errors_logged) / len([h for h in daily_hours if h > 0])
risk_factor = round(error_frequency ** 2 + absent_days * 0.3, 3)

# Secondary distractor: unused data transformation
phantom_data = [[i*j for j in range(3)] for i in range(5)]
stale_flag = any(sum(row) > 10 for row in phantom_data)

# Final evaluation function
def evaluate_performance(prod, risk):
    if prod < 5.0:
        return max(10, int(50 - risk * 10))
    elif prod >= 8.0:
        return min(95, int(75 + prod - risk * 5))
    else:
        base = 60 + (prod - 6.0) * 5
        penalty = risk * 7
        return int(base - penalty)

# Critical statement
final_score = evaluate_performance(adjusted_productivity, risk_factor)

# Output result
print(f"Result: {final_score}")