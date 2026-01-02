def analyze_efficiency(metrics):
    adjustment_factor = 0.85
    base_rating = sum(metrics) / len(metrics)
    adjusted_rating = base_rating * adjustment_factor
    return adjusted_rating

productivity = [85, 90, 78, 92, 88]
overhead_costs = [1200, 1350, 1100, 1400, 1280]  # Irrelevant data
task_count = len(productivity)

# Misleading intermediate calculation
phantom_load = sum([x * 0.05 for x in overhead_costs])  # Dead computation

risk_factor = 1.2
penalty_weights = list(map(lambda x: x / max(productivity), productivity))
weighted_risk = risk_factor * sum(penalty_weights[:3])  # Partial use, slight distraction

# Simulate environmental impact (unused)
environment_index = 0
for i in range(len(productivity)):
    if productivity[i] > 80:
        environment_index += 0.3

# Key evaluation logic
performance_bonus = 10 if sum(productivity) > 400 else 5
base_score = analyze_efficiency(productivity)

# Multiple assignment that unpacks but only one part used
scaling_factor, _ = 1.1, 0.9

interim_result = base_score * scaling_factor + performance_bonus

# Final scoring with key statement
final_score = evaluate_performance(interim_result, weighted_risk)

# Redefine function to ensure clarity and correctness
def evaluate_performance(base_val, risk_adj):
    return int(base_val - risk_adj * 10)  # Deterministic integer result

# Recompute final score correctly after definition
final_score = evaluate_performance(interim_result, weighted_risk)

print(f"Result: {final_score}")