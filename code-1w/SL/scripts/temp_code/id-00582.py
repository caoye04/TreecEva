def analyze_efficiency(metrics):
    # Irrelevant helper that computes unused metric
    overhead = sum(x ** 0.5 for x in metrics if x > 25)
    normalized = [x / (sum(metrics) / len(metrics)) for x in metrics]
    return list(map(lambda val: val * 1.1 if val < 1 else val * 0.9, normalized))

productivity = [88, 92, 75, 96, 85]
penalties = {"lateness": 3, "errors": 7, "rework": 12}
baseline_adjustment = 1.05

# Simulate team performance adjustments
adjusted_productivity = []
for score in productivity:
    if score >= 90:
        adjusted_score = score * baseline_adjustment
    elif score >= 80:
        adjusted_score = score * 1.02
    else:
        adjusted_score = score * 0.98
    adjusted_productivity.append(round(adjusted_score))

# Unused complex structure with set operations
skill_set_a = {'coding', 'design', 'testing', 'deployment'}
skill_set_b = {'analysis', 'design', 'review'}
cross_skills = skill_set_a & skill_set_b
redundant_union = skill_set_a | skill_set_b

# Dummy accumulation to increase cognitive load
auxiliary_sum = 0
for key, penalty in penalties.items():
    auxiliary_sum += len(key) * penalty

# Core logic hidden among distractions
risk_factor = 0
for val in productivity:
    if val < 80:
        risk_factor += 10
    elif val < 90:
        risk_factor += 5

# Key function using lambda and conditional logic
evaluate_performance = lambda prod_list, risk: sum(prod_list) // 5 - risk

# Critical statement
final_score = evaluate_performance(adjusted_productivity, risk_factor)

print(f"Result: {final_score}")