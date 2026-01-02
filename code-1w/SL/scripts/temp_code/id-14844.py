def analyze_efficiency(base_rate, overhead):
    return lambda x: base_rate * x - overhead

# Simulate employee performance metrics
task_completion = 42
hours_worked = 8.5
base_productivity = task_completion / hours_worked

# Risk adjustment factors
risk_factor = 0.87
penalty_curve = lambda r: r ** 2 if r > 0.8 else r
adjusted_risk = penalty_curve(risk_factor)

# Distractor: Irrelevant financial calculations
project_budget = 150000
unrelated_expense = 3745
budget_utilization = project_budget / (unrelated_expense + 1)  # Not used later

# Secondary distractor: Unused helper function
def calculate_revenue(units, price_per_unit):
    return units * price_per_unit

# Complex productivity scoring with conditional logic
productivity = 0
if base_productivity >= 5:
    productivity += 10
else:
    productivity += 5

productivity += 2 if adjusted_risk < 0.9 else -1

# Nested condition to adjust for workload intensity
workload_intensity = task_completion * 1.2 / (hours_worked + 1)
if workload_intensity > 5:
    if adjusted_risk > 0.85:
        productivity += 3
    else:
        productivity -= 2
else:
    productivity += 1

# Evaluate final performance score using lambda-based analyzer
efficiency_model = analyze_efficiency(1.15, 0.4)
score_component = efficiency_model(productivity)

# Final decision logic with conditional expression
final_score = 0
final_score = evaluate_performance(productivity, risk_factor) if 'score_component' in locals() else -1

def evaluate_performance(p, r):
    base = p * 7.5
    risk_penalty = 10 * (1 - r)
    return int(base - risk_penalty)  # Deterministic integer result

Result: {final_score}