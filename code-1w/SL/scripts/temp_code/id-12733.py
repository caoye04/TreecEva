def calculate_performance(results):
    total = 0
    bonus = 0
    base_multiplier = 3

    # Track index and values for performance metrics
    for i, (name, score, penalty) in enumerate(zip(['module_a', 'module_b', 'module_c'], results, [2, 1, 3])):
        adjusted = (score - penalty) % 7
        if i % 2 == 0:
            adjusted *= base_multiplier
        else:
            adjusted += base_multiplier
        total += adjusted

    # Irrelevant tracking variable (minimal distraction)
    max_possible = 10 * len(results)
    efficiency_ratio = total / max_possible

    if efficiency_ratio > 0.5:
        bonus = 5

    return total + bonus

# Simulated benchmark scores
benchmark_results = [8, 6, 9]
initial_total = sum(benchmark_results)
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")