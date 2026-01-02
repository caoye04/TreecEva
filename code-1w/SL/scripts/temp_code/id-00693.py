def analyze_efficiency(metrics):
    adjustment_factor = 0.85
    base_efficiency = sum(metrics) / len(metrics)
    adjusted = list(map(lambda x: x * adjustment_factor, metrics))
    return sum(adjusted) / len(adjusted)


def calculate_stress_level(workload, threshold=75):
    stress = 0
    if workload > threshold:
        stress = (workload - threshold) * 1.5
    else:
        stress = workload * 0.2
    return stress

# Simulated employee performance data
task_completion = [88, 92, 76, 85, 91]
errors = [3, 1, 7, 4, 2]
risk_exposure = 68
overtime_hours = 12

# Irrelevant distraction variables
teams_count = 5
project_deadline_days = 14
unused_buffer = [0] * 10
placeholder_result = None

# Core logic with distractors
productivity = analyze_efficiency(task_completion)
error_rate = sum(errors) / len(errors)

# Misleading intermediate calculation (not used in final answer)
theoretical_max = max(task_completion) * len(task_completion)
scaling_offset = theoretical_max * 0.01  # dead-end computation

risk_factor = calculate_stress_level(overtime_hours)

# Distractor: complex but unused tuple unpacking
stats_summary = (productivity, error_rate, risk_factor, 0.0)
(p_eff, e_rate, r_risk, _) = stats_summary

# Additional red herring: logical operation with no downstream effect
is_high_pressure = overtime_hours > 10 and max(task_completion) > 90
if is_high_pressure:
    temp_adjustment = 5.5
    unused_buffer[0] = temp_adjustment  # side effect that goes nowhere

# Key computational chain
performance_index = productivity - (risk_factor * 0.3)
penalty = 0
if error_rate > 3.0:
    penalty = error_rate * 2

adjusted_index = performance_index - penalty

# Final evaluation using lambda in functional context
evaluate_performance = lambda p, r: int(p - r + 50)

final_score = evaluate_performance(productivity, risk_factor)

# Output requirement
print(f"Result: {final_score}")