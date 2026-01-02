def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0.0
    if base_efficiency > 80:
        adjustment = 10.5
    elif base_efficiency > 60:
        adjustment = 5.2
    else:
        adjustment = -3.7
    return base_efficiency + adjustment

productivity = [75, 82, 90, 68, 77]
overhead_costs = [1200, 1350, 1100, 1400, 1280]

# Irrelevant computation on overhead (distractor)
total_cost = sum(overhead_costs)
avg_cost = total_cost / len(overhead_costs)
cost_per_unit = [c / p for p, c in zip(productivity, overhead_costs)]

normalized_productivity = [score * 1.1 for score in productivity if score < 85]

# Conditional expression used here (required feature)
efficiency_rating = analyze_efficiency(productivity) if sum(normalized_productivity) > 200 else 50.0

risk_factor = 0
for i, val in enumerate(productivity):
    if val < 70:
        risk_factor += 8
    elif val < 80:
        risk_factor += 3
    else:
        risk_factor -= 2

# Semi-relevant transformation (not directly used but looks important)
stability_index = efficiency_rating - (risk_factor * 0.8)
decay_rate = 0.95
projected_stability = stability_index
for _ in range(3):
    projected_stability *= decay_rate

# Core logic with multiple concepts: sets, comparisons, logical ops
critical_thresholds = {70, 80, 85}
met_targets = {score for score in productivity if score in critical_thresholds}
exceeded_expectations = any(s > 85 for s in productivity)

# Final decision logic using conditional expression
bonus_applied = len(met_targets) >= 2 and exceeded_expectations

# Key statement — answer depends on this function call
def evaluate_performance(prod_data, risk):
    raw_avg = sum(prod_data) / len(prod_data)
    penalty = risk * 1.5 if risk > 10 else 0
    multiplier = 1.2 if bonus_applied else 1.0
    return round((raw_avg - penalty) * multiplier, 2)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")