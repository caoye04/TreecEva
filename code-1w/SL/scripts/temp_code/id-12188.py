def evaluate_performance(output, risk_profile):
    base_efficiency = sum(output) // len(output) if output else 0
    safety_margin = 100 - max(risk_profile) if risk_profile else 0
    bonus = 15 if len(risk_profile) > 3 else 5
    penalty = -20 if min(output) < 50 else 0
    return base_efficiency + safety_margin + bonus + penalty

# Simulate team performance metrics
task_completion_rates = [88, 76, 92, 67, 81]
risk_exposure_levels = {12, 45, 67, 34, 89}

# Irrelevant intermediate calculations (distractors)
stress_factor = sum(x ** 0.5 for x in risk_exposure_levels) / len(risk_exposure_levels)
theoretical_max = max(task_completion_rates) * len(task_completion_rates)
avg_completion = sum(task_completion_rates) / len(task_completion_rates)
completion_set = set(task_completion_rates)
low_performers = {x for x in completion_set if x < 75}

# Key state tracking with conditional logic
if len(low_performers) >= 2:
    adjustment = 10
else:
    adjustment = 0

# Simulate workload distribution
workload_distribution = []
for i in range(len(task_completion_rates)):
    workload_distribution.append(task_completion_rates[i] * (i + 1))

total_weighted_load = sum(workload_distribution)
scaled_factor = total_weighted_load // 100

# More distraction: unused helper logic
def calculate_theoretical_efficiency(elements):
    return sum(e**2 for e in elements) // max(elements)

hypothetical_efficiency = calculate_theoretical_efficiency(task_completion_rates)

# Core computation path
productivity = task_completion_rates
risk_set = risk_exposure_levels

# Final evaluation point
final_score = evaluate_performance(productivity, risk_set)
print(f"Result: {final_score}")