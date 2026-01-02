def evaluate_performance(log_entries, threshold):
    # Irrelevant counters (distractors)
    warning_count = 0
    debug_count = 0
    info_count = 0

    # Relevant data extraction
    event_durations = [entry[2] for entry in log_entries if entry[1] == 'TASK']
    
    # Misleading filtering based on text length
    long_messages = [msg for msg in log_entries if len(msg[0]) > 20]
    message_lengths = sum(len(entry[0]) for entry in long_messages)

    # Semi-relevant preprocessing: reverse and slice last 4 valid durations
    sorted_durations = sorted(event_durations, reverse=True)
    top_durations = sorted_durations[:4]  # Only use top 4

    # Conditional logic with red herring variables
    adjustment_factor = 1.0
    if len(top_durations) >= 3:
        avg_top = sum(top_durations) / len(top_durations)
        if avg_top > threshold:
            adjustment_factor = 0.9
        else:
            adjustment_factor = 1.1  # Distractor branch not taken

    # Another distraction: character frequency count in labels
    label_chars = ''.join(entry[0] for entry in log_entries)
    critical_char_count = label_chars.count('C') + label_chars.count('R')

    # Core calculation (depends only on top_durations and threshold)
    base_score = sum(d ** 0.5 for d in top_durations)  # sqrt of each top duration
    penalty = abs(len(log_entries) - len(top_durations)) * 2  # minor penalty

    final_score = int((base_score * adjustment_factor) - penalty)

    # Dead code path - never affects result
    if critical_char_count > 10:
        final_score += 100

    return final_score

# Simulated system log: (label, type, duration_ms)
logs = [
    ('CACHE_HIT', 'INFO', 10),
    ('CRITICAL_TASK', 'TASK', 25),
    ('DATA_FETCH', 'TASK', 9),
    ('CONFIG_READ', 'DEBUG', 3),
    ('NETWORK_CALL', 'TASK', 64),
    ('COMPRESS_DATA', 'TASK', 49),
    ('RETRY_CYCLE', 'TASK', 36),
    ('VALIDATE_INPUT', 'INFO', 7)
]

total_entries = len(logs)
threshold = 30

# Key execution point
final_score = evaluate_performance(logs, threshold)
print(f"Result: {final_score}")