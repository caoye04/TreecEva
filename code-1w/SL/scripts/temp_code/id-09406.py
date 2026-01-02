def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics)
    adjusted = [x * 1.1 if x < baseline else x * 0.95 for x in metrics]
    return sum(adjusted) / len(adjusted)

risk_profile = lambda r: 'high' if r > 0.7 else 'low'

productivity_data = [0.82, 0.71, 0.93, 0.64, 0.88]
risk_factors = [0.55, 0.81, 0.67, 0.92, 0.44]

# Distractor: irrelevant transformation
temp_weights = list(map(lambda x: round(x**2, 3), risk_factors))
weight_sum = sum(temp_weights[:3])  # Dead-end computation

# Real logic begins
avg_productivity = analyze_efficiency(productivity_data)
significant_risks = [r for r in risk_factors if r > 0.7]
high_risk_count = len(significant_risks)

risk_factor = high_risk_count / len(risk_factors)

status_label = risk_profile(risk_factor)

# Conditional expression with side relevance
efficiency_bonus = 1.2 if avg_productivity > 0.8 else 1.0
penalty_rate = 0.85 if status_label == 'high' else 1.0

# Core evaluation
def evaluate_performance(p, r):
    base = p * 100
    adjustment = (1 - r) * 20
    score = base * efficiency_bonus - adjustment * 10
    if r > 0.5:
        score *= penalty_rate
    return round(score, 2)

# Key statement
final_score = evaluate_performance(avg_productivity, risk_factor)

# Irrelevant string processing distraction
diagnostic_log = "Performance scan: complete"
log_status = diagnostic_log.upper().replace(":", " ->").split(" -> ")
meta_flag = "SCAN" in log_status[0]

# Final output
Result: {final_score}