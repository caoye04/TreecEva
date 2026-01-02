def calculate_final_score(log, weight_map):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result_cache = {}

    # Irrelevant pre-processing: character frequency count (distractor)
    char_freq = {}
    for entry in log:
        text = entry.get('msg', '')
        for c in text.lower():
            if c.isalpha():
                char_freq[c] = char_freq.get(c, 0) + 1

    # Real logic begins: score accumulation based on event type and severity
    event_counts = {}
    total_events = 0
    for record in log:
        e_type = record['type']
        severity = record['severity']
        active_flag = record.get('active', True)

        if not active_flag:
            continue  # Skip inactive events

        if e_type not in event_counts:
            event_counts[e_type] = 0
        event_counts[e_type] += 1
        total_events += 1

        # Accumulate base score with weighted severity
        base_score += severity * 5

        # Track bonuses for specific rare conditions
        if e_type == 'critical' and severity > 8:
            bonus_tracker.append(severity * 2)

        # Red herring: unused complex computation
        complex_key = f'{e_type}_{severity % 3}'
        if complex_key not in temp_result_cache:
            temp_result_cache[complex_key] = (severity ** 2 + len(e_type)) // 2

    # Bonus application: only if more than one critical high-sev event
    if len(bonus_tracker) > 1:
        penalty_adjustment = sum(bonus_tracker) // 2

    # Weighted adjustment using dictionary mapping
    weighted_component = 0
    for e_type, count in event_counts.items():
        weight = weight_map.get(e_type, 1.0)
        weighted_component += count * weight

    # Dummy floating point distraction
    avg_char_freq = 0.0
    if char_freq:
        avg_char_freq = sum(char_freq.values()) / len(char_freq)
        avg_char_freq = round(avg_char_freq, 3)

    # Final composition
    scale_factor = log[0]['timestamp'] % 100
    final_score = (base_score + penalty_adjustment) // 2
    final_score += int(weighted_component)
    
    # Dead code branch: never executed due to prior filtering
    redundant_correction = 0
    for record in log:
        if record.get('status') == 'invalid':  # This field doesn't exist
            redundant_correction -= 10

    return final_score

# Input data setup
data_log = [
    {'type': 'info', 'severity': 2, 'active': True, 'timestamp': 1001, 'msg': 'System boot'},
    {'type': 'warning', 'severity': 5, 'active': True, 'timestamp': 1005, 'msg': 'High memory'},
    {'type': 'critical', 'severity': 9, 'active': True, 'timestamp': 1010, 'msg': 'CRITICAL FAILURE'},
    {'type': 'critical', 'severity': 10, 'active': True, 'timestamp': 1015, 'msg': 'EMERGENCY'},
    {'type': 'info', 'severity': 1, 'active': False, 'timestamp': 1020, 'msg': 'Routine check'}  # Inactive
]

weights = {
    'info': 0.5,
    'warning': 1.2,
    'critical': 3.0
}

# Execution
final_score = calculate_final_score(data_log, weights)
print(f"Result: {final_score}")