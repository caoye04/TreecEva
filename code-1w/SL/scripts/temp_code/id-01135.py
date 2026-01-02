def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) / len(adjusted) if adjusted else 0

productivity = [8, 7, 9, 4, 6]
risk_levels = [3, 5, 2, 8, 1]
baseline = 7.5

efficiency = analyze_efficiency(productivity)

# Simulate risk-weighted adjustment
temp_adjustments = []
for i, val in enumerate(risk_levels):
    if val < 4:
        temp_adjustments.append(1.2)
    elif val < 7:
        temp_adjustments.append(1.0)
    else:
        temp_adjustments.append(0.8)

risk_factor = 1.0
for adj in temp_adjustments:
    risk_factor *= adj

# Dummy calculations to increase cognitive load
buffer_zone = [x**2 for x in productivity if x < 6]
dummy_sum = sum(buffer_zone) * 0.05
dummy_flag = dummy_sum > 10

# Core logic disguised among other operations
normalized_productivity = sum(p * 1.1 for p in productivity) / len(productivity)
penalty = 0.0
for level in risk_levels:
    if level >= 8:
        penalty += 0.15
    elif level <= 2:
        penalty -= 0.05

adjusted_risk_factor = risk_factor - penalty

# Final evaluation using multiple concepts
def evaluate_performance(prod_scores, risk_adj):
    base = sum(prod_scores) / len(prod_scores)
    boost = 1.0 + (0.1 if base > baseline else -0.1)
    return int(base * boost * risk_adj)

intermediate_result = evaluate_performance(productivity, 1.0)
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")