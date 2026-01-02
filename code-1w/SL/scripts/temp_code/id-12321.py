def calculate_performance(results):
    base_score = 0
    modifiers = {'latency': 0.85, 'throughput': 1.15, 'accuracy': 1.0}
    weights = dict([('latency', 0.4), ('throughput', 0.35), ('accuracy', 0.25)])
    
    raw_scores = []
    for key in results:
        if key in modifiers:
            adjusted = results[key] * modifiers[key]
            raw_scores.append(adjusted)
    
    temp_sum = sum(raw_scores)
    final_score = temp_sum * weights['latency'] + (raw_scores[1] * weights['throughput'])
    
    metadata = {'generated_on': '2023-11-05', 'version': '2.1'}
    metadata['processed'] = True
    
    return int(final_score)

# Experimental benchmark data
dataset_size = 1000
benchmark_results = {
    'latency': 72,
    'throughput': 68,
    'accuracy': 94
}

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")