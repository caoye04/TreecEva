from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    data = [78, 85, 90, 65, 88, 92, 73]
    metrics = defaultdict(float)
    metrics['raw_sum'] = sum(data)
    metrics['count'] = len(data)
    metrics['average'] = metrics['raw_sum'] / metrics['count']
    metrics['peak'] = max(data)
    metrics['truncated_avg'] = sum(x for x in data if x > 70) / len([x for x in data if x > 70])
    return metrics

# Weighting strategy for evaluation
def get_weights():
    base_weights = {'average': 0.4, 'peak': 0.2, 'truncated_avg': 0.4}
    adjustment_factor = 1.1
    adjusted = {k: round(v * adjustment_factor, 3) for k, v in base_weights.items()}
    # Normalize to ensure sum is ~1.0
    total = sum(adjusted.values())
    normalized = {k: round(v / total, 3) for k, v in adjusted.items()}
    return normalized

# Evaluate overall performance using weighted combination
def evaluate_performance(metrics, weights):
    score = 0.0
    score += metrics['average'] * weights['average']
    score += metrics['peak'] * weights['peak']
    score += metrics['truncated_avg'] * weights['truncated_avg']
    
    # Distractor computation: irrelevant transformation
    temp_result = [metrics['average'] ** 0.5, metrics['peak'] / 10]
    lambda_helper = lambda x: x[0] * 0.1 + x[1] * 0.05
    dummy_score = lambda_helper(temp_result)  # Not used in final result
    
    # Additional distraction: string processing with no impact
    status_msg = "Performance evaluation complete"
    padded_msg = status_msg.upper().ljust(50, '.')
    char_count = len(padded_msg.replace('.', ''))  # unused
    
    return round(score, 3)

# Execution flow
def main():
    metrics = collect_metrics()
    weights = get_weights()
    
    # Intermediate calculations with side distractions
    outlier_count = sum(1 for x in [78, 85, 90, 65, 88, 92, 73] if x < 70)
    penalty_factor = 0.98 if outlier_count > 0 else 1.0
    adjusted_average_hint = metrics['average'] * penalty_factor  # hint not used
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()