def calculate_final_score(log_entries, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result_cache = {}

    # Irrelevant string processing (distractor)
    formatted_labels = [label.upper().strip() for label in importance_weights.keys()]
    filtered_labels = [lbl for lbl in formatted_labels if 'ERROR' not in lbl]

    # Real computation begins
    event_counts = {key: 0 for key in importance_weights}
    for entry in log_entries:
        event_type = entry['type']
        severity = entry['severity']
        if event_type in event_counts:
            event_counts[event_type] += severity

    # Bonus logic with lambda (relevant)
    apply_bonus = lambda count: count * 1.5 if count > 10 else count
    for key in event_counts:
        if event_counts[key] > 0:
            bonus_tracker.append(apply_bonus(event_counts[key]))

    # Dead code path (distractor)
    if len(temp_result_cache) == 100:
        reset_flag = True
        base_score -= sum(temp_result_cache.values())

    # Actual scoring
    raw_sum = sum(event_counts.values())
    bonus_sum = sum(bonus_tracker)
    total_weight = sum(importance_weights.values())

    # More distractions: unused intermediate calculations
    avg_severity = raw_sum / (len(log_entries) or 1)
    peak_event = max(event_counts, key=lambda k: event_counts[k])
    peak_value = event_counts[peak_event]
    decay_factor = 0.95 ** len(log_entries)

    # Final score calculation (critical)
    base_score += raw_sum
    base_score += bonus_sum // 2
    penalty_adjustment = len([e for e in log_entries if e['severity'] < 0]) * 2
    final_score = int((base_score - penalty_adjustment) * (total_weight / 10))

    return final_score

# Simulated input data
data_log = [
    {'type': 'INFO', 'severity': 3},
    {'type': 'WARNING', 'severity': 5},
    {'type': 'ERROR_CRITICAL', 'severity': 8},
    {'type': 'INFO', 'severity': 4},
    {'type': 'WARNING', 'severity': 6},
    {'type': 'ERROR_CRITICAL', 'severity': 7},
    {'type': 'DEBUG', 'severity': 2}
]

weights = {
    'INFO': 1.0,
    'WARNING': 1.5,
    'ERROR_CRITICAL': 3.0,
    'DEBUG': 0.5
}

# Execution point
final_score = calculate_final_score(data_log, weights)
print(f"Result: {final_score}")