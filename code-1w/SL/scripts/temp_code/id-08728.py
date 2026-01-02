def calculate_final_score(data_map):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_offset = 0

    # Irrelevant tracking variables (distractors)
    total_entries = len(data_map)
    temp_sum = 0
    ignored_result = [x ** 0.5 for x in range(1, 6)]  # Dead computation

    for key, values in data_map.items():
        if len(values) > 2:
            chunk_sum = sum(v ** 2 for v in values if v % 2 == 1)  # Sum of squares of odd values
            base_score += chunk_sum % 7

            # Conditional bonus logic
            if chunk_sum > 10:
                bonus_multiplier *= 1.1

        else:
            penalty_offset += len(values)

    # Secondary loop using enumerate and zip (required features)
    indices = list(range(len(data_map)))
    for i, (idx, (k, v)) in enumerate(zip(indices, data_map.items())):
        if i % 2 == 0 and len(v) >= 3:
            base_score += k % 4  # Additional score adjustment

    # Final score calculation
    final_score = int((base_score * bonus_multiplier) - penalty_offset)
    return final_score

# Data setup
raw_segments = {
    0: [3, 5, 7, 2],
    1: [4, 6],
    2: [1, 9, 5],
    3: [8],
    4: [11, 3, 7, 1, 9]
}

# Preprocessing with dictionary operations (required feature)
processed_data = {}
for key, segment in raw_segments.items():
    filtered = [x for x in segment if x > 2]
    processed_data[key] = filtered if len(filtered) > 0 else [0]

# Misleading auxiliary computation (distractor)
duplicate_check = {k: len(v) for k, v in processed_data.items()}
total_length = sum(duplicate_check.values())
normalization_factor = total_length / max(duplicate_check.values()) if duplicate_check else 1

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")