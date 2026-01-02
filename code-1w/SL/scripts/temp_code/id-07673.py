import math

# Simulate a system that evaluates employee performance across multiple dimensions
def calculate_efficiency(index_log, base_rating):
    efficiency = 0
    temp_buffer = []
    for i in index_log:
        if i % 2 == 0:
            efficiency += math.sqrt(i + base_rating) * 0.3
        else:
            efficiency -= math.log(i + 1) * 0.1
        temp_buffer.append(efficiency)
    
    # Irrelevant transformation (dead computation)
    reversed_buffer = [x * 0.95 for x in temp_buffer[::-1]]
    average_buffer = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    
    return efficiency

# Misleading auxiliary function that computes unused metrics
def compute_variance(data):
    mean_val = sum(data) / len(data)
    squared_diffs = [(x - mean_val) ** 2 for x in data]
    var_result = sum(squared_diffs) / len(squared_diffs)
    return var_result

# Another red herring: tracks 'consistency' but not used in final score
def assess_consistency(trace_series):
    trend_deviation = 0
    for j in range(1, len(trace_series)):
        trend_deviation += abs(trace_series[j] - trace_series[j-1])
    consistency_metric = 100 / (1 + trend_deviation) if trend_deviation > 0 else 100
    return consistency_metric

# Core evaluation logic with dictionary and lambda usage
def evaluate_performance(weights_dict, outcomes_list):
    # Normalize weights using lambda
    total_weight = sum(weights_dict.values())
    normalized_weights = {k: v / total_weight for k, v in weights_dict.items()}
    
    # Apply transformations
    adjusted_scores = {}
    for key, weight in normalized_weights.items():
        raw_index = ord(key.lower()) % 5  # maps 'a'->0, 'b'->1, etc.
        base_score = outcomes_list[raw_index]
        
        # Complex scoring rule involving arithmetic and conditional boosts
        if base_score > 75:
            boosted = base_score * (1 + weight * 0.5)
        elif base_score > 50:
            boosted = base_score * (1 + weight * 0.2)
        else:
            boosted = base_score * (1 - weight * 0.1)
        
        adjusted_scores[key] = max(boosted, 0)
    
    # Compute composite using weighted average via lambda
    aggregator = lambda scores, w: sum(scores[k] * w[k] for k in w)
    composite = aggregator(adjusted_scores, normalized_weights)
    
    # Final nonlinear scaling
    if composite > 80:
        final_value = 90 + (composite - 80) * 0.5
    elif composite > 60:
        final_value = 70 + (composite - 60) * 0.8
    else:
        final_value = 50 + (composite - 40) * 0.6
    
    return int(final_value)

# Main execution block
if __name__ == '__main__':
    # Input data
    metric_weights = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}  # Weight distribution
    raw_outcomes = [85, 60, 70, 90, 45]  # Performance on 5 metrics
    
    # Dead variables and irrelevant processing (distraction)
    audit_trace = [2, 4, 6, 8, 10]
    buffer_efficiency = calculate_efficiency(audit_trace, 5)
    variance_metrics = compute_variance(raw_outcomes)
    reliability_score = assess_consistency(audit_trace)
    
    # Key statement
    final_score = evaluate_performance(metric_weights, raw_outcomes)
    
    # Print result as required
    print(f"Result: {final_score}")