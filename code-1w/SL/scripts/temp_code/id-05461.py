def calculate_performance(results):
    weighted_scores = []
    
    for category, data in results.items():
        raw_score = sum(data['values'])
        penalty_factor = len([x for x in data['errors'] if x > 0])
        adjusted_score = raw_score - (penalty_factor * 1.5)
        
        if adjusted_score <= 0:
            continue
            unused_var = 999  # dead code, minor distraction
        
        weighted_scores.append(adjusted_score * data['weight'])
    
    total_weight = sum(results[cat]['weight'] for cat in results)
    final_performance = sum(weighted_scores) / total_weight
    return round(final_performance, 2)

# Simulated benchmark data from system test
benchmark_results = {
    'arithmetic': {
        'values': [85, 90, 87, 92],
        'errors': [0, 1, 0, 0],
        'weight': 0.3
    },
    'logic': {
        'values': [78, 81, 85],
        'errors': [2, 0],
        'weight': 0.25
    },
    'assignment': {
        'values': [93, 88, 85, 90],
        'errors': [0, 0, 1],
        'weight': 0.2
    },
    'control_flow': {
        'values': [76, 80],
        'errors': [1, 1, 0],
        'weight': 0.15
    },
    'data_structures': {
        'values': [88, 85],
        'errors': [0],
        'weight': 0.1
    }
}

intermediate_total = sum(len(v['values']) for v in benchmark_results.values())  # distractor calc
error_count = sum(len(v['errors']) for v in benchmark_results.values())          # distractor calc

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")