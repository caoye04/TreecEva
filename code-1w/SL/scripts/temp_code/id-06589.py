def analyze_efficiency(metrics):
    adjusted = list(map(lambda x: (x + 1) ** 2, metrics))
    return sum(adjusted) // len(adjusted)

productivity = [3, 5, 7, 9, 4]
efficiency_index = analyze_efficiency(productivity)

# Irrelevant metric tracking (distractor)
countermeasures = {i: efficiency_index % i for i in range(2, 6)}
baseline_shift = sum(countermeasures.values()) / len(countermeasures)

# Risk assessment using set operations
tolerance_levels = {1, 3, 5, 7}
current_risks = {2, 4, 5, 6, 7}
risk_intersection = tolerance_levels & current_risks  # common elements
risk_factor = len(risk_intersection) * 1.5

# Auxiliary calculation with dictionary aggregation
weights = {'low': 1, 'med': 2, 'high': 3}
severity_map = dict(zip([1, 2, 3], ['low', 'med', 'high']))
impact_scores = [weights[severity_map[min(i, 3)]] for i in productivity]

# Secondary distraction: unused loop simulating load
simulated_load = 0
for _ in range(3):
    simulated_load += efficiency_index // (risk_factor + 1)

# Core logic masked by prior complexity
def evaluate_performance(p, r):
    base = sum(p) / len(p)
    penalty = r if r > 2 else 0
    bonus = 5 if all(x >= 3 for x in p) else 0
    return int(base - penalty + bonus)

interim_result = evaluate_performance(productivity, baseline_shift)  # red herring call

final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")