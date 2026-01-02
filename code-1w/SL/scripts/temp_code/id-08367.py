def analyze_efficiency(metrics):
    adjustment_factor = 0.85
    base_efficiency = sum(metrics) / len(metrics)
    if base_efficiency > 70:
        return base_efficiency * adjustment_factor
    else:
        return base_efficiency * (adjustment_factor + 0.1)

productivity = [80, 92, 75, 88, 95]
overhead_costs = [1200, 1400, 1350, 1500, 1300]

# Irrelevant aggregation (distractor)
total_cost = sum(overhead_costs)
avg_cost = total_cost / len(overhead_costs)
adjusted_metrics = list(map(lambda x: x * 0.95, productivity))

# Real computation begins
raw_efficiency = analyze_efficiency(productivity)
decay_rate = 0.02
risk_factor = 0
for i, val in enumerate(productivity):
    if val < 85:
        risk_factor += decay_rate * (85 - val)

# Misleading intermediate calculation (semi-relevant but not used directly)
temp_score = raw_efficiency - (risk_factor * 10)
buffer_zone = 5.0  # Unused buffer (distractor)

# Core evaluation using lambda and conditional logic
evaluate_performance = lambda perf, risk: (
    perf - risk * 8 if perf > 80 
    else perf - risk * 12
)

final_score = evaluate_performance(raw_efficiency, risk_factor)

# Additional red herring: unused function
def calculate_stress_index(values):
    return max(values) - min(values)

# Print result as required
print(f"Result: {final_score}")