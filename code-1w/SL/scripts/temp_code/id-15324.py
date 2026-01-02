from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 92, 85, 76, 94, 88, 91, 87]
    timestamps = list(range(len(raw_data)))
    
    # Misleading transformation (not used in final calculation)
    squared_offsets = [x**2 - 5 for x in raw_data]
    filtered_data = [x for x in raw_data if x > 80]
    
    metrics = defaultdict(float)
    metrics['avg_raw'] = sum(raw_data) / len(raw_data)
    metrics['peak'] = max(raw_data)
    metrics['consistency'] = len([x for x in raw_data if x >= 85])
    metrics['trend'] = raw_data[-1] - raw_data[0]  # Last vs first
    
    # Dummy entries to distract
    metrics['dummy_offset'] = sum(squared_offsets) / len(squared_offsets)
    metrics['placeholder'] = -999
    
    return dict(metrics)

# Weighting strategy for evaluation
def get_weights():
    base_weights = {'avg_raw': 0.3, 'peak': 0.25, 'consistency': 0.35, 'trend': 0.1}
    
    # Irrelevant transformations
    temp = [w * 1.1 for w in base_weights.values()]
    normalized = [t / sum(temp) for t in temp]  # Never used
    
    # Add red herring weight
    base_weights['dummy_offset'] = 0.0  # Zero weight but looks relevant
    
    return base_weights

# Main evaluation logic
def evaluate_performance(metrics, weights):
    score = 0.0
    debug_values = []
    
    # Core calculation with meaningful and misleading components
    for key, weight in weights.items():
        if key in metrics:
            contribution = metrics[key] * weight
            debug_values.append((key, contribution))
            
            # Only add to score if weight > 0 (excludes dummy)
            if weight > 0:
                score += contribution
    
    # Post-processing with distractor
    adjustment_factor = metrics.get('trend', 0) * 0.05
    adjusted_score = score + adjustment_factor  # Looks important, not used
    
    # Final scaling based on consistency threshold
    if metrics['consistency'] >= 3:
        score *= 1.1  # Performance bonus
    
    # Dead code path (never reached due to condition above)
    if metrics['consistency'] < 0:
        score *= 0.9
    
    return int(round(score))

# Execution flow
if __name__ == "__main__":
    # Collect observed metrics
    metrics = collect_metrics()
    
    # Retrieve weighting scheme
    weights = get_weights()
    
    # Compute final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")