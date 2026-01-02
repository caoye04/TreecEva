def calculate_performance(data):
    base_weight = 0.8
    bonus_multiplier = 1.2
    penalty_factor = 0.9
    
    # Irrelevant preprocessing: normalize unrelated metrics
    normalized_sizes = [x / max(data) for x in data if x > 0]
    size_offsets = [abs(len(str(x)) - 2) for x in data]
    
    # Key computation path
    valid_entries = [x for x in data if x >= 10]
    adjusted_values = []
    
    for idx, val in enumerate(valid_entries):
        if idx % 2 == 0:
            adjusted_val = val * base_weight
        else:
            adjusted_val = val * penalty_factor
        adjusted_values.append(round(adjusted_val))
    
    # Secondary adjustment with conditional logic
    boosted_values = [
        x * bonus_multiplier if x < 50 else x 
        for x in adjusted_values
    ]
    
    # Dummy tracking variables (not used in final result)
    avg_size_offset = sum(size_offsets) / len(size_offsets) if size_offsets else 0
    peak_value = max(data)
    entry_count = len(data)
    
    raw_total = sum(boosted_values)
    correction_shift = len(valid_entries) - len(data)
    intermediate_score = raw_total + (correction_shift * 3)
    
    # Final scoring with clamp
    final_score = max(intermediate_score, 20)
    
    # Additional red herring: sorting unused list
    sorted_normals = sorted(normalized_sizes, reverse=True)
    padding_factor = sum([1 for x in sorted_normals if x < 0.5])
    
    return int(final_score)

# Input data
benchmark_data = [15, 25, 8, 40, 12, 5, 30]

# Execute and print result
result = calculate_performance(benchmark_data)
print(f"Result: {result}")