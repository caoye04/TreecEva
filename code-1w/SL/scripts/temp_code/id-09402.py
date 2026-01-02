def evaluate_performance(metrics, base):
    adjustment = 0
    temp_result = []
    
    # Irrelevant preprocessing: normalize unused values
    normalized = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]
    avg_normalized = sum(normalized) / len(normalized)

    # Real logic begins: identify key deviations
    significant = {m for m in metrics if abs(m - base) > 15}
    minor = {m for m in metrics if m <= base}

    # Misleading secondary path: dead computation on subset
    if len(significant) > 2:
        offset = sum([s % 7 for s in significant]) // 2
    else:
        offset = base // 3  # Not actually impactful due to fixed input

    # Core calculation chain
    growth_trend = 0
    for i, val in enumerate(metrics):
        if val > base:
            growth_trend += (val - base) * 1.5
        elif val < base:
            growth_trend -= (base - val) * 0.8

    # Conditional bonus based on set symmetry
    mirrored = {base + (base - m) for m in minor}
    overlap = len(significant & mirrored)

    incentive = 0
    if overlap >= 1:
        incentive = 25

    # Auxiliary tracking: irrelevant counter
    step_counter = 0
    for _ in range(len(metrics)*2):
        step_counter += 1  # Distractor: simulates workload

    # Final composition
    raw_score = growth_trend + incentive
    penalty = len([x for x in metrics if x < 70]) * 5
    final_score = int(raw_score - penalty + offset)

    return final_score

# Input data
baseline = 85
metric_set = [92, 88, 67, 95, 71, 84]

# Execution point
final_score = evaluate_performance(metric_set, baseline)
print(f"Result: {final_score}")