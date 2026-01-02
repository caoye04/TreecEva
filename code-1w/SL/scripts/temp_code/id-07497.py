def evaluate_performance(metrics):
    base = metrics['accuracy'] * 100
    penalty = 0
    
    if metrics['latency'] > 50:
        penalty += (metrics['latency'] - 50) * 0.5
    if metrics['error_rate'] > 0.05:
        penalty += 10
    
    bonus = 5 if metrics['concurrency'] >= 100 and metrics['uptime'] > 99.9 else 0
    
    intermediate = base - penalty + bonus
    
    # Irrelevant metric - minimal distraction
    debug_info = {'processed': metrics['requests'], 'batch': 4}
    
    final = int(intermediate)
    return final

# Input data
evaluation_metrics = {
    'accuracy': 0.93,
    'latency': 60,
    'error_rate': 0.07,
    'concurrency': 150,
    'uptime': 99.95,
    'requests': 10000
}

final_score = evaluate_performance(evaluation_metrics)
print(f"Result: {final_score}")