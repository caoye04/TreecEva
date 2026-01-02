def analyze_trends(data, base):
    trend = 0
    adjustments = []
    for val in data:
        if val > base * 1.1:
            trend += 1
            adjustments.append(val * 0.05)
        elif val < base * 0.9:
            trend -= 1
            adjustments.append(-val * 0.03)
    return trend, adjustments

raw_input = "78,85,92,64,77,58,96"
data_points = [int(x) for x in raw_input.split(',')]

baseline = sum(data_points) / len(data_points)

# Simulate auxiliary diagnostics
trend_count, corrections = analyze_trends(data_points, baseline)
diagnostic_flag = 'stable' if abs(trend_count) < 2 else 'volatile'

# Irrelevant aggregation (distractor)
total_magnitude = sum(abs(x - baseline) for x in data_points)
scaling_factor = 1.0 if total_magnitude < 100 else 0.9

# Primary metric computation with conditional expression
metrics = []
for x in data_points:
    deviation = abs(x - baseline)
    category = 'high' if x >= baseline else 'low'
    weight = 1.2 if category == 'high' else 0.8
    # Include string-based logic as per requirement
    status = f'{category}-{"above" if deviation > 10 else "near"}'.upper()
    score = (x * weight) - deviation * 0.5
    metrics.append({'value': x, 'score': score, 'status': status})

# Secondary filtering based on status pattern (uses string method)
filtered_metrics = [m for m in metrics if 'ABOVE' in m['status']]

threshold = 80.0

# Core logic with distraction: some entries are processed but only one matters
processed_values = []
for entry in filtered_metrics:
    temp_val = entry['score']
    if entry['value'] > threshold:
        temp_val += 5
    elif entry['value'] == threshold:
        temp_val += 2
    else:
        temp_val -= 3
    processed_values.append(temp_val)

# Final processing step - key intervention point
final_score = 0
for v in processed_values:
    if v > 75:
        final_score += v * 0.7
    else:
        final_score += v * 0.3

# Normalize using irrelevant constant (dead path)
if diagnostic_flag == 'critical':
    final_score *= 0.95  # Never executed

# Print result as required
print(f"Result: {final_score}")