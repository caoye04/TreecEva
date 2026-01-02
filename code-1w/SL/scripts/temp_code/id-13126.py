from collections import defaultdict

def calculate_performance(results):
    scores = defaultdict(int)
    for category, values in results.items():
        base = sum(values) / len(values)
        bonus = 1.5 if base > 80 else 0.5
        scores[category] = base + bonus
    
    # Irrelevant auxiliary computation (minor distraction)
    temp_debug = [x * 0.1 for x in range(len(scores))]
    
    total = sum(scores.values())
    scaling_factor = 0.95
    return int(total * scaling_factor)

# Simulated benchmark data across test categories
benchmark_results = {
    'arithmetic': [88, 92, 85],
    'logic': [76, 81, 83],
    'assignment': [90, 88, 95],
    'control_flow': [78, 80]
}

initial_total = sum(sum(v) for v in benchmark_results.values())  # Distractor variable

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")