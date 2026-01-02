from itertools import cycle

def calculate_performance(results):
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.25, 0.15]
    weight_cycle = cycle(weights)
    
    for i, (score, valid) in enumerate(results):
        if not valid:
            continue
        current_weight = next(weight_cycle)
        weighted_sum += score * current_weight
    
    return round(weighted_sum, 3)

# Benchmark test results: (score, valid_flag)
benchmark_results = [
    (95, True),
    (87, False),  # Invalid run, excluded
    (90, True),
    (88, True),
    (92, True),
    (85, True)
]

initial_avg = sum(r[0] for r in benchmark_results) / len(benchmark_results)  # Irrelevant computation

final_score = calculate_performance(benchmark_results)
print(f"Target result: {final_score}")