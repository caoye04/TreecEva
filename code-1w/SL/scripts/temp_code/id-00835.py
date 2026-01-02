def calculate_final_score(items, factors):
    temp_scores = []
    adjustment = 0.0
    base_offset = sum([i % 7 for i in range(10)]) / 2  # Irrelevant computation
    
    for idx, (val, weight) in enumerate(zip(items, factors)):
        if idx % 2 == 0:
            transformed = (val ** 0.5) * weight
        else:
            transformed = (val + idx) // (weight + 1)
        
        # Dead code path - never executed due to logic
        if val < 0:
            adjustment += val ** 2
        
        temp_scores.append(int(transformed))

    # Secondary processing with distractor variables
    cumulative = 0
    checksum = 0  # Unused variable
    for i, score in enumerate(temp_scores):
        checksum ^= score  # Bitwise distraction
        if i > 0 and temp_scores[i] > temp_scores[i-1]:
            cumulative += score * 2
        else:
            cumulative += score

    # Linear search for pattern (semi-relevant)
    peak_index = 0
    for i in range(1, len(temp_scores)):
        if temp_scores[i] > temp_scores[peak_index]:
            peak_index = i

    # Final computation with red herring adjustment
    magic_factor = 3.1415
    dummy_accum = 0
    for x in [2, 4, 6]:
        dummy_accum += magic_factor * x  # Irrelevant accumulation

    result = cumulative + peak_index - int(base_offset)
    return result

# Input data
raw_data = [16, 25, 9, 36, 49]
weights_list = [2, 3, 1, 4, 2]

# Execute
result = calculate_final_score(raw_data, weights_list)
print(f"Target result: {result}")