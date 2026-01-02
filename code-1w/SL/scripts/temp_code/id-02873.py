def calculate_final_score(data, limits):
    # Preprocess: filter valid entries and normalize case (irrelevant for numbers but included)
    processed = [x for x in data if isinstance(x, (int, float)) and x >= 0]
    
    # Distractor: tracking state that isn't used
    max_value = max(processed) if processed else 0
    temp_stats = {'count': len(processed), 'peak': max_value}
    
    # Actual logic begins: categorize values based on thresholds
    low_tier = {x for x in processed if x < limits[0]}
    mid_tier = {x for x in processed if limits[0] <= x < limits[1]}
    high_tier = {x for x in processed if x >= limits[1]}
    
    # Compute tier scores with weighted contributions
    score_a = sum(low_tier) * 0.5
    score_b = sum(mid_tier) * 1.2
    score_c = sum(high_tier) * 2.0
    
    # Distractor: unused intermediate calculations
    avg_high = sum(high_tier) / len(high_tier) if high_tier else 0
    outlier_count = len([x for x in processed if x > 3 * avg_high]) if high_tier else 0
    
    # Final aggregation
    aggregate = score_a + score_b + score_c
    penalty = len(low_tier) * 0.3  # small deduction per low-tier item
    final_score = aggregate - penalty
    
    # Additional red herring: modifying unrelated structure
    temp_stats['adjusted_peak'] = max_value + penalty
    
    return final_score

# Input data with mixed types and irrelevant entries
data_set = [10, -5, 'ignore', 25, 8, 30, None, 15, 40, 7]
thresholds = (12, 25)

# Execute computation
result = calculate_final_score(data_set, thresholds)
final_score = round(result, 4)
print(f"Result: {final_score}")