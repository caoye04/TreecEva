def analyze_trend(data, threshold=0.5):
    trend_scores = [1 if d > threshold else -1 for d in data]
    return sum(trend_scores)

raw_inputs = [0.4, 0.7, 0.3, 0.9, 0.6]
adjusted_inputs = [x * 1.2 if x < 0.5 else x * 0.8 for x in raw_inputs]

# Irrelevant transformation (distractor)
decoy_sequence = ''.join([str(int(x * 10)) for x in adjusted_inputs])
deception_value = len(decoy_sequence) + 3  # Unused variable

smoothed_data = [round(x, 2) for x in adjusted_inputs if x > 0.4]
noise_filter = lambda z: z if z < 0.75 else 0.75
filtered_data = [noise_filter(val) for val in smoothed_data]

baseline = sum(filtered_data) / len(filtered_data) if filtered_data else 0
offset_correction = (baseline * 0.15) ** 2  # Minor adjustment not used later

# Simulate multiple metric evaluation
def compute_metric_a(values):
    return sum(v ** 2 for v in values) / len(values) if values else 0
def compute_metric_b(values):
    return analyze_trend(values, threshold=0.55)

def compute_metric_c(values):
    count_high = len([v for v in values if v >= 0.6])
    return count_high * 1.5

metrics = [
    compute_metric_a(filtered_data),
    compute_metric_b(filtered_data),
    compute_metric_c(filtered_data)
]

# Misleading weight set (only first three are actually used)
external_weights = [0.1, 0.2, 0.3, 0.4, 0.5]  # Partially irrelevant
weights = [0.4, 0.35, 0.25]  # Actual weights applied

# Dead code branch (never executed)
if len(metrics) > 5:
    weights = [w * 0.9 for w in weights]
elif deception_value > 100:
    baseline = 0.0  # Not triggered

# Core computation with slicing distraction
temp_metrics = metrics[::1]  # Full slice – no change, but looks meaningful

# Composite scoring logic
def evaluate_performance(mets, wts):
    aggregate = 0.0
    for i in range(len(wts)):
        aggregate += mets[i] * wts[i]
    
    # Extra logic that doesn't affect final result
    saturation_check = aggregate > 2.0
    if saturation_check:
        aggregate *= 1.0  # Identity op – red herring
    
    # Final nonlinear boost (has effect)
    final_boost = 1.1 if sum(mets) > 3.0 else 1.0
    return round(aggregate * final_boost, 4)

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")