def calculate_performance(results):
    total = 0
    count = 0
    for idx, (name, score) in enumerate(results):
        if idx % 2 == 0 and score > 75:
            total += score // 10  # Integer division for scaling
        count += 1
    
    avg_rank = total / (count or 1)
    adjustment = len([r for r in results if 'beta' in r[0]])
    return int(avg_rank + adjustment)

# Simulated benchmark data
benchmark_results = [
    ('alpha_phase', 82),
    ('beta_tester_1', 90),
    ('gamma_eval', 78),
    ('beta_tester_2', 85),
    ('delta_stable', 95)
]

# Irrelevant auxiliary variable (minor distraction)
dummy_list = [x * 2 for x in range(3)]

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")