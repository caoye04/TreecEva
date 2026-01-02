from itertools import compress, cycle

def analyze_efficiency(metrics):
    base = sum(m * (i + 1) for i, m in enumerate(metrics))
    adjustment = len([m for m in metrics if m > 75])
    return base + adjustment * 2

def compute_stress_level(hours, deadlines):
    stress_index = 0
    for h, d in zip(hours, deadlines):
        if h > 8:
            stress_index += d * 1.5
        elif h < 4:
            stress_index -= d * 0.5
    return max(stress_index, 0)

def evaluate_performance(output, risk):
    efficiency = output * 0.8
    penalty = risk * 3 if risk > 50 else 0
    return int(efficiency - penalty)

# Simulated employee performance data
task_completion = [88, 92, 76, 85, 90]
hours_worked = [9, 7, 10, 6, 8]
deadline_count = [3, 2, 4, 1, 3]

# Irrelevant intermediate calculations (distractors)
avg_hours = sum(hours_worked) / len(hours_worked)
total_deadlines = sum(deadline_count)
workload_ratio = total_deadlines / len(task_completion) if avg_hours > 6 else 0

# Key derived metrics
productivity = analyze_efficiency(task_completion)
risk_factor = compute_stress_level(hours_worked, deadline_count)

# Red herring: unused function call
unused_mask = list(compress(task_completion, [h > 7 for h in hours_worked]))
filtered_metrics = [x for x in task_completion if x > 80]
scaled_metrics = list(map(lambda x: x * 1.1, filtered_metrics))

# Misleading state tracking
status_log = []
for val in scaled_metrics:
    status_log.append(f"Adjusted: {val:.1f}")

# Core evaluation logic with conditional expression
temp_bonus = 10 if len(filtered_metrics) >= 3 else 5
productivity += temp_bonus

# Final computation point
final_score = evaluate_performance(productivity, risk_factor)

# Output result as required
print(f"Result: {final_score}")