def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 65, 45, 92, 88]
overhead = [p * 0.05 for p in productivity]
dummy_calc = sum([x**2 for x in overhead])

baseline = 80
risk_factor = 0
for val in productivity:
    if val < baseline:
        risk_factor += 1
    elif val >= 90:
        risk_factor -= 1

risk_factor = max(0, risk_factor)

# Simulate auxiliary diagnostic pass
status_codes = []
for i in range(len(productivity)):
    code = 1 if productivity[i] > 85 else 0
    status_codes.append(code)

trigger_count = sum(status_codes)
threshold_met = trigger_count >= 3

interim = analyze_efficiency(productivity)

scaling_modifier = 1.2 if threshold_met else 0.9

projected = interim * scaling_modifier

buffer_zone = [projected * 0.1, projected * 0.05]

penalty = buffer_zone[1] if risk_factor > 2 else 0

final_score = 0
def evaluate_performance(efficiency, risk):
    global penalty
    base = efficiency - (risk * 5)
    if base < 60:
        return 60
    return int(base - penalty)

final_score = evaluate_performance(projected, risk_factor)

print(f"Result: {final_score}")