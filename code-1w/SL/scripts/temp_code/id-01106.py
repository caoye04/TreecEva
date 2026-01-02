def evaluate_performance(output, risk):
    base_efficiency = 85
    adjustment = (lambda x: x * 1.2 if x > 70 else x * 0.9)(output)
    safety_margin = 100 - risk
    return adjustment + safety_margin

# Irrelevant metric (distractor)
baseline = 75

productivity = 78
risk_factor = 15

# Conditional expression for secondary validation (not used in final result)
status = 'optimal' if productivity >= 75 and risk_factor <= 20 else 'review'

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")