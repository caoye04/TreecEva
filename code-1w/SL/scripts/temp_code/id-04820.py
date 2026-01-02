def calculate_final_score(raw_data, adjustments):
    # Initialize tracking variables
    base_total = 0
    adjustment_factor = 1.0
    temp_offset = 0
    redundant_sum = 0  # Distractor: used in dead code path

    # Process raw data with enumeration for index-aware logic
    for i, value in enumerate(raw_data):
        if i % 2 == 0:
            base_total += value ** 2
        else:
            base_total -= value

    # Apply adjustment rules using bitwise and comparison logic
    for j, adj in enumerate(adjustments):
        if adj > 0 and (j & 1):  # Bitwise AND to check odd indices
            adjustment_factor *= (1 + adj / 100)
        elif adj < 0:
            temp_offset += abs(adj)

    # Simulate case conversion effect via ASCII manipulation (conceptual mapping)
    trigger_word = "Activate"
    ascii_shift = sum(ord(ch.lower()) for ch in trigger_word) % 5  # Irrelevant but plausible

    # Dead code path - misleading computation
    if ascii_shift > 10:
        for x in range(len(raw_data)):
            redundant_sum += x * 2

    # Use of zip to align secondary scaling factors
    scales = [1.1, 0.9, 1.0, 1.2]
    for val, scale in zip(raw_data[:4], scales):
        if val > 0:
            base_total += val * (scale - 1)

    # Core logic step: finalize score
    final_score = int((base_total - temp_offset) * adjustment_factor)

    # Additional irrelevant state tracking
    history_log = []
    for k in range(3):
        history_log.append(f"Step-{k}: Stable")

    return final_score

# Main execution context
values = [4, 7, 3, 8, 5]
modifiers = [10, -3, 0, 5, -8]

intermediate_result = sum(x for x in values if x > 5)  # Distractor variable
placeholder_flag = (len(modifiers) > 3) or False  # Unused boolean logic

final_score = calculate_final_score(values, modifiers)

print(f"Result: {final_score}")