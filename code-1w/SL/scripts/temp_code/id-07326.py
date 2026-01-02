def analyze_efficiency(metrics):
    base = sum(metrics) / len(metrics)
    adjusted = base * 0.9 if base > 80 else base * 1.1
    penalty = 5 if max(metrics) - min(metrics) > 50 else 0
    return adjusted - penalty

productivity = [88, 76, 92, 81, 95]
overhead_costs = [12, 15, 10, 18, 14]
resource_ratio = sum(overhead_costs) / len(overhead_costs)

efficiency = analyze_efficiency(productivity)
fluctuation_index = (max(productivity) - min(productivity)) // 10

status_flags = { 'stable': efficiency > 85, 'growing': productivity[-1] > productivity[0] }

risk_metrics = [10, 20, 5, 15]
risk_factor = sum(r for r in risk_metrics if r > 10) * 0.5
auxiliary_data = [r * 2 for r in risk_metrics]  # Distractor: unused list comprehension

scaling_factor = 1.0
if status_flags['stable']:
    scaling_factor += 0.1
if status_flags['growing']:
    scaling_factor += 0.05

adjusted_risk = risk_factor * scaling_factor

# Simulate conditional bonus adjustment
bonus_eligibility = 'yes' if efficiency > 80 and adjusted_risk < 25 else 'no'
bonus_points = 10 if bonus_eligibility == 'yes' else 0

# Irrelevant string manipulation distraction
log_entry = "Performance review complete"
log_entry = log_entry.upper().replace(" ", "_")
log_timestamp = "2023-11-05"  # Unused variable

# Core evaluation logic with set operations and conditional expression
targets_met = {88, 92, 95}
actual_high_performers = set(productivity)
overlap_count = len(targets_met & actual_high_performers)

incentive_multiplier = 1.25 if overlap_count >= 2 else 0.9

final_score = 0  # Initialization

def evaluate_performance(prod, risk):
    raw_score = sum(prod) * 0.3 - risk * 2
    stability_bonus = 20 if fluctuation_index <= 2 else 0
    performance_set = set(p // 10 * 10 for p in prod)  # Bucket scores by decade
    completeness_factor = 0.95 if len(performance_set) >= 4 else 0.85
    return (raw_score + stability_bonus) * completeness_factor + bonus_points * incentive_multiplier

final_score = evaluate_performance(productivity, risk_factor)

# Red herring: secondary calculation with no impact
projected_next = efficiency * 1.05
buffer_allocation = projected_next * 0.05

# Final output
print(f"Result: {final_score}")