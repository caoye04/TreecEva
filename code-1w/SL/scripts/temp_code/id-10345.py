def analyze_efficiency(metrics):
    adjusted = list(map(lambda x: (x + 1e-5) ** 0.5, metrics))
    baseline = sum(adjusted) / len(adjusted)
    return baseline * 0.85

productivity = [85, 90, 78, 92, 88]
risk_metrics = [0.1, 0.3, 0.2, 0.5, 0.4]

# Distractor: Irrelevant transformation chain
temp_data = [x * 2 for x in productivity]
doubled_metrics = [y + 10 for y in temp_data]
shadow_copy = doubled_metrics.copy()

# Actual computation path begins
raw_efficiency = analyze_efficiency(productivity)
noise_level = sum([abs(a - b) for a, b in zip(risk_metrics[1:], risk_metrics[:-1])])
risk_factor = noise_level * 2.5

# Misleading intermediate calculation (dead-end)
theoretical_max = max(productivity) * 1.1
penalty_rate = 0 if theoretical_max > 100 else 0.05

# Core logic with conditional adjustment
if risk_factor < 1.0:
    risk_adjustment = 1.0
else:
    risk_adjustment = 1.5 if risk_factor > 2.0 else 1.2

adjusted_productivity = raw_efficiency * (1 - penalty_rate)

# Linear search for threshold (semi-relevant)
threshold_met = False
for val in productivity:
    if val >= 90:
        threshold_met = True
        break

bonus_eligibility = threshold_met and adjusted_productivity > 80

# Final evaluation using lambda-based weighting
evaluate_performance = lambda p, r: p - (r * risk_adjustment) + (5 if bonus_eligibility else 0)
final_score = evaluate_performance(adjusted_productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")