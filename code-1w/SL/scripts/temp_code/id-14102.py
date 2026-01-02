def process_task_log(log_entries, threshold_char):
    char_count = 0
    valid_tasks = []
    temp_buffer = []
    total_lines = len(log_entries)
    line_counter = 0

    for entry in log_entries:
        line_counter += 1
        if not entry.strip():
            continue
        
        # Irrelevant string processing (distractor)
        stripped = entry.strip().lower()
        if threshold_char in stripped:
            char_count += stripped.count(threshold_char)

        # Actual logic: extract task ID and status
        if '[TASK]' in entry and 'COMPLETED' in entry:
            task_id = entry.split('[TASK]')[1].split(':')[0].strip()
            duration_str = entry.split('DURATION=')[1].split()[0]
            try:
                duration = float(duration_str)
                temp_buffer.append((task_id, duration))
            except (IndexError, ValueError):
                continue

    # Secondary filtering (semi-relevant)
    min_duration = float('inf')
    for _, duration in temp_buffer:
        if duration < min_duration:
            min_duration = duration

    # Finalize valid tasks above average duration
    durations = [d for _, d in temp_buffer]
    avg_duration = sum(durations) / len(durations) if durations else 0
    
    for task_id, duration in temp_buffer:
        if duration >= avg_duration - 0.5:
            valid_tasks.append((task_id, duration))

    # Red herring computation
    compression_ratio = len(valid_tasks) / total_lines if total_lines else 0
    metadata_hash = (len(temp_buffer) * 37) % 101

    return valid_tasks, char_count, min_duration


def evaluate_performance(tasks, multiplier):
    score = 0
    duration_sum = 0
    penalty = 0

    for tid, dur in tasks:
        # Scoring logic
        if len(tid) > 4:
            score += 10
        else:
            score += 5
        
        duration_sum += dur
        
        # Dummy checksum (not used)
        checksum = sum(ord(c) for c in tid) % 256

    average_duration = duration_sum / len(tasks) if tasks else 0

    # Apply multiplier based on performance tier
    if average_duration < 2.0:
        score *= 1.5
    elif average_duration < 4.0:
        score *= 1.2
    else:
        penalty = 15

    final_score = int((score - penalty) * multiplier)

    # Dead code path (distractor)
    if final_score < 0:
        final_score = 0
    
    return final_score

# Main execution
log_data = [
    "[SYSTEM] Initializing task manager...",
    "[TASK] TX100 : CONFIGURATION - COMPLETED DURATION=3.2s STATUS=OK",
    "",
    "[TASK] AB7 : DATA FETCH - COMPLETED DURATION=1.8s STATUS=OK",
    "[TASK] LONGTASK2024 : STREAMING - COMPLETED DURATION=4.5s STATUS=OK",
    "[TASK] S8 : PROCESSING - COMPLETED DURATION=2.1s STATUS=OK",
    "[TASK] FINALIZE_X : CLEANUP - COMPLETED DURATION=3.9s STATUS=OK"
]

parsed_tasks, char_freq, min_time = process_task_log(log_data, 'a')
base_multiplier = 2.0

# Key statement
final_score = evaluate_performance(parsed_tasks, base_multiplier)

print(f"Result: {final_score}")