def calculate_performance(data):
    base = len(data)
    adjustments = 0
    
    for key, value in data.items():
        if value.isdigit():
            adjustments += int(value) % 3
        elif value.isalpha():
            adjustments += len(value) // 2
    
    normalized = base * 1.5
    final_score = int(normalized + adjustments - (base > 5))
    return final_score

benchmark_data = {
    'task_a': '12',
    'task_b': 'X',
    'task_c': '99',
    'task_d': 'pass',
    'task_e': '5',
    'task_f': 'OK'
}

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")