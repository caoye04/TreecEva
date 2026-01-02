from collections import defaultdict

# Simulate system performance metrics over time
timestamps = [100, 200, 300, 400, 500]
raw_data = [85, 90, 78, 92, 88]

# Irrelevant auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E']
placeholder_map = {k: v for k, v in zip(dummy_labels, timestamps)}

# Initialize metric tracker
metric_history = defaultdict(list)
for t, val in zip(timestamps, raw_data):
    metric_history['values'].append(val)
    metric_history['smoothed'].append(val * 0.95)  # Some transformation

# Weight configuration for scoring (critical)
weights = {'base': 0.6, 'trend': 0.3, 'stability': 0.1}

# Misleading secondary weights (distractor)
alt_weights = {'legacy': 0.4, 'experimental': 0.6}

# Trend analysis (semi-relevant)
def compute_trend(values):
    if len(values) < 2:
        return 0
    return sum(values[-2:]) / 2 - sum(values[:2]) / 2

# Stability metric based on variance (relevant)
def compute_stability(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return 100 / (1 + variance / 10)  # Inverse relationship

# Core evaluation function
def evaluate_performance(metrics, w):
    base_score = sum(metrics['values']) / len(metrics['values'])
    trend_bonus = compute_trend(metrics['values']) * w['trend']
    stability_factor = compute_stability(metrics['values']) * w['stability']
    
    # Dummy computation with no effect (dead code path - distractor)
    if len(metrics['smoothed']) > 100:
        dummy = max(metrics['smoothed']) - min(metrics['smoothed'])
    else:
        pass  # Misleading control flow
    
    # Actual score calculation
    raw_final = base_score * w['base'] + trend_bonus + stability_factor
    
    # Additional irrelevant lambda (distractor)
    transform = lambda x: x * 1.05 if x > 90 else x * 0.98
    adjusted_vals = [transform(v) for v in metrics['values']]  # Computed but unused
    
    return round(raw_final, 2)

# Execute main logic
metrics = {
    'values': [85, 90, 78, 92, 88],
    'labels': ['m1', 'm2', 'm3', 'm4', 'm5']  # Unused field
}

# Secondary unused metric group (distractor)
analysis_set = [
    {'type': 'latency', 'data': [40, 55, 50]},
    {'type': 'throughput', 'data': [200, 180, 195]}
]

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")