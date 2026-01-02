def analyze_efficiency(metrics):
    if not metrics:
        return 0
    base = sum(metrics) / len(metrics)
    adjustment = 0
    for val in metrics:
        if val > base:
            adjustment += 0.1
        elif val < base:
            adjustment -= 0.05
    return base + adjustment

productivity = [85, 90, 78, 92, 88]
safety_record = [95, 87, 85, 90, 93]
overhead_costs = [200, 210, 195, 220, 205]

# Distractor: unused function
def calculate_budget_variance(planned, actual):
    variance = 0
    for p, a in zip(planned, actual):
        variance += (a - p) ** 2
    return variance ** 0.5

# Irrelevant computations
avg_cost = sum(overhead_costs) / len(overhead_costs)
total_safety_incidents = sum([100 - s for s in safety_record if s < 90])

risk_factor = 0
if any(cost > 200 for cost in overhead_costs):
    risk_factor += 1.5
if len(safety_record) > 4:
    risk_factor += 0.5

# Conditional expression and dictionary usage
efficiency_band = {
    (0, 80): 'Low',
    (80, 90): 'Moderate',
    (90, 100): 'High'
}

efficiency_label = None
avg_productivity = analyze_efficiency(productivity)
for (low, high), label in efficiency_band.items():
    if low <= avg_productivity < high:
        efficiency_label = label
        break

# Semi-relevant transformation
temp_score = avg_productivity * 1.1 if efficiency_label == 'High' else avg_productivity * 0.95

# Key computation with distractors
bonus_multiplier = 1.0
if efficiency_label == 'High' and risk_factor < 2:
    bonus_multiplier = 1.2

intermediate_result = temp_score * bonus_multiplier

# Final evaluation using dictionary lookup and conditional logic
def evaluate_performance(prod, risk):
    base_score = sum(prod) / len(prod)
    penalty = 10 if risk > 1.8 else 5
    # Additional distraction inside function
    shadow_metrics = [p * 0.98 for p in prod if p > 80]
    adjustment = len(shadow_metrics) * 0.5
    return base_score - penalty + adjustment

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")