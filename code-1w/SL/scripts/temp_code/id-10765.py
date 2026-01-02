def calculate_performance(results):
    base_score = results['latency'] * 0.5
    if results['errors'] == 0:
        base_score += 10
    else:
        base_score -= results['errors'] * 2
    
    # Additional adjustment based on throughput
    throughput_factor = results['throughput'] / 100
    base_score += throughput_factor
    
    # Irrelevant metric (distractor)
    peak_memory = results['memory_usage']['peak']
    avg_temp = 45.2  # Sensor reading, not used in calculation
    
    return round(base_score, 2)

# Simulated benchmark data
dataset_metrics = {
    'samples_processed': 1500,
    'average_batch_size': 32
}

benchmark_results = {
    'latency': 85,
    'throughput': 120,
    'errors': 3,
    'memory_usage': {
        'peak': 2048,
        'allocated': 1536
    }
}

initial_estimate = 70.0
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")