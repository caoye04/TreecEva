def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0.0
    if base_efficiency > 80:
        adjustment = 10.5
    elif base_efficiency > 60:
        adjustment = 5.2
    else:
        adjustment = -3.1
    return base_efficiency + adjustment

productivity_data = [75, 82, 90, 67, 71]

# Irrelevant transformation (distractor)
transformed_data = list(map(lambda x: x ** 0.5 * 2.1, productivity_data))

raw_average = sum(productivity_data) / len(productivity_data)
adjusted_productivity = analyze_efficiency(productivity_data)

# Dummy risk assessment with unused branches
risk_profile = {'low': 0.8, 'medium': 1.2, 'high': 1.8}
risk_factor = risk_profile['medium']

if raw_average < 70:
    risk_factor *= 1.1
else:
    temp_risk = 0.95  # Dead code path variable
    risk_factor *= 0.9  # Actually executed

# Unused set operations (distractor)
unique_metrics = set(productivity_data)
duplicate_check = {x for x in productivity_data if productivity_data.count(x) > 1}

# Core logic hidden among distractions
def evaluate_performance(p, r):
    performance_map = {i: i * 0.75 for i in range(50, 101)}
    base = performance_map.get(int(p), 60)
    penalty = 0
    if r >= 1.5:
        penalty = 8
    elif r >= 1.0:
        penalty = 4
    return int(base - penalty)

intermediate_result = adjusted_productivity * 0.87  # Not used directly

# Key execution point
final_score = evaluate_performance(raw_average, risk_factor)

print(f"Result: {final_score}")