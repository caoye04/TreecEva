def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) / len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 65, 45, 92]
overhead_costs = [x * 0.05 for x in productivity]  # Distractor: not used later
baseline = sum(p // 10 for p in productivity)  # Semi-relevant, used in risk_factor

# Simulate environmental fluctuations (distraction)
env_noise = 0
for i in range(len(productivity)):
    env_noise += (i + 1) * 0.01

risk_factor = baseline * 0.8 + env_noise  # Minor influence via baseline

# Conditional adjustment based on threshold logic
if risk_factor < 30:
    risk_factor += 5
else:
    temp_offset = [x for x in overhead_costs if x > 4.0]  # Dead-end computation
    risk_factor += len(temp_offset) * 0.2

# Core evaluation function
def evaluate_performance(efficiency_data, penalty):
    base_performance = analyze_efficiency(efficiency_data)
    adjustment = 0
    for val in efficiency_data:
        if val > 80:
            adjustment += 2
        elif val > 70:
            adjustment += 1
    # Apply non-linear scaling
    final_value = (base_performance + adjustment) * (1 - penalty / 100)
    return round(final_value, 4)

# Key statement
temp_result = evaluate_performance(productivity, 0)  # Unused warm-up call
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")