def evaluate_performance(log_entries):
    base_threshold = 75
    bonus_factor = 1.2
    penalty_factor = 0.8
    intermediate_sum = 0
    temp_result = 0

    # Track valid assessments and compute base score
    valid_assessments = set()
    flagged_entries = set()
    for entry in log_entries:
        category = entry['type']
        score = entry['value']
        if category == 'technical':
            if score >= base_threshold:
                valid_assessments.add(entry['id'])
                intermediate_sum += score * bonus_factor
            else:
                flagged_entries.add(entry['id'])
                intermediate_sum -= 5
        elif category == 'behavioral':
            if score < 60:
                flagged_entries.add(entry['id'])
            intermediate_sum += max(score, 50)  # Floor for behavioral

    # Dummy tracking to increase cognitive load
    audit_trace = []
    for aid in sorted(valid_assessments):
        audit_trace.append(f'V-{aid}')
    for fid in sorted(flagged_entries):
        audit_trace.append(f'F-{fid}')

    # Secondary computation with partial relevance
    adjustment = 0
    if len(valid_assessments) > 3:
        adjustment += 10
    if len(flagged_entries) >= 2:
        adjustment -= len(flagged_entries) * 3

    # Irrelevant statistical check (distractor)
    avg_flagged = 0
    if flagged_entries:
        total_flagged = sum(e['value'] for e in log_entries if e['id'] in flagged_entries)
        avg_flagged = total_flagged / len(flagged_entries)

    # Core logic step: apply modular adjustment based on count parity
    mod_adjust = len(valid_assessments) % 4
    if mod_adjust == 0:
        temp_result = intermediate_sum + adjustment
    else:
        temp_result = intermediate_sum - adjustment

    # Final scaling using comparison logic
    scaling_factor = 1.1 if intermediate_sum > 300 else 0.95
    final_score = int(temp_result * scaling_factor)

    return final_score

# Input data
assessments = [
    {'id': 101, 'type': 'technical', 'value': 80},
    {'id': 102, 'type': 'technical', 'value': 70},
    {'id': 103, 'type': 'technical', 'value': 85},
    {'id': 104, 'type': 'technical', 'value': 78},
    {'id': 105, 'type': 'behavioral', 'value': 55},
    {'id': 106, 'type': 'behavioral', 'value': 65},
    {'id': 107, 'type': 'technical', 'value': 72}
]

# Execute
final_score = evaluate_performance(assessments)
print(f'Result: {final_score}')