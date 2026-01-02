def evaluate_system_status(metrics):
    weight_function = lambda x: 0.8 * x['cpu'] + 0.15 * x['memory'] + 0.05 * x['disk']
    
    baseline = 75
    adjustment = 10 if metrics['redundancy_ok'] else -15
    
    raw_score = weight_function(metrics)
    adjusted_score = raw_score + adjustment
    
    threshold_score = adjusted_score >= baseline
    final_status = 'STABLE' if threshold_score else 'CRITICAL'
    
    # Irrelevant logging
    log_entry = f'System check: {final_status}'
    extra = [baseline, adjustment]  # Distractor list
    
    return {'status': final_status, 'score': adjusted_score}

# Input data
data = {
    'cpu': 88.0,
    'memory': 65.0,
    'disk': 90.0,
    'redundancy_ok': True
}

# Execution
evaluation_result = evaluate_system_status(data)
print(f'Result: {evaluation_result["score"]}')