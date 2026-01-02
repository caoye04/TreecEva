def analyze_efficiency(metrics):
    efficiency = sum(metrics) / len(metrics) if metrics else 0
    adjusted = efficiency * 1.2 if efficiency > 75 else efficiency * 0.9
    return adjusted

productivity = [85, 90, 78, 92, 88]
overhead_costs = [15, 20, 18, 25, 22]  # Distractor list

efficiency_score = analyze_efficiency(productivity)
baseline_risk = 1.05
risk_factor = {
    'market': 1.1,
    'operations': 0.95,
    'regulatory': 1.02
}

# Irrelevant computation on overhead (distractor)
total_overhead = sum(overhead_costs)
avg_overhead = total_overhead / len(overhead_costs)
projected_savings = avg_overhead * 0.15  # Dead code path

# Simulate conditional adjustment using dictionary values
if efficiency_score > 85:
    risk_factor['operations'] *= 0.9
    risk_factor['market'] += 0.05
else:
    risk_factor['regulatory'] *= 1.1

# Compute exposure set from risk keys (semi-relevant)
exposure_areas = set(risk_factor.keys())
critical_exposure = {k: v for k, v in risk_factor.items() if v >= 1.0}

# Complex conditional expression combining arithmetic and dict lookup
multiplier = 0.8 if 'compliance' in exposure_areas else (1.1 if len(critical_exposure) > 2 else 1.05)

# Core logic embedded among distractions
temp_val = efficiency_score + sum(risk_factor.values())
raw_performance = temp_val * multiplier

# Final evaluation function with nested logic
def evaluate_performance(prod_data, risks):
    base = sum(prod_data) / len(prod_data)
    risk_penalty = sum(risks.values()) - len(risks)
    if base > 80:
        if risk_penalty < 0.5:
            return int(base - risk_penalty * 10)
        else:
            return int(base - risk_penalty * 5)
    else:
        return int(base - risk_penalty * 8)

final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Target result: {final_score}")