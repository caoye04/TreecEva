def analyze_efficiency(metrics):
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    return weighted_sum

productivity = [85, 90, 78, 92]
overhead_costs = [1500, 1600, 1450, 1700]
baseline_threshold = 88

# Irrelevant aggregation
avg_cost = sum(overhead_costs) / len(overhead_costs)
cost_per_unit = avg_cost / 100

# Distractor: unused function
lambda_filter = lambda x: x > baseline_threshold
high_performers = list(filter(lambda_filter, productivity))

# Real computation begins
raw_efficiency = analyze_efficiency(productivity)

# Simulate risk adjustment with set operations
risk_set_a = {80, 85, 90, 95}
risk_set_b = {85, 90, 92, 94}
risk_overlap = risk_set_a & risk_set_b  # intersection
risk_factor = len(risk_overlap) * 0.5

# String-based distractor
status_report = "Performance review Q3"
if "Q3" in status_report:
    reporting_period = 3
else:
    reporting_period = 4

# Core logic hidden among distractions
def evaluate_performance(efficiency_data, risk):
    base_score = analyze_efficiency(efficiency_data)
    adjusted_score = base_score - risk * 2.5
    if adjusted_score >= 80:
        bonus = 5
    else:
        bonus = 0
    final_rating = adjusted_score + bonus
    return final_rating

# Misleading intermediate calculation (dead path)
placeholder_value = 0
for cost in overhead_costs:
    if cost > 1600:
        placeholder_value += 1  # Not used later

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")