def calculate_performance(data):
    base_scores = {k: v * 1.5 for k, v in data.items()}
    bonus = sum(1 for val in base_scores.values() if val > 20)
    adjustment = len(base_scores) - bonus
    
    # Irrelevant auxiliary variable (minimal distraction)
    temp_log = [f'{k}: {v}' for k, v in base_scores.items()]
    
    total = sum(base_scores.values())
    final_score = total + bonus * 2 - adjustment
    return final_score

# Benchmark dataset for system performance
benchmark_data = {'module_a': 12, 'module_b': 18, 'module_c': 22, 'module_d': 14}
final_score = calculate_performance(benchmark_data)
print(f'Result: {final_score}')