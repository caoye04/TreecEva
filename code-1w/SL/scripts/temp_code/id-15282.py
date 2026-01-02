def process_metrics(entries, config):
    total = 0
    penalty = 0
    bonus_tracker = []
    temp_result = 0

    for entry in entries:
        # Irrelevant string processing (distractor)
        name_clean = entry['name'].strip().lower()
        if 'test' in name_clean:
            continue

        raw_value = entry['value']
        category = entry['type']

        # Actual logic begins
        if category == 'A':
            temp_result += raw_value * 1.2
        elif category == 'B':
            temp_result += raw_value * 0.85
        else:
            temp_result += raw_value * 0.6

        # Bitwise flag check (semi-relevant)
        flags = entry.get('flags', 0)
        if flags & 0x1:
            bonus_tracker.append(raw_value)

        # Mod arithmetic distractor
        if raw_value % 7 == 0:
            penalty += 3

    # Distractor: unused aggregation
    avg_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0

    # Main scoring logic with conditional modifiers
    base_score = int(temp_result)
    if base_score > config['limit']:
        adjustment = base_score * config['penalty_rate']
        base_score -= int(adjustment)

    # Final threshold override
    threshold_met = all(base_score >= t for t in config['min_thresholds'])
    final_score = base_score + (5 if threshold_met else -10)

    # Dead code path (distractor)
    if False:
        debug_log = f"Final score adjusted: {final_score}"
        print(debug_log)

    return final_score

# Data setup
config_data = {
    'limit': 150,
    'penalty_rate': 0.1,
    'min_thresholds': [95, 100]
}

data = [
    {'name': ' Alice ', 'value': 50, 'type': 'A', 'flags': 1},
    {'name': 'Bob_Test', 'value': 40, 'type': 'B'},
    {'name': ' Charlie ', 'value': 60, 'type': 'C', 'flags': 2},
    {'name': 'Diana', 'value': 35, 'type': 'A', 'flags': 3},
    {'name': ' Eve ', 'value': 70, 'type': 'B'}
]

# Execute and print result
result_var = process_metrics(data, config_data)
print(f"Result: {result_var}")