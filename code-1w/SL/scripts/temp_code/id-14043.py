def analyze_performance(logs, min_threshold):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    outlier_count = 0
    cumulative_weight = 0.0

    # Misleading initialization - not all used in final logic
    stats_cache = {}
    debug_trace = []
    rolling_avg = 0

    for i, entry in enumerate(logs):
        char_count = len(entry['message'])
        priority = entry.get('priority', 1)
        weight = 1 + (char_count // 10) * 0.1

        # Irrelevant computation - simulates data analysis but unused
        if char_count > 50:
            debug_trace.append(f"Long message at {i}")
            cumulative_weight += weight * 0.5

        # Core logic begins
        severity = entry['severity']
        adjusted_severity = severity * weight

        temp_sum += adjusted_severity

        if severity >= min_threshold:
            valid_count += 1

        # Dead code path - looks meaningful but never affects result
        if i % 100 == 0:
            dummy_var = i ** 2
            stats_cache[i] = dummy_var  # Unused cache

    # Secondary loop using zip - combines with phantom indices
    indices = list(range(total_entries))
    phantom_map = [x * 0.1 for x in indices]
    contribution = 0

    for idx, (log, ph_val) in enumerate(zip(logs, phantom_map)):
        if log['severity'] > 3:
            contribution += ph_val * log['severity']

    # Conditional expression with red herring
    fallback_mode = True if valid_count < 5 else False
    adjustment_factor = 0.8 if fallback_mode else 1.2

    # Key distraction: complex-looking but irrelevant sorting
    sorted_logs = sorted(logs, key=lambda x: len(x['message']), reverse=True)
    mid_index = len(sorted_logs) // 2
    median_length = len(sorted_logs[mid_index]['message'])

    # Real answer computation - depends only on temp_sum and valid_count
    base_score = temp_sum / total_entries if total_entries > 0 else 0
    bonus = valid_count * 0.5
    final_score = base_score + bonus - 2  # Final deterministic formula

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_logs = [
    {'message': 'System boot successful', 'severity': 1, 'priority': 2},
    {'message': 'Minor delay in process startup detected during initialization sequence', 'severity': 4, 'priority': 3},
    {'message': 'All services operational', 'severity': 2, 'priority': 1},
    {'message': 'High-frequency error burst observed in network module', 'severity': 5, 'priority': 4},
    {'message': 'Resource usage within normal parameters', 'severity': 1, 'priority': 1},
    {'message': 'Unexpected disconnection from primary node', 'severity': 5, 'priority': 5},
    {'message': 'Scheduled maintenance completed', 'severity': 3, 'priority': 2}
]
threshold = 4

final_score = analyze_performance(feedback_logs, threshold)