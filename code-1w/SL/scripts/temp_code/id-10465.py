def analyze_pattern(data, width):
    if len(data) < width:
        return -1

    # Irrelevant transformation (distractor)
    temp_shadow = [x ** 2 for x in data]
    offset_map = sum([i * v for i, v in enumerate(data)])  # Unused

    # Core logic begins
    subsegments = []
    for i in range(len(data) - width + 1):
        subsegment = data[i:i + width]  # slicing operation
        subsegments.append(subsegment)

    # Secondary processing with decoy logic
    filtered_segments = []
    control_flag = False
    for seg in subsegments:
        avg = sum(seg) / len(seg)
        variance = sum((x - avg) ** 2 for x in seg) / len(seg)
        if variance > 2.5:  # arbitrary threshold (misleading)
            control_flag = True
        if len(set(seg)) == width and seg[0] % 2 == 0:  # actual filter condition
            filtered_segments.append(seg)

    # Dead path (never executed due to logic)
    if control_flag and len(filtered_segments) == 0:
        backup_result = sum(temp_shadow) // 17
        return backup_result

    # Real computation path
    score_pool = []
    for fs in filtered_segments:
        product = 1
        for val in fs:
            product *= val
        score_pool.append(product % 19)

    # Final aggregation
    filtration_score = sum(score_pool) * len(filtered_segments)
    
    # Unused variables (red herrings)
    mirror_check = data[::-1]
    pivot_index = len(data) // 3
    dummy_accumulator = 0
    for k in range(pivot_index):
        dummy_accumulator += mirror_check[k] * (k + 1)

    return filtration_score

# Main execution
sequence = [2, 5, 8, 3, 6, 9, 4, 7]
window_size = 3
redundant_copy = sequence[:]  # distractor
padding_shift = [0] * 2  # unused buffer

# Key call
filtration_score = analyze_pattern(sequence, window_size)

# Output target result
print(f"Target result: {filtration_score}")