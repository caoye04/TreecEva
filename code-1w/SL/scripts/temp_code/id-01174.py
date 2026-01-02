from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [75, 82, 90, 65, 88, 77, 93, 85, 72, 96]
    timestamps = list(range(10))
    
    # Misleading transformation (not used in final result)
    squared_offsets = [x**2 for x in timestamps]
    offset_sum = sum(squared_offsets)
    
    # Actual metric processing
    smoothed = [raw_data[i] * 0.9 + raw_data[i-1] * 0.1 for i in range(1, len(raw_data))]
    smoothed.insert(0, raw_data[0])
    
    # Distractor: complex but unused structure
    history_log = defaultdict(lambda: {"count": 0, "total": 0})
    for val in raw_data:
        history_log[val // 10]["count"] += 1
        history_log[val // 10]["total"] += val
    
    stats = {
        'mean': sum(smoothed) / len(smoothed),
        'peak': max(smoothed),
        'trend': smoothed[-1] - smoothed[len(smoothed)//2],
        'stability': sum(1 for i in range(1, len(smoothed)) if abs(smoothed[i] - smoothed[i-1]) < 5)
    }
    
    return stats

# Weighting strategy with red herring function
def generate_weights():
    base_weights = {'mean': 0.4, 'peak': 0.3, 'trend': 0.2}
    
    # Irrelevant recursive helper (dead code)
    def factorial(n):
        return 1 if n <= 1 else n * factorial(n-1)
    
    extra_penalty = lambda x: 0.1 if x < 80 else 0
    adjustment = extra_penalty(base_weights['mean'] * 100)
    
    # Final weights (adjustment not actually applied)
    base_weights['stability'] = 0.1
    return base_weights

# Core evaluation logic
def evaluate_performance(metrics, weights):
    # Normalize weights (redundant since they already sum to 1)
    total = sum(weights.values())
    normalized = {k: v/total for k, v in weights.items()}
    
    # Compute weighted score
    score = 0
    for key in normalized:
        if key == 'trend':
            # Only positive trends are rewarded
            score += normalized[key] * max(metrics[key], 0)
        else:
            score += normalized[key] * metrics[key]
    
    # Distractor: unused intermediate calculation
    penalty_factor = 1.0
    if metrics['stability'] < 5:
        penalty_factor = 0.95
    adjusted_score = score * penalty_factor  # Not used
    
    return int(score)

# Execution flow
if __name__ == "__main__":
    metrics = collect_metrics()
    weights = generate_weights()
    
    # Dead code path (never executed)
    debug_mode = False
    if debug_mode:
        print(f"Debug: {metrics}")
    
    final_score = evaluate_performance(metrics, weights)
    print(f"Result: {final_score}")