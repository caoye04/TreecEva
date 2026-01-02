def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    baseline = sum(metrics) / len(metrics)
    bonus = len([x for x in adjusted if x > baseline]) * 2
    return bonus

productivity = [8, 6, 4, 9, 7]
risk_levels = {1: 'low', 2: 'medium', 3: 'high'}
task_complexity = {'alpha': 3, 'beta': 7, 'gamma': 5}

# Irrelevant data structure manipulation
distraction_set = set(task_complexity.values())
complement_set = {1, 2, 3, 4, 5} - {x for x in range(3, 6) if x % 2 == 1}
side_calc = len(distraction_set) * max(complement_set)

# Dummy transformation chain
intermediate_vals = list(map(lambda x: x ** 2 - x, productivity))
filtered_intermediates = [val for val in intermediate_vals if val > 10]
phantom_score = sum(filtered_intermediates) // 3 if filtered_intermediates else 0

risk_factor = 0
for key, value in task_complexity.items():
    if value > 4:
        risk_factor += value // 2
        if value == 7:
            risk_factor += 1

# Simulated efficiency analysis (not used but looks relevant)
efficiency_boost = analyze_efficiency(productivity)
legacy_mode = False

# Core logic disguised among distractors
base_performance = sum(productivity)
penalty = 0
if risk_factor > 5:
    penalty = base_performance * 0.1
else:
    penalty = base_performance * 0.05

normalized_risk = risk_factor / 10.0
evaluation_weights = [0.7, 0.3]

# Final computation
weighted_productivity = base_performance * evaluation_weights[0]
risk_adjustment = normalized_risk * 100 * evaluation_weights[1]

final_score = weighted_productivity + risk_adjustment - penalty

# Red herring: unused but plausible-looking aggregation
consistency_check = all(p >= 6 for p in productivity if p != 9)
shadow_metric = (sum(productivity) + risk_factor) // len(productivity)

Result: final_score