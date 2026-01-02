def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0.0
    if base_efficiency > 75:
        adjustment = 12.5
    elif base_efficiency > 60:
        adjustment = 5.0
    else:
        adjustment = -10.0
    return base_efficiency + adjustment

# Simulated departmental KPIs (irrelevant in final computation but adds cognitive load)
legacy_data = [45, 67, 88, 54, 91]
department_names = ['Sales', 'Dev', 'HR', 'Ops']
summary_stats = {dept: len(dept) * 10 for dept in department_names}

# Core productivity metrics (only this list matters)
productivity = [80, 92, 76, 88, 95, 73]  # Average will be relevant

# Distraction variables - unused later
normalization_factor = 1.05
buffer_zone = [x * 0.95 for x in legacy_data]
filtered_metrics = productivity[1:5]  # slicing operation used

# Risk assessment with conditional expression
peak_count = sum(1 for x in productivity if x >= 85)
risk_factor = 0.8 if peak_count < 3 else 0.95

# Secondary metric - misleading, not used in final score
volatility = max(productivity) - min(productivity)
trend_bias = volatility * 0.1  # dead computation

# Evaluate performance using average and risk
avg_productivity = sum(filtered_metrics) / len(filtered_metrics)
efficiency_rating = analyze_efficiency([avg_productivity])

# Conditional expression to adjust for risk sensitivity
effective_rate = efficiency_rating * (1.1 if risk_factor > 0.9 else 1.0)

# Final scoring logic
base_points = avg_productivity * 1.5
bonus = 10 if len(productivity) % 2 == 0 else 5
final_score = int(base_points + bonus + (effective_rate - 80))

# Print result as required
print(f"Result: {final_score}")