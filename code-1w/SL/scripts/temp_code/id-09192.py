def analyze_efficiency(metrics):
    base_effort = sum(metrics) * 0.85
    adjustment = (max(metrics) - min(metrics)) * 0.15
    return base_effort + adjustment

productivity = [80, 92, 78, 95, 88]
risk_factor = [0.9, 1.1, 0.8, 1.2, 1.0]

# Irrelevant preprocessing (distractor)
temp_data = [x ** 2 for x in productivity if x > 85]
shadow_index = sum(temp_data) // len(temp_data) if temp_data else 0

# Semi-relevant transformation
weighted_productivity = list(map(lambda x: x * 1.05, productivity))
adjusted_risk = [max(0.5, min(2.0, 1.1 * r)) for r in risk_factor]

# Misleading intermediate calculation
dummy_score = 0
for val in adjusted_risk:
    if val > 1.0:
        dummy_score += 10
    elif val < 1.0:
        dummy_score -= 5

# Core logic obscured by surrounding noise
performance_index = analyze_efficiency(weighted_productivity)
penalty_rate = sum(adjusted_risk) / len(adjusted_risk)

# Key decision logic with conditional expression
scaling_factor = 1.2 if penalty_rate < 1.1 else 0.9
bonus_applied = True if performance_index > 350 else False

# Final computation involving multiple concepts
evaluate_performance = lambda p, r: int((sum(p) / 10) * scaling_factor - (sum(r) * 10)) + (50 if bonus_applied else 0)
final_score = evaluate_performance(productivity, risk_factor)

# Dead code path (distractor)
if shadow_index > 10000:
    final_score *= 2

# Output result as required
print(f"Result: {final_score}")