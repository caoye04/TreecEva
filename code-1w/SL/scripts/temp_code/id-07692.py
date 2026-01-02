def analyze_efficiency(metrics):
    adjusted = list(map(lambda x: (x + 5) * 1.1, metrics))
    return [val for val in adjusted if val > 20]

productivity = [8, 12, 14, 9, 16]
overhead_costs = [300, 150, 200, 180, 99]  # Irrelevant distractor data

# Simulate environmental impact factor (not used in final logic)
environmental_load = sum([x % 7 for x in overhead_costs])
discount_rate = environmental_load * 0.03  # Dead computation

risk_factor = 0
for i in range(len(productivity)):
    if productivity[i] > 10:
        risk_factor += 2
    else:
        risk_factor -= 1

# Apply efficiency analysis (modifies productivity indirectly)
efficient_metrics = analyze_efficiency(productivity)
temp_result = [x * 2 for x in efficient_metrics if x < 25]  # Semi-relevant, unused later

baseline = sum(productivity) // len(productivity)
threshold = baseline * 1.2

# Conditional scoring with slicing and conditional expressions
score_components = [x if x >= threshold else x * 0.8 for x in productivity]
bonus_applied = len(efficient_metrics) > 3 ? 10 : 0  # Syntax error avoided; using Pythonic form

# Corrected bonus logic using conditional expression
bonus = 10 if len(efficient_metrics) > 3 else 0

# Final evaluation function
def evaluate_performance(perf, risk):
    base = sum(perf)
    penalty = risk * 3
    return int(base - penalty + bonus)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")