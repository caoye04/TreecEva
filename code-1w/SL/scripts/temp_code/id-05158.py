def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) / len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 92, 88, 76, 95]
overhead_costs = [23, 45, 12, 67, 34, 56, 78]

# Distractor: irrelevant financial adjustment
cost_multiplier = 1.07
adjusted_costs = list(map(lambda x: x * cost_multiplier, overhead_costs))
total_adjusted_cost = sum(adjusted_costs)

# Real computation begins
baseline = sum(productivity) / len(productivity)
variance = sum((x - baseline) ** 2 for x in productivity) / len(productivity)
std_dev = variance ** 0.5

# Use of enumerate and zip (required python features)
efficiency_pairs = list(zip(productivity, overhead_costs))
risk_indicators = []
for i, (prod, cost) in enumerate(efficiency_pairs):
    if i % 2 == 0:
        risk_indicators.append(cost / (prod + 1) * 100)
    else:
        risk_indicators.append((cost + 5) / (prod + 10) * 100)

risk_factor = sum(risk_indicators[:len(risk_indicators)//2])

# Simulate historical comparison (distractor)
historical_benchmark = [80, 85, 75, 90, 82]
drift_scores = []
for h in historical_benchmark:
    drift = abs(h - baseline)
    drift_scores.append(drift)
mean_drift = sum(drift_scores) / len(drift_scores)

# Set operation (required feature): identify high performers
high_performers = set(p for p in productivity if p >= 85)
low_risk_indices = {i for i, r in enumerate(risk_indicators) if r < 40}
consistent_staff = high_performers & set(productivity[i] for i in low_risk_indices)

# Secondary distractor: unused sorting
sorted_productivity = sorted(productivity, reverse=True)
sorted_with_index = list(enumerate(sorted_productivity))

# Core logic with nested dependency
def adjust_for_risk(base, risks):
    total_risk = sum(risks)
    if total_risk > 150:
        return base * 0.85
    elif total_risk > 100:
        return base * 0.9
    else:
        return base * 0.95

def evaluate_performance(prods, risk_vals):
    avg_perf = sum(prods) / len(prods)
    adjusted_avg = adjust_for_risk(avg_perf, risk_vals)
    efficiency_bonus = analyze_efficiency(prods)
    final_value = adjusted_avg + (efficiency_bonus * 0.1)
    return int(final_value)

# Key assignment statement
temp_result = analyze_efficiency(productivity)
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")