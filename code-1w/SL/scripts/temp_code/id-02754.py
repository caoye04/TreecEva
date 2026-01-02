def analyze_efficiency(metrics):
    adjusted = []
    for val in metrics:
        if val > 70:
            adjusted.append(val * 0.9)
        elif val < 30:
            adjusted.append(val * 1.2)
        else:
            adjusted.append(val)
    return sum(adjusted) / len(adjusted)

productivity = [85, 45, 70, 55, 90]
baseline = [50, 60, 55, 65, 58]

# Irrelevant transformation chain (distractor)
temp_data = [x + 2 for x in baseline]
decay_factor = 0.95
deprecated_buffer = [round(x * decay_factor, 2) for x in temp_data]

# Real computation begins
avg_baseline = sum(baseline) / len(baseline)
efficiency_ratio = analyze_efficiency(productivity) / avg_baseline

# Simulate risk adjustment with string-based flags
risk_flags = ['low', 'MEDIUM', 'high']
risk_map = {'low': 0.1, 'MEDIUM': 0.25, 'high': 0.5}
risk_index = len(risk_flags) - 1

# Use string method to determine risk level
status_label = 'risk_assessment_final'.upper().replace('_', '')
is_valid = status_label.endswith('FINAL') and 'ASSESSMENT' in status_label

if is_valid:
    risk_factor = risk_map[risk_flags[risk_index % 2]]  # Deliberately avoids 'high'
else:
    risk_factor = 0.15

# Secondary distractor: unused tuple unpacking
total_risk, _, _ = (risk_factor * 2, risk_factor * 3, risk_factor * 4)

# Core logic: performance evaluation with mixed arithmetic and logical control
scale_factor = 1.5 if efficiency_ratio > 1.0 else 1.1
bonus_weight = 0.05 if 'MEDIUM' in risk_flags else 0.0

incentive_score = efficiency_ratio * scale_factor
penalty_adjustment = risk_factor * 10

# Final score computation
final_score = incentive_score * 100 - penalty_adjustment * 5

# Print required result
print(f"Result: {final_score}")