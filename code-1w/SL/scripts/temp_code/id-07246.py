def calculate_performance(results):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    scaling_factor = 0.01
    
    # Irrelevant tracking variables (distractors)
    total_entries = len(results)
    temp_sum = sum(results.values())
    avg_temp = temp_sum / total_entries if total_entries else 0
    
    # Intermediate computations with partial relevance
    raw_scores = [v for v in results.values() if v >= 60]  # Filter passing scores
    adjustment = len(raw_scores) * scaling_factor
    
    # Simulate historical drift (unused)
    historical_bias = 0.05 * sum(1 for v in results.values() if v < 70)
    
    # Core logic masked by noise
    high_performers = 0
    for k, v in results.items():
        if v > bonus_threshold:
            high_performers += 1
    
    # Multiple assignment and distractor unpacking
    (a, b), (c, d) = ((1, 2), (3, 4))
    dummy_calc = a * c + b * d  # Unused but plausible
    
    # Actual performance formula buried in logic
    base_total = sum(v * base_multiplier for v in raw_scores)
    penalty_deduction = sum(10 for v in results.values() if v < 60)
    bonus_award = high_performers * 7
    
    final_value = base_total - penalty_deduction + bonus_award
    
    # Red herring: string manipulation that doesn't affect result
    status_labels = ['pass' if v >= 60 else 'fail' for v in results.values()]
    status_counts = {label: status_labels.count(label) for label in set(status_labels)}
    summary_str = ''.join(status_counts.keys())
    
    # Final scaling unrelated to main path
    noise_offset = len(summary_str) * 0.5
    
    return int(final_value - noise_offset)

# Benchmark data (real input)
benchmark_results = {
    'task_A': 92,
    'task_B': 78,
    'task_C': 55,
    'task_D': 88,
    'task_E': 67,
    'task_F': 96,
    'task_G': 44
}

# Key computation point
final_score = calculate_performance(benchmark_results)

print(f"Result: {final_score}")