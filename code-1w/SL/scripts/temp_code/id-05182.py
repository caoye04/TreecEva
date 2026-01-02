def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [45, 70, 80, 60, 90]

baseline = [p * 0.95 for p in productivity]
decay_factor = 0.9
projected = []
for val in baseline:
    projected.append(val * decay_factor)

# Irrelevant transformation on projections
temp_analysis = [round(p + 10) for p in projected if p < 65]

aggregate = sum(productivity) + sum(projected)
scale_factor = aggregate / 1000

status_flags = {i: 'active' if p >= 70 else 'review' for i, p in enumerate(productivity)}
high_performers = [i for i, p in status_flags.items() if p == 'active']

utilization_rate = len(high_performers) / len(productivity)

risk_pool = set(range(10, 100, 7))
penalty_set = {x for x in risk_pool if x % 3 == 0}
bonus_set = {x for x in risk_pool if x % 5 == 0}
risk_set = penalty_set.symmetric_difference(bonus_set)

# Dummy tracking of fluctuations
fluctuation_log = []
for i in range(len(productivity)):
    diff = abs(productivity[i] - (projected[i] if i < len(projected) else 0))
    fluctuation_log.append(diff // 10)

# Auxiliary scoring with red herring
aux_scores = []
for p in productivity:
    if p > 75:
        aux_scores.append(p * 0.8)
    elif p > 60:
        aux_scores.append(p * 0.6)
    else:
        aux_scores.append(p * 0.4)

mean_aux = sum(aux_scores) / len(aux_scores) if aux_scores else 0

# Core evaluation logic
threshold = analyze_efficiency(productivity)
efficient_count = len([p for p in productivity if p > threshold])

scaling_modifier = utilization_rate * (efficient_count / len(productivity))

raw_score = sum(productivity) * scaling_modifier

penalties = len(risk_set.intersection(set(productivity)))
bonuses = len(bonus_set.intersection(set(productivity)))

final_score = int(raw_score - (penalties * 5) + (bonuses * 3))

Result: final_score