def analyze_efficiency(output, overhead):
    base_efficiency = output / (overhead + 1)
    penalty = 0.1 if output < 50 else 0
    adjusted = base_efficiency - penalty * base_efficiency
    return adjusted

risk_assessment = lambda x: 2 * x + 1 if x > 10 else x // 2

productivity_data = [45, 60, 30, 80]
overhead_costs = [8, 12, 5, 15]
efficiency_list = []

for i in range(len(productivity_data)):
    score = analyze_efficiency(productivity_data[i], overhead_costs[i])
    efficiency_list.append(score)

aggregated_output = sum(productivity_data)
total_overhead = sum(overhead_costs)
avg_efficiency = sum(efficiency_list) / len(efficiency_list)

# Misleading intermediate calculations
theoretical_max = 100 * len(productivity_data)
waste_ratio = (theoretical_max - aggregated_output) / theoretical_max
dummy_metric = (aggregated_output - total_overhead) * 0.5  # Not used later

# Simulate risk based on average efficiency
if avg_efficiency > 4.0:
    risk_level = 5
else:
    risk_level = 15

risk_factor = risk_assessment(risk_level)

# Core logic for final evaluation
def evaluate_performance(prod, risk):
    normalized_prod = prod / 100.0
    adjustment = 1 - (risk * 0.01)
    performance_index = normalized_prod * adjustment
    bonus = 0.05 if performance_index > 0.3 else 0
    return int((performance_index + bonus) * 100)

final_score = evaluate_performance(aggregated_output, risk_factor)
print(f"Result: {final_score}")