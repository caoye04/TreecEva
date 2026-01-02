def calculate_final_score(raw_data, limits):
    # Preprocess: filter and transform data
    processed = [x * 1.5 for x in raw_data if x > 0]
    temp_sum = sum(processed)
    adjustment_factor = 0.9 if temp_sum > 100 else 1.1

    # Irrelevant statistical distraction
    mean_val = temp_sum / len(processed) if processed else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in processed) / len(processed) if processed else 0
    outlier_count = sum(1 for x in processed if abs(x - mean_val) > 2 * (variance_proxy ** 0.5))

    # Real computation path
    clipped = [min(x, limits['max_cap']) for x in processed]
    boosted = [x + (x * 0.2) for x in clipped if x < limits['boost_threshold']]
    bonus = len(boosted) * 2.5

    # Another red herring: unused transformation
    inverted_map = {i: 1/(x+1) for i, x in enumerate(processed)}
    log_transform = [round(x, 3) for x in [1 + (y/10) for y in range(5)] if y in raw_data]  # semi-relevant but unused

    # Core logic with slicing and conditional expression
    segment = clipped[1:-1]  # Exclude first and last
    base_score = sum(segment) * adjustment_factor
    penalty = sum(x for x in clipped if x > limits['penalty_floor']) * 0.1 if segment else 0

    # Final assembly
    final = base_score - penalty + bonus
    return int(final)

# Main execution
config = {
    'max_cap': 80,
    'boost_threshold': 40,
    'penalty_floor': 60
}

raw_input_data = [10, -5, 20, 30, 50, 70, 0, 45]
scratch_buffer = [x for x in raw_input_data if x % 2 == 0]  # irrelevant filtering
intermediate_stats = {'count_pos': sum(1 for x in raw_input_data if x > 0)}

final_score = calculate_final_score(raw_input_data, config)
print(f"Result: {final_score}")