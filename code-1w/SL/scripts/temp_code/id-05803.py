def calculate_performance(results):
    base_score = 0
    penalty = 0
    
    # Extract relevant metrics
    latency = results['latency_ms']
    throughput = results['throughput_ops']
    errors = results['error_count']
    
    # Irrelevant variable (minor distraction)
    debug_mode = True
    
    base_score += throughput * 2
    base_score -= errors * 5
    
    if latency < 100:
        base_score += 10
    elif latency < 200:
        base_score += 5
    else:
        penalty += 3
    
    consistency = results['consistency_factor']
    if consistency > 0.9:
        base_score += 7
    
    final_score = base_score - penalty
    return final_score

# Input data
benchmark_results = {
    'latency_ms': 150,
    'throughput_ops': 42,
    'error_count': 3,
    'consistency_factor': 0.93
}

# Execution point
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")