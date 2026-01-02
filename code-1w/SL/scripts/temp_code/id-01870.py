def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics) if metrics else 0
    adjusted = [x * 1.1 for x in metrics if x > baseline]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 92, 88]
risk_levels = [3, 1, 4, 2, 5]
department_codes = ['A', 'B', 'C', 'D', 'E']

# Irrelevant pre-processing (distractor)
temp_data = {dept: val * 2 for dept, val in zip(department_codes, risk_levels)}
smoothed_risk = [max(r - 1, 1) for r in risk_levels]

# Semi-relevant transformation
risk_factor = sum(smoothed_risk) / len(smoothed_risk)
productivity_index = analyze_efficiency(productivity)

# Conditional adjustment based on risk threshold
risk_adjustment = 1.05 if risk_factor <= 2.5 else 0.95

# Core evaluation logic
performance_rating = productivity_index * risk_adjustment

# Final scoring with conditional expression
final_score = performance_rating if performance_rating >= 80 else performance_rating * 0.8

# Dead code path (distractor)
if False:
    final_score += 10
    buffer = [i ** 2 for i in range(10)]

# Unused intermediate calculation (distractor)
redundant_metric = sum([p // r for p, r in zip(productivity, risk_levels)])

Result: final_score