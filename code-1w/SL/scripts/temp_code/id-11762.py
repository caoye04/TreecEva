def calculate_performance(data):
    base_score = sum(data['metrics']['raw'])
    adjustments = data['metrics']['weights']
    weighted_penalty = 0
    
    for i, weight in enumerate(adjustments):
        if i % 2 == 0:
            weighted_penalty += weight * 0.5
        else:
            weighted_penalty -= weight * 0.3
    
    stability_bonus = len(data['config']['flags']) if data['config']['optimized'] else 0
    temp_data = [base_score, weighted_penalty]
    slice_sum = sum(temp_data[:2])
    
    final_score = slice_sum + stability_bonus
    return final_score

# Simulated benchmark input
dataset_size = 1024
benchmark_data = {
    'metrics': {
        'raw': [12, 15, 22, 8],
        'weights': [4, 6, 5, 7]
    },
    'config': {
        'optimized': True,
        'flags': ['F1', 'F2', 'F3']
    }
}

intermediate_result = benchmark_data['metrics']['raw'][0] * 2  # distractor
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")