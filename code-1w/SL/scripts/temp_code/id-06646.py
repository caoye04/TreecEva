def calculate_performance(data):
    base_multiplier = 1.5
    threshold = 85
    penalty_factor = 0.9
    bonus_increment = 2.5
    temp_offset = 0  # unused distractor
    debug_flag = False  # misleading flag, not used

    # Irrelevant preprocessing (distractor block)
    adjusted_data = [x * 1.01 for x in data if x > 0]
    normalized = list(map(lambda x: x / max(adjusted_data), adjusted_data))

    # Core logic with meaningful steps
    valid_entries = [x for x in data if isinstance(x, (int, float)) and x >= 0]
    above_threshold = list(filter(lambda x: x >= threshold, valid_entries))

    count = len(valid_entries)
    hits = len(above_threshold)

    # Simulated performance ratio with bonus and penalty logic
    if count == 0:
        return 0.0
    
    base_ratio = hits / count
    if base_ratio >= 0.7:
        applied_multiplier = base_multiplier
    else:
        applied_multiplier = penalty_factor
    
    # Accumulate score through staged logic
    raw_score = base_ratio * 100
    adjusted_score = raw_score * applied_multiplier
    
    # Bonus logic based on early termination condition
    for i, val in enumerate(valid_entries):
        if val >= threshold:
            adjusted_score += bonus_increment
            break  # early exit, only adds bonus once

    # Dead code path (never executed due to structure, adds interference)
    if debug_flag:
        print(f'Debug: {adjusted_score=}')

    final_score = int(round(adjusted_score))  # final deterministic integer result

    return final_score

# Main execution
benchmark_data = [78, 92, 88, 65, 96, 89, 77]
intermediate_calc = sum([x**2 for x in benchmark_data]) / 1000  # irrelevant computation
offset_tracker = enumerate(benchmark_data)  # unused but plausible distraction
zipped_view = list(zip(benchmark_data, [x * 0.1 for x in benchmark_data]))  # side analysis, unused

final_score = calculate_performance(benchmark_data)
print(f'Result: {final_score}')