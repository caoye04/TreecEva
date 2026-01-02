def analyze_efficiency(metrics):
    base = sum(metrics) / len(metrics)
    adjustment = (lambda x: x ** 0.5 if x > 5 else x / 2)(base)
    return adjustment

# Simulate employee performance evaluation
task_completion = [8, 7, 9, 6, 8]
error_rate = [2, 3, 1, 4, 2]

productivity = sum(task_completion) - sum(error_rate)
risk_factor = max(error_rate) - min(error_rate)

# Irrelevant distraction: calculate team diversity index (not used)
demographic_vars = [0.2, 0.5, 0.3]
diversity_index = sum([x * (1 - x) for x in demographic_vars])
redundant_calc = diversity_index * 100 // 1 if diversity_index > 0.1 else 0

# Another distraction: simulate unused time tracking
time_logs = "08:00,09:30,11:15,13:45"
durations = [int(t.split(':')[0]) * 60 + int(t.split(':')[1]) for t in time_logs.split(',')]
avg_duration = sum(durations) / len(durations)
adjusted_avg = avg_duration * 0.95

# Core logic with meaningful computation
efficiency_metrics = [productivity, risk_factor, len(task_completion)]
normalized_productivity = analyze_efficiency(efficiency_metrics)

# Conditional scoring logic
if productivity >= 30:
    performance_bonus = 10
elif productivity >= 20:
    performance_bonus = 5
else:
    performance_bonus = 0

risk_penalty = risk_factor * 2

# Key function using lambda and conditional expressions
evaluate_performance = lambda prod, risk: (
    (prod + performance_bonus - risk_penalty) 
    if risk < 3 else 
    (prod + performance_bonus // 2 - risk_penalty)
)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")