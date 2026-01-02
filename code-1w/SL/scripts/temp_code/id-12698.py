def calculate_performance(data):
    base_multiplier = 1.5
    threshold = 85
    penalty_factor = 0.9
    bonus_increment = 2.5

    # Irrelevant tracking variables (distractors)
    total_iterations = 0
    debug_log = []
    temp_accumulator = 0

    # Preprocessing: extract performance metrics above threshold
    filtered_metrics = [x for x in data if x > threshold]

    # Secondary list comprehension with semi-relevant transformation
    normalized = [(val * base_multiplier) for val in data]

    # Simulate stateful processing with lambda filtering
    high_performers = list(filter(lambda x: x > threshold * base_multiplier, normalized))

    # Core logic begins here
    raw_sum = sum(filtered_metrics)
    count_bonus = len(high_performers) * bonus_increment

    # Apply conditional penalty if any metric is below 70 (not in filtered set)
    has_underperformer = any(x < 70 for x in data)
    penalty = penalty_factor if has_underperformer else 1.0

    # Accumulate intermediate values (some used, some not)
    temp_accumulator += raw_sum  # Used only to create illusion of state

    # Final score computation
    base_score = raw_sum * penalty
    final_score = base_score + count_bonus

    # Dead code path - never executed but adds interference
    if False:
        debug_log.append(f'Debug: {final_score}')
        total_iterations += 1

    return final_score

# Main execution
benchmark_data = [92, 88, 76, 95, 83, 90]
interim_result = [x ** 0.5 for x in benchmark_data]  # Unused preprocessing
auxiliary_flag = len(benchmark_data) % 2 == 0  # Unused boolean
final_score = calculate_performance(benchmark_data)
print(f'Target result: {final_score}')