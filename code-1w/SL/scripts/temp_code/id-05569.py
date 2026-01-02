def evaluate_performance(output_levels, benchmark_criteria):
    base_efficiency = 0
    peak_count = 0
    transient_buffer = set()
    
    for level in output_levels:
        if level > sum(benchmark_criteria) / len(benchmark_criteria):
            base_efficiency += level * 0.85
            peak_count += 1
        else:
            base_efficiency += level * 0.3
    
    # Simulate auxiliary diagnostic pass (not directly used)
    for criterion in benchmark_criteria:
        temp_diag = criterion ** 2 - criterion
        if temp_diag > 10:
            transient_buffer.add(temp_diag)

    adjustment_factor = 1.0
    if peak_count >= 3:
        adjustment_factor = 1.4
    elif peak_count == 2:
        adjustment_factor = 1.1
    
    # Secondary validation using set intersection
    valid_levels = {x for x in output_levels if x > 15}
    reference_pool = {16, 18, 20, 22, 24}
    confirmed_valid = valid_levels & reference_pool  # Intersection
    
    validation_bonus = 0
    if len(confirmed_valid) >= 2:
        validation_bonus = 8.5
    
    # Irrelevant statistical tracking
    cumulative_drift = 0.0
    for i in range(len(output_levels) - 1):
        cumulative_drift += abs(output_levels[i] - output_levels[i+1])

    # Final computation with red herring variables
    raw_score = base_efficiency * adjustment_factor + validation_bonus
    penalty_deduction = len(transient_buffer) * 0.5  # Minor effect, but not impactful
    final_score = int(raw_score - penalty_deduction + 0.5)  # Rounded integer

    return final_score

# Input data
productivity_set = [12, 19, 22, 14, 25]
threshold_regime = [10, 18, 20]

# Execution point
final_score = evaluate_performance(productivity_set, threshold_regime)
print(f"Result: {final_score}")