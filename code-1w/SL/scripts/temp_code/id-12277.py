def evaluate_performance(records, config):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []

    for i, record in enumerate(records):
        if i % 2 == 0:
            base_score += len(record) * config.get('weight_a', 1)
        else:
            temp_value = sum([ord(c) % 5 for c in record])
            penalty_adjustment += temp_value  # Unused distraction

        if 'x' in record:
            bonus_tracker.append(i * 0.5)

    aggregate_bonus = sum(bonus_tracker) if bonus_tracker else 0
    final_score = base_score + int(aggregate_bonus)
    
    # Distractor variables and operations
    snapshot = records[1:4]
    mirror_copy = snapshot[::-1]
    dummy_sum = sum(len(s) for s in mirror_copy)
    outlier_flag = dummy_sum > 100

    return final_score


# Simulated dataset
raw_data = ['axb', 'byc', 'cxd', 'dye', 'exf']
data_slice = raw_data[::2]  # Slicing every other element

threshold_map = {
    'weight_a': 3,
    'weight_b': -1,
    'debug_mode': False
}

intermediate_result = [len(item) for item in raw_data]  # Dead computation path
scaling_factor = max(intermediate_result) ** 2  # Unused scaling

final_score = evaluate_performance(data_slice, threshold_map)
print(f"Result: {final_score}")