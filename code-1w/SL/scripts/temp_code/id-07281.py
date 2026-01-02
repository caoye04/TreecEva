def evaluate_performance(output, risk):
    base_score = output * 1.5
    penalty = 0
    if risk > 0.5:
        penalty = base_score * 0.3
    elif risk < 0.2:
        penalty = base_score * 0.1
    return int(base_score - penalty)

# Simulate team performance metrics
team_data = {'alpha': 85, 'beta': 90, 'gamma': 78}
productivity = sum(team_data.values()) / len(team_data)

# Calculate risk factor using bitwise and arithmetic operations
temp_a = 23
temp_b = 17
dummy_mask = (temp_a & temp_b) ^ 5
risk_numerator = (temp_a ^ temp_b) + (temp_a >> 2)
risk_denominator = temp_b + (temp_a << 1)
risk_factor = risk_numerator / risk_denominator

# Irrelevant string processing (distractor)
status_report = "Performance review Q3: Stable"
keywords = status_report.lower().split(':')
flag = any('stable' in kw for kw in keywords)

# Dummy dictionary operations (semi-relevant)
score_map = {k: v * 1.1 for k, v in team_data.items()}
avg_boosted = sum(score_map.values()) / len(score_map)

# Core computation with lambda (used for adjustment)
adjustment_func = lambda x: x * 0.95 if x > 80 else x * 1.05
adjusted_productivity = adjustment_func(productivity)

# Final evaluation step
final_score = evaluate_performance(productivity, risk_factor)

# Print result
print(f"Result: {final_score}")