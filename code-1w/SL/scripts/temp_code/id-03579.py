def analyze_trends(data, baseline):
    trend_scores = []
    deviation_total = 0
    for i, point in enumerate(data):
        deviation = abs(point - baseline)
        if deviation > 5:
            adjustment = deviation * 0.1
        else:
            adjustment = 0
        score = point - adjustment
        trend_scores.append(score)
        deviation_total += deviation
    return trend_scores, deviation_total

values = [12, 15, 10, 8, 14]
baseline_ref = 10
trends, total_dev = analyze_trends(values, baseline_ref)

# Simulate secondary metric: volatility index
volatility = sum(abs(trends[i] - trends[i-1]) for i in range(1, len(trends)))
volatility_index = round(volatility / len(trends), 3)

# Irrelevant transformation (dead-end calculation)
transformed = [x ** 0.5 for x in values if x > 9]
scaling_factor = len(transformed) * 0.75 if transformed else 0

# Core evaluation logic
metrics = [sum(trends), volatility_index, total_dev, scaling_factor]
weights = [0.4, 0.2, -0.1, 0.05]

# Secondary helper to mask actual computation path
def normalize(lst):
    max_val = max(lst)
    return [round(x / max_val, 4) for x in lst] if max_val != 0 else lst

normalized_metrics = normalize([abs(m) for m in metrics])
dummy_shift = sum(normalized_metrics[::2]) - sum(normalized_metrics[1::2])

# Actual scoring logic buried among distractions
def evaluate_performance(mets, wts):
    raw = sum(mets[i] * wts[i] for i in range(len(mets)))
    penalty = 0
    if mets[1] > 3.0:
        penalty += 2
    if len([x for x in mets if x < 0]) > 1:
        penalty += 3
    return round(raw - penalty, 4)

final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")