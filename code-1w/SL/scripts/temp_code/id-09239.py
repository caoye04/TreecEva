def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) // len(adjusted) if adjusted else 0


def compute_stress_level(hours, threshold=8):
    excess = hours - threshold
    return max(0, excess * 1.5)


def evaluate_performance(output, risk):
    base = output * 0.8
    penalty = risk * 2.5
    return int(base - penalty)

# Simulation data
task_completion = [7, 6, 9, 4, 8]
daily_hours = [7.5, 9.0, 8.2, 6.0, 10.5]

# Irrelevant aggregations
avg_hours = sum(daily_hours) / len(daily_hours)
hour_set = set(int(h) for h in daily_hours)
peak_load = max(task_completion) * 10

# Intermediate computations with distractions
productivity = analyze_efficiency(task_completion)

# Dummy recursion (distractor)
def dummy_recursion(n):
    if n <= 1:
        return 1
    return n + dummy_recursion(n - 2)

_ = dummy_recursion(7)

# Misleading risk modeling
raw_risk = sum(compute_stress_level(h) for h in daily_hours)
adjusted_risk = raw_risk * 0.7
risk_factor = adjusted_risk if adjusted_risk > 10 else 10

# Key state tracking
status_flags = {"stable": productivity > 7, "high_risk": risk_factor >= 12}

# Core evaluation logic
temp_debug = productivity * risk_factor
final_score = evaluate_performance(productivity, risk_factor)

# Additional red herring: unused tuple unpacking
_, _, *extra = (1, 2, 3, 4, 5)

# Print final result
print(f"Result: {final_score}")