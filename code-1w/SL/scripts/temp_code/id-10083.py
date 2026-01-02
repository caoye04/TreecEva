from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    data = [120, 85, 90, 110, 95]
    timestamps = [1, 2, 3, 4, 5]
    
    # Misleading intermediate processing
    avg_latency = sum(data) / len(data)
    peak_value = max(data)
    normalized = [x / 100 for x in data]  # Not actually used later
    
    metrics = defaultdict(float)
    metrics['base'] = sum(data)
    metrics['fluctuation'] = max(data) - min(data)
    metrics['consistency'] = len([x for x in data if x >= 90])
    metrics['outliers'] = len([x for x in data if x < 80 or x > 115])
    
    # Dummy transformation (distraction)
    transformed = [x ** 0.5 for x in data if x > 100]
    adjustment_factor = len(transformed) * 0.5
    
    return metrics

# Weighting schema for evaluation
def define_weights():
    weights = {}
    weights['base'] = 0.4
    weights['fluctuation'] = -0.1  # Penalty for high fluctuation
    weights['consistency'] = 0.3
    weights['outliers'] = -0.2
    weights['phantom'] = 0.5  # Unused weight (red herring)
    return weights

# Core evaluation logic
def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Relevant weighted components
    for key in ['base', 'fluctuation', 'consistency', 'outliers']:
        if key in metrics and key in weights:
            score += metrics[key] * weights[key]
    
    # Irrelevant adjustment (dead code path - never executed due to condition)
    temp_buffer = [score * 1.1]
    if len(temp_buffer) > 10:  # Impossible condition
        score = sum(temp_buffer) / len(temp_buffer)
    
    # Extra computation that looks important but doesn't alter result
    shadow_score = score * 0.95
    verification_check = abs(score - shadow_score) < 1e-5
    
    return int(score)  # Final conversion

# Main execution flow
if __name__ == "__main__":
    # Collect observed system behavior
    raw_metrics = collect_metrics()
    
    # Apply weighting model
    importance_weights = define_weights()
    
    # Compute final evaluation score
    final_score = evaluate_performance(raw_metrics, importance_weights)
    
    # Print result as required
    print(f"Result: {final_score}")