def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = (lambda x: x ** 0.5 if x > 20 else x / 2)(base_efficiency)
    return adjustment

metrics_data = [4, 7, 3, 8, 5]

# Irrelevant transformation (distractor)
transformed_data = [x ** 2 for x in metrics_data if x % 2 == 1]
shadow_metric = len(transformed_data) * 2.5

efficiency = analyze_efficiency(metrics_data)

productivity = efficiency * 3.7
risk_levels = {'low': 1, 'med': 2, 'high': 3}
risk_factor = risk_levels['med']

# Dummy calculation chain (semi-relevant but not used directly)
temp_weights = {i: productivity / (i + 1) for i in range(1, 4)}
proxy_risk = sum(temp_weights.values()) / risk_factor

unused_correction = proxy_risk * 0.8 if efficiency > 30 else 0

# Core logic hidden among distractions
def evaluate_performance(p, r):
    if p < 50:
        return int(p - r * 3)
    else:
        return int(p + r * 2)

final_score = evaluate_performance(productivity, risk_factor)

# Print required result
print(f"Result: {final_score}")