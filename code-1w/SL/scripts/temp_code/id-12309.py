def calculate_final_score(entries, importance_weights):
    base_score = 0
    adjustment_factor = 0.0
    temp_buffer = []
    cumulative_shift = 0

    # Irrelevant pre-processing (distractor)
    for i, entry in enumerate(entries):
        if i % 2 == 0:
            temp_buffer.append(entry * 1.5)
        else:
            temp_buffer.append(entry + 0.5)

    # Real logic begins: weighted scoring with conditional boosts
    for idx, (val, weight) in enumerate(zip(entries, importance_weights)):
        contribution = val * weight
        
        # Conditional boost based on position and magnitude
        if val > 50 and idx in [1, 3]:
            contribution *= 1.2
        elif val < 10 and idx == 2:
            contribution *= 0.8
        
        # Apply nested conditional scaling
        if idx > 0:
            prev_val = entries[idx - 1]
            if prev_val > val:
                contribution -= 5
            else:
                contribution += 3

        base_score += contribution

    # Secondary adjustment using distractor buffer
    noise_accumulator = 0
    for x in temp_buffer:
        noise_accumulator += x % 7
    adjustment_factor = noise_accumulator / len(temp_buffer)  # Computed but not used directly

    # Final computation path
    scale_modifier = 1.0
    if base_score > 200:
        scale_modifier = 0.95
    elif base_score < 100:
        scale_modifier = 1.05

    # Introduce dead code path (misleading)
    outlier_count = 0
    if False:  # Simulated dead branch
        for v in entries:
            if v > 100:
                outlier_count += 1

    # Actual final score calculation
    intermediate = base_score * scale_modifier
    final_score = int(intermediate - 17)  # Key deterministic transformation

    return final_score

# Input data
raw_data = [45, 67, 8, 92]
weights_list = [0.8, 1.1, 0.9, 1.2]

# Execute main logic
target_result = calculate_final_score(raw_data, weights_list)
print(f"Result: {target_result}")