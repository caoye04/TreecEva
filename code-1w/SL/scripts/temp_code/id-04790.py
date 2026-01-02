def calculate_final_score(entries, limits):
    base_score = 0
    penalty_adjustment = 0
    temp_buffer = []
    cumulative_shift = 0

    # Irrelevant pre-processing (distractor)
    for i, entry in enumerate(entries):
        if i % 3 == 0:
            temp_buffer.append(i * 0.5)

    # Core logic with mixed paradigms
    valid_count = 0
    for idx, (val, meta) in enumerate(zip(entries, [x**0.5 for x in range(len(entries))])):
        shifted_val = val + (idx % 4)
        exceeds_primary = shifted_val > limits['primary']
        meets_secondary = val % 2 == 0

        # Conditional scoring with state tracking
        if exceeds_primary and meets_secondary:
            base_score += int(shifted_val // 2)
            valid_count += 1
        elif not exceeds_primary and val > 10:
            penalty_adjustment -= 1

        # Red herring: accumulating unused values
        cumulative_shift += (shifted_val * 0.1) % 2

    # Secondary processing: another distraction
    outlier_flags = [1 for v in entries if v > limits['primary'] * 1.2]
    flag_sum = sum(outlier_flags)  # Used nowhere critical

    # Real computation path
    multiplier = valid_count if valid_count > 0 else 1
    intermediate = base_score * multiplier

    # Final adjustment using a misleading but inert expression
    noise_term = len(temp_buffer) - flag_sum if flag_sum else 0  # Not actually impactful
    final_score = intermediate - abs(penalty_adjustment)

    return final_score

# Input setup
data = [12, 15, 8, 20, 6, 25, 10]
thresholds = {'primary': 18}

result = calculate_final_score(data, thresholds)
print(f"Target result: {result}")