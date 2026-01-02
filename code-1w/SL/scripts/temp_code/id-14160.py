def calculate_performance(metrics):
    base_score = sum(metrics['accuracy']) * 0.4
    penalty = len([x for x in metrics['errors'] if x > 1]) * 0.5
    bonus = 2.0 if metrics['convergence'][0] else 0.0
    
    # Conditional expression based on efficiency
    efficiency_factor = 1.2 if metrics['efficiency'] > 85 else 0.9
    
    adjusted = base_score - penalty + bonus
    final_score = adjusted * efficiency_factor
    
    # Irrelevant auxiliary calculation (minor distraction)
    _temp_debug = [x * 0.1 for x in metrics['accuracy']]
    _unused_metric = max(metrics['convergence'])
    
    return final_score

# Input data
performance_metrics = {
    'accuracy': [88, 92, 85],
    'errors': [0, 3, 1, 4],
    'convergence': [True, False],
    'efficiency': 88
}

# Compute result
final_score = calculate_performance(performance_metrics)
print(f"Result: {final_score}")