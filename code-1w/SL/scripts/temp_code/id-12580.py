def analyze_efficiency(metrics):
    weights = [0.2, 0.3, 0.5]
    efficiency = sum(w * m for w, m in zip(weights, metrics))
    adjustment = 0.9 if efficiency > 70 else 1.1
    return efficiency * adjustment

productivity_data = [80, 65, 90]
overhead_cost = 1250

# Simulate environmental load (distractor)
environmental_factor = 1.05
baseline_stress = 42
adjusted_stress = baseline_stress * environmental_factor

# Irrelevant financial projection (dead code path)
projected_revenue = 0
if overhead_cost < 1000:
    projected_revenue = 20000
else:
    projected_revenue = 15000  # This doesn't affect final result

# Core logic disguised with auxiliary computations
raw_efficiency = analyze_efficiency(productivity_data)
penalty_rate = 0.05 if raw_efficiency < 75 else 0.02
risk_factor = (raw_efficiency * penalty_rate) + 10

# Dummy data structure for distraction
status_log = {
    'timestamp': '2023-11-05',
    'level': 'critical',
    'value': adjusted_stress
}

# Secondary helper to obscure main flow
compute_margin = lambda x, y: (x - y) * 0.1

margin_buffer = compute_margin(raw_efficiency, penalty_rate * 100)

# Additional red herring calculation
phantom_metric = 0
for i in range(3):
    phantom_metric += productivity_data[i] % 7

# Actual performance evaluation
productivity = raw_efficiency + margin_buffer

# Key statement containing target variable
final_score = evaluate_performance(productivity, risk_factor)

# Definition inserted after usage to increase cognitive load
def evaluate_performance(eff, risk):
    base = eff - risk
    if base > 80:
        return base * 1.2
    elif base > 60:
        return base * 1.1
    else:
        return base * 0.9

print(f"Result: {final_score}")