def analyze_trend(data):
    if not data:
        return 0
    trend = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    volatility = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    avg_change = sum(data[i] - data[i-1] for i in range(1, len(data))) / (len(data) - 1) if len(data) > 1 else 0
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * 0.7 + data[i] * 0.3)
    return len([x for x in smoothed if x > sum(data) / len(data)])


def compute_risk_adjustment(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    stdev = variance ** 0.5
    outliers = [x for x in values if abs(x - mean_val) > 2 * stdev]
    adjustment_factor = 0.95 if len(outliers) > 0 else 1.05
    penalty = len(outliers) * 0.01
    return adjustment_factor - penalty

metrics = [88, 92, 76, 85, 90]
weights = [0.2, 0.3, 0.15, 0.1, 0.25]

historical_data = [85, 87, 88, 86, 90, 91, 89]
dummy_flags = [True if x % 2 == 0 else False for x in range(len(historical_data))]

baseline_shift = 2.5
temp_buffer = [x + baseline_shift for x in metrics]

risk_profile = compute_risk_adjustment(metrics)
adjusted_metrics = [m * risk_profile for m in metrics]

if len(metrics) != len(weights):
    raise ValueError("Mismatched dimensions")

# Simulate auxiliary analysis with side computation
trend_strength = analyze_trend(historical_data)
scaling_factor = 1.0 + (trend_strength / len(historical_data)) * 0.1

useless_sum = sum(dummy_flags)
dummy_calc = useless_sum * 0.01  # Irrelevant to final result

intermediate_results = []
for i in range(len(adjusted_metrics)):
    weighted_val = adjusted_metrics[i] * weights[i] * scaling_factor
    intermediate_results.append(weighted_val)

consistency_bonus = 0.0
if all(m > 75 for m in metrics):
    consistency_bonus = 3.5

final_score = sum(intermediate_results) + consistency_bonus

print(f"Result: {final_score}")