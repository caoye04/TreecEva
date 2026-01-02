from collections import defaultdict

def calculate_performance(results):
    score = 0
    penalties = defaultdict(int)
    
    for idx, (name, data) in enumerate(results.items()):
        base = sum(data) / len(data)
        if base > 80:
            score += 10
        else:
            penalties['low_perf'] += 1
    
    # Additional adjustment based on consistency
    all_averages = [sum(v)/len(v) for v in results.values()]
    if all(avg >= 75 for avg in all_averages):
        score += 5
    
    final_score = score - penalties['low_perf']
    return final_score

# Benchmark test results per module
benchmark_results = {
    'arithmetic': [85, 90, 88],
    'logic': [92, 87, 85],
    'assignment': [78, 80, 82],
    'control_flow': [88, 85, 90]
}

initial_offset = 0  # Irrelevant setup (minimal distraction)
baseline_reference = None

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")