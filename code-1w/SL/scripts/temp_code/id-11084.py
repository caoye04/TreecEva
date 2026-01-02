def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) / len(adjusted) if adjusted else 0

metrics_data = [4, 7, 9, 3, 8, 6]
efficiency_ratio = analyze_efficiency(metrics_data)

productivity = {}
risk_levels = ['low', 'medium', 'high']
base_values = [100, 85, 60]

for i, level in enumerate(risk_levels):
    productivity[level] = base_values[i] * efficiency_ratio

# Simulate auxiliary computation (distractor)
countermeasures = {lvl: val * 0.9 for lvl, val in productivity.items()}
buffer_zone = sum(countermeasures.values()) / 3

risk_factor = {
    'low': 0.1,
    'medium': 0.25,
    'high': 0.5
}

status_flags = []
for key in productivity:
    if productivity[key] > 80 and risk_factor[key] < 0.3:
        status_flags.append(True)
    else:
        status_flags.append(False)

# Irrelevant tracking variable (dead code path)
monitoring_state = any(status_flags) and not all(status_flags)

scaling_factor = 1.5
penalty_offset = 10

# Core logic with distraction from above
intermediate_scores = []
for k in productivity:
    raw = productivity[k]
    risk_adj = risk_factor[k]
    score = (raw * scaling_factor) - (penalty_offset * risk_adj)
    intermediate_scores.append(score)

# Misleading aggregation
shadow_score = sum([s * 0.8 for s in intermediate_scores])

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Helper function defined after use (adds cognitive load)
def evaluate_performance(prod, risk):
    total = 0.0
    count = 0
    for level in prod:
        if level in risk:
            contribution = prod[level] * (1 - risk[level])
            total += contribution
            count += 1
    return int(total / count) if count else 0

print(f"Result: {final_score}")