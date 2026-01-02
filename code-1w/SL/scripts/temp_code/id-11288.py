def calculate_final_score(items, importance_weights):
    # Irrelevant preprocessing: reverse and slice (distractor)
    reversed_items = items[::-1]
    mid_section = reversed_items[1:4]
    temp_sum = sum(mid_section) * 0.5  # Dead computation

    # Core logic: weighted score with filtering
    valid_indices = list(filter(lambda x: items[x] > 0, range(len(items))))
    weighted_values = []
    for i in valid_indices:
        adjustment = 1.0
        if i % 2 == 0:
            adjustment += 0.1
        elif i == 3:
            adjustment -= 0.05
        weighted_values.append(items[i] * importance_weights.get(i, 0.8) * adjustment)

    # Secondary distraction: unused aggregation
    peak_value = max(weighted_values) if weighted_values else 0
    smoothed_avg = sum(weighted_values) / len(weighted_values) if weighted_values else 0

    # Final scoring with string-based condition (hybrid paradigm)
    mode_flag = 'dynamic' if len(valid_indices) > 3 else 'static'
    multiplier = 1.2 if 'dyn' in mode_flag else 1.0

    base_score = sum(weighted_values)
    final_score = base_score * multiplier

    # Additional red herring: tuple unpacking that doesn't affect result
    backup_data = (sum(items), sum(importance_weights.values()), temp_sum)
    primary, secondary, _ = backup_data

    return final_score

# Main execution
raw_data = [4, -2, 8, 5, 0, 7]
weights = {0: 1.1, 2: 0.9, 3: 1.3, 5: 0.7}

intermediate_total = sum(x for x in raw_data if x % 2 == 1)  # Distractor
normalization_factor = max(raw_data) / 10.0  # Unused path

final_score = calculate_final_score(raw_data, weights)
print(f"Result: {final_score}")