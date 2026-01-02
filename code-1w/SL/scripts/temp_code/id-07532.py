def analyze_efficiency(logs):
    total_ops = sum([len(entry) for entry in logs])
    avg_len = total_ops / len(logs) if logs else 0
    filtered = [op for entry in logs for op in entry if op > 2]
    efficiency = len(filtered) / total_ops if total_ops > 0 else 0
    return efficiency


def compute_volatility(data):
    if not data:
        return 0
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance ** 0.5

# Simulated employee task logs over a week
daily_tasks = [
    [3, 1, 4, 1, 5],
    [2, 7, 1, 8, 2],
    [8, 1, 8, 2, 8],
    [4, 5, 9, 2, 6],
    [5, 3, 5, 8, 9]
]

# Irrelevant metrics (distractors)
task_lengths = [len(day) for day in daily_tasks]
peak_day = max(task_lengths)
duplicate_count = sum(1 for day in daily_tasks for x in day if x == 8)

# Core productivity metric
baseline_effort = sum(sum(day) for day in daily_tasks)
productivity = analyze_efficiency(daily_tasks)

# Risk assessment from error rates
error_rates = [0.05, 0.02, 0.07, 0.04, 0.06]
risk_volatility = compute_volatility(error_rates)
risk_factor = max(risk_volatility, 0.03) * 100

# Dummy transformation (dead code path - not used)
if risk_factor < 5:
    adjusted_risk = risk_factor * 2
else:
    adjusted_risk = risk_factor + 1  # Not used anywhere

# Final evaluation with distraction variables present but not all used
def evaluate_performance(eff, risk):
    base_score = eff * 100
    penalty = risk * 0.5 if risk > 4 else 0
    bonus = 10 if base_score > 60 else 5
    # Additional logic to increase reasoning steps
    if eff > 0.7:
        bonus += 5
    elif eff > 0.5:
        bonus += 3
    else:
        bonus += 1
    return base_score - penalty + bonus

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")