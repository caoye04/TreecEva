def process_performance(data_str, limit):
    # Irrelevant preprocessing: case conversion and splitting
    normalized = data_str.upper().replace(' ', '').split(',')
    
    # Extract numeric values using list comprehension with filtering
    raw_values = [int(x) for x in normalized if x.isdigit()]
    
    # Misleading intermediate computations (not directly used)
    average_value = sum(raw_values) // len(raw_values) if raw_values else 0
    peak_value = max(raw_values) if raw_values else 0
    fluctuation_index = (peak_value - average_value) % 7
    
    # Distractor: dead computation path
    temp_offset = 0
    for val in raw_values:
        if val > 100:
            temp_offset += val // 10
        elif val < 10:
            temp_offset -= val
    
    # Relevant logic begins: filter values above threshold
    qualified = [v for v in raw_values if v >= limit]
    
    # Apply diminishing returns using modular arithmetic
    adjusted_scores = []
    for i, score in enumerate(qualified):
        penalty = i % 3  # increases every third element
        adjusted = score - penalty
        adjusted_scores.append(adjusted)
    
    # Secondary distraction: unused string transformation chain
    metadata_tag = ''.join([chr(97 + (len(raw_values) % 26)) for _ in range(3)])
    checksum_hint = ''.join(sorted(set(str(len(raw_values) * 11))))
    
    # Final aggregation with conditional boost
    base_total = sum(adjusted_scores)
    if len(qualified) >= 4 and fluctuation_index > 3:
        base_total += 10  # performance bonus
    
    # Key result
    final_score = base_total * 2 // 3  # normalization step
    
    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Input setup
raw_data = "55,30,80,45,12,91,67"
threshold = 40
final_score = process_performance(raw_data, threshold)