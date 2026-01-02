def calculate_performance(results):
    base_score = 0
    penalty_factor = 0.9
    bonus_multiplier = 1.2
    temp_offset = 5  # irrelevant offset used in distraction
    adjustment = 0

    for test, data in results.items():
        raw = data['iterations'] * data['efficiency']
        if raw > 100:
            adjustment += 10
        else:
            adjustment -= 5

        # Distractor computation - not used in final score
        hypothetical = (data['latency'] + temp_offset) ** 0.5
        stability_check = hypothetical > 8.5

        base_score += raw

        # Early termination red herring
        if base_score < 0:
            break

    # Another distractor block
    outlier_count = 0
    for val in results.values():
        if val['efficiency'] < 0.3:
            outlier_count += 1
    # outlier_count is never used

    # Conditional expression with dictionary lookup
    scaling_mode = 'high' if base_score > 300 else 'low'
    scaling_factors = {'high': bonus_multiplier, 'low': penalty_factor}
    
    scaled_score = base_score * scaling_factors[scaling_mode]
    
    # Final adjustment using conditional expression
    final_score = int(scaled_score + (adjustment if adjustment > 0 else 0))
    
    return final_score

# Input data
benchmark_results = {
    'test_a': {'iterations': 50, 'efficiency': 1.8, 'latency': 7},
    'test_b': {'iterations': 40, 'efficiency': 2.1, 'latency': 12},
    'test_c': {'iterations': 60, 'efficiency': 1.2, 'latency': 5},
    'test_d': {'iterations': 30, 'efficiency': 2.5, 'latency': 15}
}

final_score = calculate_performance(benchmark_results)
print(f"Target result: {final_score}")