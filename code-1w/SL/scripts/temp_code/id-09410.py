from itertools import compress, cycle

def analyze_metrics(data, weights):
    weighted_sum = sum(x * w for x, w in zip(data, weights))
    norm_factor = sum(weights)
    return weighted_sum / norm_factor if norm_factor != 0 else 0

def validate_entry(record):
    # Irrelevant validation logic (not used in final path)
    if not record.get('active'):
        return False
    if record.get('version', 1) < 2:
        return False
    return True

def calculate_performance(results):
    scores = [r['score'] for r in results]
    categories = [r['category'] for r in results]
    
    # Distractor: unused transformation
    normalized = [(s - min(scores)) / (max(scores) - min(scores) + 1e-8) for s in scores]
    
    # Conditional expression with real impact
    bonuses = [0.5 if c == 'critical' else 0.1 for c in categories]
    
    base_performance = analyze_metrics(scores, [1.0, 1.2, 0.8, 1.5, 0.7])
    
    # Simulate adaptive weighting using cycle (real contribution)
    dynamic_weights = [w for w, _ in zip(cycle([1.1, 0.9]), range(len(scores)))]
    adjusted = sum(s * w for s, w in zip(scores, dynamic_weights))
    
    # Real computation branch
    if len(scores) > 4:
        adjustment = 1.05
    else:
        adjustment = 1.0
    
    # Final calculation
    raw_total = base_performance * adjustment
    
    # Dead code path (distractor)
    outlier_count = 0
    for val in scores:
        if val < 50:
            outlier_count += 1  # never used

    # Key decision using conditional expression
    penalty = 0.95 if any(s < 40 for s in scores) else 1.0
    
    # Final score computed here
    final_score = raw_total * penalty
    
    # Print required output
    print(f"Target result: {final_score}")
    return final_score

# Main execution block
benchmark_results = [
    {'score': 88, 'category': 'core', 'active': True, 'version': 2},
    {'score': 92, 'category': 'critical', 'active': True, 'version': 2},
    {'score': 76, 'category': 'aux', 'active': True, 'version': 3},
    {'score': 94, 'category': 'critical', 'active': True, 'version': 2},
    {'score': 81, 'category': 'core', 'active': True, 'version': 2}
]

# Unused data structures (distractors)
dummy_logs = ['err_retry', 'timeout', 'reconnect']
status_flags = {key: False for key in ['calibration', 'sync', 'validation']}

# Trigger point: calculate performance
final_score = calculate_performance(benchmark_results)