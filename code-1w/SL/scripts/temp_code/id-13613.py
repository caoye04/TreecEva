def analyze_efficiency(metrics):
    weighted_sum = sum(m * (i + 1) for i, m in enumerate(metrics))
    adjustment = len(metrics) ** 0.5
    return weighted_sum / adjustment if adjustment != 0 else 0

productivity = [7, 5, 8, 6, 9]
risk_levels = [2, 4, 3, 5, 2, 4, 3]

# Irrelevant helper that's defined but not used in final path
def assess_stability(readings):
    base = sum(1 for r in readings if r > 3)
    penalty = 0
    for r in readings:
        if r == 4:
            penalty += 0.5
        elif r == 5:
            penalty += 1.0
    return base - penalty

# Distractor variables
temp_flux = [x * 1.5 for x in risk_levels if x % 2 == 0]
aggregate_risk = sum(risk_levels) / len(risk_levels)
dummy_matrix = [[i + j for j in range(3)] for i in range(3)]

# Unused lambda — adds interference
risk_validator = lambda x: True if 1 <= x <= 5 else False
valid_risks = list(filter(risk_validator, risk_levels))

# Core logic with relevant computation
baseline_effort = sum(productivity) / len(productivity)
efficiency_score = analyze_efficiency(productivity)

# Secondary processing with set operations (required feature)
unique_productivity = set(productivity)
boost_elements = {8, 9}
if boost_elements.issubset(unique_productivity):
    efficiency_score *= 1.2

# Risk-based modifier
high_risk_count = len([r for r in risk_levels if r >= 4])
risk_factor = 1.0 - (high_risk_count / len(risk_levels)) * 0.3

# Final evaluation using lambda (required feature)
evaluate_performance = lambda perf, risk: int((perf * 0.7 + 10 * efficiency_score * 0.3) * risk)

# Key statement
final_score = evaluate_performance(productivity[0], risk_factor)

print(f"Result: {final_score}")