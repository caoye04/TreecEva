def calculate_performance(data_map):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    temp_offset = 0.01
    
    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    normalized_sum = 0.0
    adjusted_values = []
    
    for key in data_map:
        if key.startswith('tmp') or key == 'meta':
            continue  # Skip irrelevant keys
        
        raw_value = data_map[key]
        
        # Simulate noise filtering (partially relevant)
        if raw_value < 10:
            outlier_count += 1
            continue
        
        # Core transformation logic
        capped_value = min(raw_value, 100)
        weighted_score = capped_value * base_multiplier
        
        if capped_value > bonus_threshold:
            weighted_score += 5
        
        # Conditional expression for dynamic adjustment
        adjustment = 2.0 if weighted_score > 90 else (1.0 if weighted_score > 70 else 0.5)
        weighted_score *= adjustment
        
        adjusted_values.append(weighted_score)
    
    # Dummy normalization (not used in final result)
    if adjusted_values:
        avg_adjusted = sum(adjusted_values) / len(adjusted_values)
        for val in adjusted_values:
            normalized_sum += (val - avg_adjusted) ** 2
        
    # Real computation path
    raw_total = sum(data_map[k] for k in data_map if k not in ['meta', 'tmp1', 'tmp2'])
    valid_count = len([v for k, v in data_map.items() if k not in ['meta', 'tmp1', 'tmp2'] and v >= 10])
    base_score = raw_total * 0.8
    
    # Apply decay based on missing entries
    expected_entries = 5
    missing_penalty = (expected_entries - valid_count) * 3
    
    # Final score calculation
    final_raw = base_score - missing_penalty
    
    # Dictionary-based grade mapping (semi-relevant)
    grade_map = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
    performance_level = 'A' if final_raw >= 85 else 'B' if final_raw >= 75 else 'C'
    
    # Only this line matters for output
    final_score = int(final_raw + grade_map.get(performance_level, 75) * 0.1)
    
    return final_score

# Setup input data
benchmark_data = {
    'task1': 92,
    'task2': 87,
    'task3': 96,
    'tmp1': 5,         # ignored
    'tmp2': 3,         # ignored
    'meta': 'xyz',     # ignored
}

# Execute main logic
result = calculate_performance(benchmark_data)
print(f"Result: {result}")