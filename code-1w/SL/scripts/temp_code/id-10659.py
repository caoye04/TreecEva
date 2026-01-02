def process_metrics(log_entries, cutoff):
    total_entries = len(log_entries)
    valid_count = 0
    error_accumulator = 0
    temp_buffer = []
    
    for entry in log_entries:
        # Irrelevant transformation (distractor)
        transformed = (entry * 3) + 2
        temp_buffer.append(transformed)
        
        if entry < 0:
            error_accumulator += abs(entry)
        elif entry >= cutoff:
            valid_count += 1
    
    # Unused intermediate calculation (dead code path)
    if error_accumulator > 100:
        saturation_level = error_accumulator // 10
    else:
        saturation_level = 0  # Not used later

    # Core logic: efficiency = valid_count * 100 / total_entries
    efficiency_rate = (valid_count * 100) // total_entries if total_entries > 0 else 0
    
    # Secondary metric (not needed)
    average_error = error_accumulator / total_entries if total_entries > 0 else 0
    
    # List comprehension to filter high-value entries (semi-relevant)
    significant_events = [x for x in log_entries if x > cutoff * 2]
    event_boost = len(significant_events) * 2
    
    # Final score combines efficiency and boost
    efficiency_score = efficiency_rate + event_boost
    
    # Red herring: unused normalization
    normalized_score = efficiency_score / 150.0 if efficiency_score > 0 else 0
    
    final_output = efficiency_score
    return final_output

# Input data
raw_data = [10, 15, 20, 25, 8, 12, 30, 35, 40, 7, 18, 22, 27, 32, 37]
cutoff_threshold = 20

efficiency_score = 0
final_output = process_metrics(raw_data, cutoff_threshold)
print(f"Result: {final_output}")