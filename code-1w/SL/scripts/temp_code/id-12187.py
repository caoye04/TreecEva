def calculate_final_score(raw_data):
    # Preprocessing: filter and transform data
    processed = list(filter(lambda x: x > 0, raw_data))
    squared = [x ** 2 for x in processed]
    shifted = [x >> 1 for x in squared]  # Bitwise shift as transformation

    # Irrelevant intermediate computation (distractor)
    avg_val = sum(shifted) / len(shifted) if shifted else 0
    temp_result = [y for y in shifted if y < avg_val]  # Unused later

    # Core logic: weighted scoring with conditional boosts
    base_score = 0
    bonus_tracker = []
    for val in shifted:
        if val % 4 == 0:
            base_score += val // 4
            if val % 8 == 0:
                bonus_tracker.append(val // 8)

    # Additional distraction: unused statistical block
    mean = sum(processed) / len(processed) if processed else 0
    variance = sum((x - mean) ** 2 for x in processed) / len(processed) if processed else 0
    std_dev = variance ** 0.5

    # Real contribution: combine base and selective bonuses
    adjustment_factor = len(bonus_tracker) * 3
    final_score = base_score + adjustment_factor

    # Red herring: complex-looking but irrelevant bitwise mix
    mask = 0b1010
    masked_vals = [val ^ mask & 0xF for val in bonus_tracker]  # Not used

    return final_score

# Input data
input_data = [1, 2, 3, 4, 5, 6, 7, 8, -1, 0, 12]

# Execute main logic
final_score = calculate_final_score(input_data)

# Print result
print(f"Result: {final_score}")