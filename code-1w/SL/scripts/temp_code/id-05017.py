def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 65, 45, 92, 88]
efficiency = analyze_efficiency(productivity)

# Distractor: irrelevant computation on same data
temp_weights = list(map(lambda x: (x / max(productivity)) ** 0.5, productivity))
weighted_sum = sum(temp_weights[:3]) * 10

# Risk assessment with nested logic and redundant checks
risk_levels = set()
risk_factor = 0
for val in productivity:
    if val < 60:
        risk_levels.add('low')
    elif val < 85:
        risk_levels.add('moderate')
    else:
        risk_levels.add('high')

if 'low' in risk_levels:
    risk_factor += 10
if len(risk_levels) > 2:
    risk_factor += 5

# Simulate conditional override (never triggers due to data)
critical_failure = any(x < 30 for x in productivity)
if critical_failure:
    efficiency = 0
    risk_factor = 100  # dead code path

# Secondary distractor: unused transformation
discounted_metrics = {i: v * 0.95 for i, v in enumerate(productivity)}

# Core evaluation logic with list comprehension and conditionals
def evaluate_performance(values, risk):
    base_score = sum(v for v in values if v >= 85)
    penalty = 0
    for v in values:
        if v < 70:
            penalty += 5
    # Additional adjustment based on efficiency bucket
    level_bonus = 0
    if efficiency > 80:
        level_bonus = 20
    elif efficiency > 60:
        level_bonus = 10
    
    # Final composition
    raw = base_score - penalty + level_bonus - risk
    return int(raw // 1.5)  # integer scaling

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")