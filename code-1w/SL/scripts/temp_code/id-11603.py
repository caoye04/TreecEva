def evaluate_performance(metrics, weights):
    temp_result = 0
    base_adjustment = 0.1
    scaling_factor = 1.5
    
    # Irrelevant computation (distractor)
    unused_product = 1
    for val in metrics.values():
        unused_product *= val % 7
    
    # Semi-relevant preprocessing (distraction with partial use)
    normalized = {}
    total_metric = sum(metrics.values())
    for k, v in metrics.items():
        normalized[k] = v / total_metric if total_metric != 0 else 0
    
    # Core logic begins
    weighted_sum = 0
    weight_total = sum(weights[k] for k in metrics.keys())
    
    for key in metrics:
        if key in weights and metrics[key] > 0.5 * max(metrics.values()):
            contribution = metrics[key] * weights[key]
            weighted_sum += contribution

    # Conditional expression used
    adjustment = (0.2 if weighted_sum > 10 else 0.05) * base_adjustment
    
    # State tracking with dictionary
    history = {'step1': weighted_sum, 'step2': adjustment}
    temp_result = history['step1'] + history['step2'] * 100
    
    # Final score calculation
    final_score = int(temp_result // scaling_factor)
    
    return final_score

# Main execution
metrics = {'accuracy': 8.2, 'latency': 4.1, 'throughput': 12.3, 'stability': 6.7}
weights = {'accuracy': 0.3, 'throughput': 0.5, 'stability': 0.2}  # latency missing intentionally

# Extra irrelevant variables (dead code path)
counterfeit_data = [x ** 2 for x in range(5)]
placeholder = {k: 0 for k in metrics}

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")