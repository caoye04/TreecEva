def evaluate_performance(metrics):
    base_score = metrics['accuracy'] * 100
    penalty = 0.1 * metrics['latency']
    adjusted_accuracy = base_score - penalty
    
    scaling_factors = {'low': 0.8, 'medium': 1.0, 'high': 1.2}
    load_profile = 'medium' if metrics['concurrent_users'] < 50 else 'high'
    
    scaled_scores = {
        'response_time': adjusted_accuracy * scaling_factors[load_profile],
        'throughput': metrics['throughput'] * 1.5
    }
    
    # Irrelevant metric (minor distraction)
    debug_mode = False
    temp_log = [f"User count: {metrics['concurrent_users']}"]
    
    adjustment_factor = 1.1 if metrics['errors'] == 0 else 0.9
    final_score = min(scaled_scores.values()) * adjustment_factor
    return final_score

# Input data
evaluation_data = {
    'accuracy': 0.92,
    'latency': 20,
    'concurrent_users': 65,
    'throughput': 40,
    'errors': 0
}

result = evaluate_performance(evaluation_data)
print(f"Result: {result}")