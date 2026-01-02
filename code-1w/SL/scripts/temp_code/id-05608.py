def analyze_trends(data, threshold=0.5):
    trend_scores = []
    for entry in data:
        magnitude = abs(entry['change'])
        direction = 1 if entry['change'] > 0 else -1
        normalized_score = magnitude * direction * 0.8
        trend_scores.append(normalized_score)
    
    # Distractor: irrelevant aggregation
    avg_trend = sum(trend_scores) / len(trend_scores) if trend_scores else 0
    high_magnitude_count = len([s for s in trend_scores if abs(s) > threshold])
    return trend_scores


def calculate_weights(n):
    weights = [0.1] * n
    for i in range(1, n):
        weights[i] = weights[i-1] * 1.5
    total = sum(weights)
    return [w / total for w in weights]

# Simulate feedback analysis in a training loop
data_stream = [
    {'change': 0.3, 'epoch': 1},
    {'change': -0.15, 'epoch': 2},
    {'change': 0.05, 'epoch': 3},
    {'change': -0.2, 'epoch': 4}
]

# Extract epochs and changes separately (semi-relevant)
epochs = [item['epoch'] for item in data_stream]
changes = [item['change'] for item in data_stream]

# Compute trend scores using helper function
trend_analysis = analyze_trends(data_stream)

# Distractor: unused weight calculation
weight_scheme = calculate_weights(len(data_stream))

# Feedback calibration based on magnitude bands
feedback_levels = []
for val in changes:
    if abs(val) >= 0.25:
        feedback_levels.append('high')
    elif abs(val) >= 0.1:
        feedback_levels.append('medium')
    else:
        feedback_levels.append('low')

# State tracker for adjustment history (partially used)
adjustment_log = {'applied': [], 'skipped': []}
scaling_factor = 1.0
for level in feedback_levels:
    if level == 'high':
        scaling_factor *= 1.1
        adjustment_log['applied'].append(scaling_factor)
    elif level == 'medium':
        scaling_factor *= 0.95
        adjustment_log['applied'].append(scaling_factor)
    # 'low' triggers no action, not logged

# Core evaluation logic
baseline_score = 75.0
penalty_map = {'high': -2, 'medium': -1, 'low': 0}
correction_factor = 0
for level in feedback_levels:
    correction_factor += penalty_map[level]

# Secondary adjustment based on trend sign consistency
positive_trends = sum(1 for c in changes if c > 0)
negative_trends = sum(1 for c in changes if c < 0)
consistency_bonus = 5 if positive_trends == 0 or negative_trends == 0 else -3

# Final performance score computation
raw_score = baseline_score + correction_factor + consistency_bonus

# Non-linear saturation effect
if raw_score > 80:
    final_score = 80 + (raw_score - 80) * 0.5
elif raw_score < 60:
    final_score = 60 + (raw_score - 60) * 0.7
else:
    final_score = raw_score

# Ensure output format matches requirement
print(f"Target result: {final_score}")