def calculate_final_score(raw_data):
    # Preprocessing: filter and transform relevant entries
    processed = list(map(lambda x: x * 1.5 if x > 10 else x * 0.8, raw_data))
    
    # Irrelevant statistics (distractor computations)
    avg_val = sum(processed) / len(processed) if processed else 0
    max_val = max(processed) if processed else 0
    outlier_count = sum(1 for x in processed if x > 2 * avg_val)  # Likely zero, not used
    
    # Relevant conditional logic with slicing
    segment_a = processed[:len(processed)//2]
    segment_b = processed[len(processed)//2:]
    
    bonus = 0
    if len(segment_a) > 3:
        bonus += 5
        temp_sum = sum(segment_a[1:-1])  # Middle elements
        if temp_sum > 15:
            bonus += 3
    
    # Misleading control flow - looks important but unused
    penalty = 0
    for val in segment_b:
        if val < 0:
            penalty += 1  # Never triggered in this data
    adjustment = penalty * 2  # Dead computation
    
    # Core scoring logic
    base_score = sum(segment_a) * 0.9
    growth_factor = (segment_b[-1] / segment_b[0]) if segment_b[0] != 0 else 1
    dynamic_score = base_score * growth_factor
    
    # Final composition
    final_score = int(dynamic_score + bonus)  # Truncate to integer
    
    # Additional red herring: complex unused calculation
    shadow_score = sum(x**2 for x in processed if x % 2 == 0)
    normalized = shadow_score / (final_score or 1)
    
    return final_score

# Main execution context
raw_dataset = [8, 12, 14, 7, 11, 13]
interim_result = [x for x in raw_dataset if x % 2 == 0]  # Even numbers only (distractor)
eval_mask = [True, False] * 3
filtered_pairs = [(raw_dataset[i], eval_mask[i]) for i in range(len(raw_dataset))]

# Key statement
final_score = calculate_final_score(raw_dataset)
print(f"Result: {final_score}")