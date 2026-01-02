def evaluate_performance(data, importance):
    # Irrelevant transformation (distractor)
    adjusted_data = [x * 1.05 for x in data]
    temp_result = sum([x ** 0.5 for x in adjusted_data if x > 50])

    # Core logic disguised among noise
    normalized = list(map(lambda x: x / 100.0, data))
    weighted_vals = [n * w for n, w in zip(normalized, importance)]
    
    # Dead code path (misleading control flow)
    if len(weighted_vals) > 10:
        scaling_factor = 1.2
    else:
        scaling_factor = 1.0  # Never used
    
    # Secondary distractor: unused accumulation
    cumulative_shift = 0
    for i in range(len(weighted_vals)):
        if i % 2 == 0:
            cumulative_shift += weighted_vals[i] * 0.1

    # Actual critical computation
    base_score = sum(weighted_vals) * 100
    penalty = 0
    for val in normalized:
        if val < 0.3:
            penalty += 5
    final_score = base_score - penalty

    # Additional red herring: complex but irrelevant bitwise mix
    key = 0
    for v in data:
        key ^= int(v) & 7
    key_sum = sum([key >> i for i in range(3)])  # Unused

    return final_score

# Simulated performance metrics and corresponding weights
metrics = [85, 92, 78, 63, 55, 88, 72]
weights = [0.1, 0.2, 0.15, 0.1, 0.05, 0.25, 0.15]

# Extra variables to increase cognitive load
baseline = [m * 0.9 for m in metrics]
drift = sum([abs(a - b) for a, b in zip(metrics, baseline)])
threshold_check = any(x < 60 for x in metrics)

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")