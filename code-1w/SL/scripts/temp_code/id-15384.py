def calculate_final_score(raw_data, limit):
    # Preprocessing: filter and transform
    processed = [x ** 0.5 for x in raw_data if x > 0]
    
    # Irrelevant transformation (distractor)
    temp_stats = {
        'sum': sum(processed),
        'max': max(processed),
        'count': len(processed)
    }
    
    # Misleading normalization (not used later)
    normalized = [round(x / (temp_stats['max'] + 1e-9), 3) for x in processed]
    
    # Actual logic begins: count how many pass threshold
    above_threshold = [val for val in processed if val >= limit]
    
    # Secondary filter based on string condition (hybrid type reasoning)
    labels = [f"item_{i}" for i in range(len(raw_data))]
    valid_labels = [lbl for lbl in labels if lbl.endswith('3') or lbl.endswith('7')]
    
    # Dummy usage of labels (semi-relevant but doesn't affect score)
    label_flag = any("7" in lb for lb in valid_labels)
    
    # Core scoring logic
    base_score = len(above_threshold) * 10
    bonus = 5 if label_flag and len(above_threshold) > 2 else 0
    
    # Red herring: unused complex computation
    outlier_check = [p for p in processed if p > 3 * (sum(processed) / len(processed) + 1e-9)]
    stability_index = len(outlier_check) == 0
    
    # Final calculation
    final_score = base_score + bonus
    return final_score

# Main data
input_data = [16, 25, 9, 0, 36, 49, -4, 64]
threshold = 5.0

# Execute
result = calculate_final_score(input_data, threshold)
print(f"Target result: {result}")