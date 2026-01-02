def calculate_performance(data):
    # Precompute various statistics (some are red herrings)
    total_entries = len(data)
    valid_count = sum(1 for x in data if x['status'] == 'active')
    avg_latency = sum(x['latency'] for x in data) / total_entries
    
    # Distractor: irrelevant aggregation
    error_sum = sum(x.get('errors', 0) for x in data)
    timeout_count = len([x for x in data if x['latency'] > 100])
    
    # Key logic: efficiency ratio based on throughput and latency
    total_throughput = sum(x['throughput'] for x in data)
    efficiency_ratio = total_throughput / (avg_latency + 1)
    
    # Secondary metric with partial relevance
    performance_flags = [1 if x['throughput'] > 50 else 0 for x in data]
    flag_coverage = sum(performance_flags) / total_entries
    
    # Weighted score calculation (core answer path)
    base_score = efficiency_ratio * 0.7
    coverage_bonus = flag_coverage * 15
    stability_penalty = (timeout_count / total_entries) * 10
    
    # Final computation
    final_score = base_score + coverage_bonus - stability_penalty
    
    # More distractions below (dead computations)
    peak_throughput = max(x['throughput'] for x in data)
    hypothetical_gain = peak_throughput * 0.05
    normalized_errors = error_sum / (total_entries + 1e-5)
    
    return final_score

# Simulated benchmark dataset
benchmark_data = [
    {'status': 'active', 'latency': 45, 'throughput': 60, 'errors': 2},
    {'status': 'inactive', 'latency': 80, 'throughput': 30, 'errors': 5},
    {'status': 'active', 'latency': 20, 'throughput': 75, 'errors': 1},
    {'status': 'active', 'latency': 60, 'throughput': 55, 'errors': 3},
    {'status': 'active', 'latency': 90, 'throughput': 40, 'errors': 4},
    {'status': 'active', 'latency': 30, 'throughput': 80, 'errors': 0}
]

# Execute and print result
result = calculate_performance(benchmark_data)
print(f"Result: {result}")