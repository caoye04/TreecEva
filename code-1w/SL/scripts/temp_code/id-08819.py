def calculate_performance(base, delta, limit):
    adjusted = base + delta * 1.5
    if adjusted > limit:
        penalty = (adjusted - limit) * 0.1
        adjusted -= penalty
    status = "optimal" if adjusted >= base else "suboptimal"
    flag = status.startswith('o')
    normalized = round(adjusted, 2)
    return normalized

baseline = 85.0
deviation = 12
deflection = 3.5  # irrelevant variable
threshold = 95.0
initial_check = baseline > 80  # side check

final_score = calculate_performance(baseline, deviation, threshold)
print(f"Target result: {final_score}")