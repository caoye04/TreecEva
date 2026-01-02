from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 135, 140, 128, 150, 160, 145, 130]
    processed = defaultdict(int)
    temp_buffer = []

    for i, val in enumerate(raw_data):
        if val > 130:
            processed['high_count'] += 1
            if i % 2 == 0:
                temp_buffer.append(val * 0.1)
        else:
            processed['low_count'] += 1

    # Irrelevant smoothing operation (distractor)
    smoothed = [raw_data[i] * 0.9 + raw_data[i-1] * 0.1 for i in range(1, len(raw_data))]
    processed['trend'] = sum(smoothed[:3]) - sum(smoothed[-3:])

    # Key metric: average of high values above threshold
    high_vals = [v for v in raw_data if v > 135]
    processed['avg_high'] = sum(high_vals) / len(high_vals) if high_vals else 0

    return dict(processed)

# Weighting logic with conditional expression
def apply_weights(data, base_weight=0.8):
    w = {}
    w['count_weight'] = base_weight if data['high_count'] > 3 else base_weight * 0.7
    w['trend_weight'] = 1.2 if data['trend'] > 0 else 0.8
    w['bonus'] = data['high_count'] * 2 if data['avg_high'] > 140 else 0  # possible bonus
    w['penalty'] = -5 if data['low_count'] < 2 else 0
    return w

# Evaluate final performance score
def evaluate_performance(metrics, weights):
    score = 0
    score += metrics['high_count'] * 10
    score += metrics['avg_high'] * weights['count_weight']
    score += metrics['trend'] * weights['trend_weight']
    score += weights['bonus']
    score += weights['penalty']
    
    # Dead code path - never executed under current logic (distractor)
    if metrics.get('invalid_flag', False):
        score -= 100
    
    return int(score)

# Main execution flow
metrics = collect_metrics()
weights = apply_weights(metrics)
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")