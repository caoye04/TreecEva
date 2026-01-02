def calculate_performance(data):
    base_scores = [len(task['name']) * task['complexity'] for task in data]
    adjustments = []
    
    for entry in data:
        threshold = 3
        if entry['type'] == 'compute':
            penalty = entry['errors'] * 2
        else:
            penalty = entry['errors']
        adjustments.append(penalty)
    
    total_base = sum(base_scores)
    total_adjustment = sum(adjustments)
    final_score = total_base - total_adjustment
    
    temp_debug_value = 999  # Irrelevant debug variable (minimal distraction)
    return final_score

benchmark_data = [
    {'name': 'parser', 'complexity': 4, 'type': 'compute', 'errors': 1},
    {'name': 'encoder', 'complexity': 7, 'type': 'memory', 'errors': 0},
    {'name': 'validator', 'complexity': 8, 'type': 'compute', 'errors': 2},
    {'name': 'loader', 'complexity': 6, 'type': 'io', 'errors': 1}
]

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")