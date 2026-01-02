def analyze_efficiency(data, threshold=0.75):
    """Irrelevant analysis function (red herring)"""
    count = 0
    for val in data:
        if val > threshold:
            count += 1
    return count

# Distractor variables
dummy_data = [0.1, 0.4, 0.8, 0.9, 0.6]
useless_sum = sum(x ** 2 for x in dummy_data if x < 0.7)
flag = False

# Real computation begins: system performance metrics
metrics = [88, 92, 76, 85, 95]  # [cpu, memory, disk, network, gpu]
weights = [0.3, 0.2, 0.15, 0.25, 0.1]  # Weight distribution across components

# Irrelevant conditional block (dead path due to flag)
if flag and len(dummy_data) > 10:
    adjusted = [x * 1.1 for x in metrics]
else:
    baseline_offset = 5
    # Misleading intermediate transformation
    temp_adjusted = [(x + baseline_offset) * 0.95 for x in metrics]

# Actual relevant logic hidden among distractions
scaling_factor = 1.0
for i, (val, w) in enumerate(zip(metrics, weights)):
    if val >= 85:
        scaling_factor *= 1.05
    elif val < 75:
        scaling_factor *= 0.9

# Decoy dictionary with plausible but unused data
performance_labels = {
    'critical': [metrics[2]],
    'optimal': [m for m in metrics if m > 90],
    'standard': [m for m in metrics if 75 <= m <= 90]
}

# Another red herring: complex slicing with no impact
subset = temp_adjusted[1:4][::-1]
shadow_calc = sum(subset[i] * (i+1) for i in range(len(subset)))

# Core accumulation logic buried in noise
weighted_total = 0
for idx, (metric, weight) in enumerate(zip(metrics, weights)):
    contribution = metric * weight
    weighted_total += contribution

# Secondary adjustment using conditional expression
bonus_applied = True if sum(weights) == 1.0 else False
bonus = 7 if bonus_applied and weighted_total > 85 else 0

# Final evaluation obscured by surrounding noise
final_score = 0

# Key statement
final_score = evaluate_performance(metrics, weights)

# Supporting function defined after use (another distraction)
def evaluate_performance(mets, wts):
    base = sum(m * w for m, w in zip(mets, wts))
    extra = 5 if all(m >= 70 for m in mets) else 0
    adj = base * (1.1 if base > 80 else 1.0)
    return int(adj + extra)

print(f"Result: {final_score}")