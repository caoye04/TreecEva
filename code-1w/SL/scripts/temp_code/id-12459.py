def process_metrics(log_entries):
    total_entries = len(log_entries)
    valid_count = 0
    error_accumulator = 0
    temp_buffer = []
    
    for entry in log_entries:
        if not isinstance(entry, dict) or 'status' not in entry:
            continue
        
        status = entry['status']
        timestamp = entry.get('timestamp', 0)
        duration = entry.get('duration', 0)
        
        # Irrelevant computation: tracking timestamps (distractor)
        if timestamp > 1000:
            temp_buffer.append(timestamp * 0.001)
        
        # Real logic begins
        if status == 'success':
            valid_count += 1
            error_accumulator += max(0, 5 - duration)  # Reward shorter durations
        elif status == 'failed':
            error_accumulator -= 3
        else:
            error_accumulator -= 1

    # Semi-relevant transformation (only partially used)
    average_error_offset = error_accumulator / total_entries if total_entries else 0
    normalized_valid = valid_count / total_entries if total_entries else 0

    # Complex conditional expression (required feature)
    efficiency_modifier = 1.5 if normalized_valid > 0.7 else (0.8 if normalized_valid > 0.4 else 0.3)
    
    # Character counting distraction: count letters in status words
    phantom_counter = sum(len(s) for s in ['success', 'failed', 'pending'])
    dummy_metric = phantom_counter * 0.01  # Unused except to mislead

    # Core calculation
    base_score = valid_count * 10 + error_accumulator
    efficiency_score = base_score * efficiency_modifier  # This is our target

    # Dead code path - never executed under current logic
    if len(temp_buffer) > 100:
        efficiency_score *= 1.1

    final_output = {
        'score': efficiency_score,
        'valid_ratio': normalized_valid,
        'modifier': efficiency_modifier
    }
    
    return final_output

# Input data
entries = [
    {'status': 'success', 'duration': 3},
    {'status': 'success', 'duration': 6},
    {'status': 'failed'},
    {'status': 'success', 'duration': 2},
    {'status': 'unknown'},
    {'status': 'success', 'duration': 1},
    {'status': 'failed'},
    {'status': 'success', 'duration': 4}
]

result_dict = process_metrics(entries)
efficiency_score = result_dict['score']
print(f"Target result: {efficiency_score}")