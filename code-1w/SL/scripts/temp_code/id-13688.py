def analyze_performance(log_data):
    base_points = 0
    penalty_count = 0
    temp_buffer = []
    adjusted_sum = 0
    outlier_threshold = 100
    correction_factor = 1.0
    
    # Process each entry in the log
    for entry in log_data.split(','):
        clean_entry = entry.strip().lower()
        
        if 'error' in clean_entry:
            penalty_count += 1
            continue
        
        try:
            raw_value = int(clean_entry)
            temp_buffer.append(raw_value)
            
            if raw_value > outlier_threshold:
                base_points += raw_value // 3
            else:
                base_points += raw_value
        except ValueError:
            # Irrelevant data, skip
            pass

    # Simulate some intermediate analysis (not used directly)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    high_performers = [x for x in temp_buffer if x > 85]
    buffer_stats = {'count': len(temp_buffer), 'mean': avg_temp}

    # Key distraction: conditional expression with unused path
    status_flag = 'optimal' if len(high_performers) > 2 else 'review_needed'
    scaling_modifier = 0.95 if status_flag == 'optimal' else 1.05

    # Actual computation chain
    raw_total = sum(temp_buffer)
    deduction = penalty_count * 10
    adjusted_sum = raw_total - deduction
    
    # Correction based on data quality
    if 'clean' in log_data.lower():
        correction_factor = 1.1
    else:
        correction_factor = 0.9

    # Final scoring step
    final_score = round(adjusted_sum * correction_factor)
    
    # Dead code - never accessed
    if final_score < 0:
        final_score = 0

    return final_score

# Input data with mixed content
data_log = "85, 92, error: retry, 78, 96, 88, invalid, 94"
result = analyze_performance(data_log)
print(f"Result: {result}")