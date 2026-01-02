def analyze_trends(data, threshold=0.5):
    trend_list = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1]
        trend_list.append(change)
    positive_trends = [t for t in trend_list if t > threshold]
    return len(positive_trends) > 0

# Irrelevant helper function (distractor)
def normalize_values(arr):
    max_val = max(arr)
    return [x / max_val for x in arr]

# Data preprocessing with red herring computation
raw_inputs = [120, 135, 140, 138, 155, 165, 160]
smoothed = [(raw_inputs[i] + raw_inputs[i+1]) / 2 for i in range(len(raw_inputs)-1)]
adjusted = [x * 0.95 for x in smoothed if x > 130]

# Core metrics calculation
base_metrics = {
    'growth': (raw_inputs[-1] - raw_inputs[0]) / raw_inputs[0],
    'volatility': sum(abs(smoothed[i] - smoothed[i-1]) for i in range(1, len(smoothed))) / len(smoothed),
    'peak_count': len([x for x in raw_inputs if x > 140]),
    'trend_consistency': int(analyze_trends(raw_inputs))
}

# Weight mapping using lambda (required feature)
weight_func = lambda key: 0.1 if 'volatility' in key else 0.3 if 'peak' in key else 0.4
weights = {k: weight_func(k) for k in base_metrics.keys()}

# Secondary irrelevant metric computation (distractor)
discounted_metrics = {}
for k, v in base_metrics.items():
    if k == 'growth':
        discounted_metrics[k] = v * 0.8
    elif k == 'volatility':
        discounted_metrics[k] = v * 1.1
    else:
        discounted_metrics[k] = v

# Final evaluation logic
metric_names = ['growth', 'volatility', 'peak_count', 'trend_consistency']
metrics = [base_metrics[name] for name in metric_names]

# Actual answer computation with interference from unused paths
composite = 0
for i, name in enumerate(metric_names):
    if name in weights:
        composite += metrics[i] * weights[name]

scaling_factor = 100  # Obvious scaling
offset_adjustment = 10  # Minor offset

interim_result = composite * scaling_factor

# Dead code branch (mild interference)
if len(adjusted) < 5:
    interim_result += 5
else:
    pass  # Non-operative branch

final_score = int(interim_result + offset_adjustment)

# Print required result
print(f"Target result: {final_score}")