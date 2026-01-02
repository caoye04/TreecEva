def calculate_performance(results):
    base_score = results['latency'] * 0.3
    if results['success_rate'] > 0.9:
        base_score += 15
    elif results['success_rate'] > 0.75:
        base_score += 8
    else:
        base_score += 2
    
    # Conditional expression for optimization bonus
    optimization_bonus = 10 if results['optimized'] else 5
    
    # Dictionary operation: dynamic adjustment based on environment
    adjustments = {'dev': -3, 'staging': 0, 'prod': 5}
    environment_factor = adjustments.get(results['environment'], 0)
    
    total = base_score + optimization_bonus + environment_factor
    
    # Irrelevant tracking variable (minor distraction)
    execution_log = f'Processed {results["run_id"]}'
    
    return int(total)

# Input data
benchmark_results = {
    'run_id': 'R-2024-X7',
    'latency': 45.0,
    'success_rate': 0.82,
    'optimized': True,
    'environment': 'staging'
}

# Key computation step
final_score = calculate_performance(benchmark_results)

print(f"Result: {final_score}")