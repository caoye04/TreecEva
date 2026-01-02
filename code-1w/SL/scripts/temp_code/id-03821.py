def calculate_performance(results):
    base_score = 0
    bonus_multiplier = 1.0
    
    for idx, (name, data) in enumerate(zip(['system_a', 'system_b'], results)):
        raw_value = data['metric'] * (idx + 1)
        if raw_value > 50:
            base_score += raw_value // 10
            bonus_multiplier *= 1.1
        else:
            base_score -= 5

    temp_offset = 3  # irrelevant variable (minimal distraction)
    final_rating = base_score * bonus_multiplier
    return int(final_rating)

# Benchmark test results
dataset_1 = {'metric': 45}
dataset_2 = {'metric': 58}
benchmark_results = [dataset_1, dataset_2]

# Critical execution point
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")