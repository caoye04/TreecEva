def analyze_efficiency(x):
    return lambda y: (x * y) + 2

# Simulate employee performance metrics
task_completion = [8, 7, 9, 6]
errors = [1, 0, 2, 1]
base_multiplier = 3

# Irrelevant intermediate calculation (distractor)
phantom_metric = sum([x ** 0.5 for x in task_completion]) / len(task_completion)

productivity = sum(task_completion) * base_multiplier
error_penalty = sum(errors) * 5

# Misleading conditional that doesn't affect final outcome
count_high_perf = 0
for val in task_completion:
    if val > 7:
        count_high_perf += 1

if count_high_perf >= 2:
    productivity += 3  # This seems important but is actually redundant due to later override

# Override based on dynamic rule
adjustment_factor = 1.2 if len(errors) > 3 else 0.8
productivity = int(productivity * adjustment_factor)

# Risk assessment with red herring computations
risk_raw = [abs(x - 7) for x in task_completion]
risk_sum = sum(risk_raw)
decoy_risk_norm = [r / (risk_sum + 1e-8) for r in risk_raw]  # Not used later
risk_factor = max(risk_raw) - min(risk_raw)

# Unused helper function (dead code path - distractor)
def normalize_score(val, min_val=0, max_val=10):
    return (val - min_val) / (max_val - min_val)

# Core evaluation logic
compute_bonus = lambda p, e: p - e * 4
bonus = compute_bonus(productivity, error_penalty)

# Final scoring with indirect dependency
evaluate_performance = lambda perf, risk: (perf // (risk + 1)) + bonus // 10

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result for inspection
print(f"Result: {final_score}")