def calculate_performance(results):
    base_score = 0
    penalty = 0
    
    for test, data in results.items():
        if data['success']:
            base_score += data['points']
            if data['time_ms'] < 50:
                base_score += 5
        else:
            penalty += data['points'] // 2

    if base_score > 0:
        return (base_score - penalty) // 1  # integer division, neutral operation
    return 0

# Irrelevant auxiliary variable (minor distraction)
threshold = 75

benchmark_results = {
    'render': {'success': True, 'points': 20, 'time_ms': 45},
    'physics': {'success': False, 'points': 30, 'time_ms': 80},
    'ai': {'success': True, 'points': 25, 'time_ms': 60},
    'input': {'success': True, 'points': 15, 'time_ms': 20}
}

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")