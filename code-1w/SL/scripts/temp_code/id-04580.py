def process_metrics(entries, importance):
    total = 0
    base_offset = len(entries) * 2
    temp_results = []
    
    # Irrelevant pre-processing (distractor)
    outlier_count = 0
    for val in entries:
        if val < 0:
            outlier_count += 1
    
    # Actual computation with nested logic and mixed paradigms
    for i, (val, weight) in enumerate(zip(entries, importance)):
        adjusted = val * weight
        if i % 2 == 0:
            adjusted = abs(adjusted) ** 0.5  # square root for even indices
        else:
            adjusted = adjusted / (i + 1)
        
        # Bitwise interference (only affects every third element, but not used later)
        debug_flag = (i ^ 3) & 1
        temp_buffer = adjusted << debug_flag  # shift based on flag (unused)
        
        temp_results.append(round(adjusted, 4))
    
    # Secondary loop with filtering (some distraction)
    filtered_sum = sum(x for x in temp_results if x > 1.0)
    scaling_factor = 1.5 if filtered_sum > 10 else 1.0
    
    # Core accumulation logic
    for j, item in enumerate(temp_results):
        multiplier = 1
        if j < len(importance) and importance[j] & 1:  # bitwise check
            multiplier += 0.1
        total += item * multiplier
    
    final_score = int(total * scaling_factor) + base_offset
    
    # Dead code path (never executed, adds confusion)
    backup_mode = False
    if False and backup_mode:
        fallback = sum(entries) // (len(entries) or 1)
        final_score = fallback

    return final_score

# Input data
data = [8, -4, 12, 6, 10]
weights = [3, 2, 5, 1, 4]

# Execute and print result
target_result = process_metrics(data, weights)
print(f"Result: {target_result}")