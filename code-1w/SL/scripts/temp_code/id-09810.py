def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = len(metrics) if base_efficiency > 50 else 0
    return base_efficiency + adjustment

productivity = [4, 7, 6, 8, 5]
overhead = [x ** 0.5 for x in productivity]
dummy_calc = [y * 2 for y in overhead if y < 2.5]

# Simulate system load interference
temp_buffer = []
for val in productivity:
    temp_buffer.append(val % 3)
status_flags = set(temp_buffer)

risk_levels = {1: 'high', 2: 'medium', 3: 'low'}
risk_counter = {k: 0 for k in risk_levels}

for p in productivity:
    if p < 5:
        risk_counter[1] += 1
    elif p < 7:
        risk_counter[2] += 1
    else:
        risk_counter[3] += 1

# Misleading aggregation
aggregate_risk = 0
for key in risk_counter:
    if risk_levels[key] == 'high':
        aggregate_risk -= risk_counter[key]
    else:
        aggregate_risk += risk_counter[key] * (key - 1)

risk_factor = abs(aggregate_risk) + 1

# Core logic with distractors
baseline = analyze_efficiency(productivity)
penalty = 0
if len(dummy_calc) > 2:
    penalty = sum(dummy_calc)
else:
    penalty = 5

adjusted_baseline = baseline - penalty

# Red herring function
def compute_headroom(data):
    peak = max(data)
    avg = sum(data) / len(data)
    return (peak - avg) * len(data)

headroom_value = compute_headroom(productivity)  # Not used later

irrelevant_set = {x for x in range(len(productivity))}
side_metric = len(irrelevant_set.intersection(status_flags))

# Final evaluation chain
def evaluate_performance(efficiency_series, risk):
    raw_score = sum(efficiency_series) + len(efficiency_series)
    modifier = 2 if risk > 3 else 1
    noise_offset = side_metric * 0.5  # Unused in integer logic
    final_value = raw_score // modifier
    if final_value % 2 == 0:
        final_value += risk
    return final_value

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")