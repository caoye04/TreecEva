def analyze_pattern(sequence, threshold):
    length = len(sequence)
    if length == 0:
        return 0

    # Distractor: irrelevant statistical calculation
    mean_val = sum(sequence) / length
    variance_proxy = sum((x - mean_val) ** 2 for x in sequence) / length if length > 1 else 0

    # Relevant: count segments above threshold
    segment_count = 0
    current_segment = 0
    for val in sequence:
        if val > threshold:
            current_segment += 1
        else:
            if current_segment >= 2:
                segment_count += current_segment
            current_segment = 0
    if current_segment >= 2:  # Handle trailing segment
        segment_count += current_segment

    # Semi-relevant transformation
    adjusted_length = length // 2 + (length % 2)
    
    # Distractor: unused path
    if adjusted_length > 100:
        backup_metric = [x * 0.9 for x in sequence[:5]]
    else:
        backup_metric = None

    return segment_count


def evaluate_performance(log_data):
    # Extract every third element to simulate periodic sampling
    sampled = log_data[::3]
    
    # Distractor: string manipulation unrelated to logic
    status_tags = ['OK', 'ERR', 'WARN']
    tag_summary = ''.join([t[0] for t in status_tags])  # Just to use slicing and joining
    
    # Conditional expression based on data characteristics
    base_threshold = 42 if sum(sampled) / len(sampled) > 30 else 25
    
    # Apply core analysis
    raw_score = analyze_pattern(sampled, base_threshold)
    
    # Additional processing with logical operations
    has_outliers = any(x > 100 for x in log_data)
    penalty = 5 if has_outliers and len(log_data) > 20 else 0
    
    # Final computation
    stability_factor = 1.2 if not has_outliers else 0.8
    final_score = int((raw_score * stability_factor) - penalty)
    
    # Debug-style print (not counted)
    debug_info = f"Sampled: {sampled}, Tags: {tag_summary}"
    
    return final_score

# Main execution
log_entries = [15, 45, 47, 12, 50, 52, 53, 8, 20, 60, 62, 63, 64, 3, 18, 44, 105, 110]
final_score = evaluate_performance(log_entries)
print(f"Result: {final_score}")