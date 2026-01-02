def analyze_employee_data(records):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    total_entries = len(records)
    aggregated_scores = []
    temp_offsets = [0] * total_entries

    for i, record in enumerate(records):
        name = record['name']
        productivity = record['productivity']
        errors = record['errors']
        attendance = record['attendance']
        
        # Irrelevant string processing (distractor)
        name_clean = name.strip().lower()
        has_high_name_length = len(name_clean) > 7
        temp_offsets[i] = int(has_high_name_length) * 2
        
        # Real logic begins
        base_score = productivity * base_multiplier
        error_penalty = errors * 3.5
        attendance_bonus = 10 if attendance > 90 else 0
        
        # Dummy list comprehension with side effect (semi-relevant)
        adjusted_errors = [e for e in [errors] if e < 20]
        if adjusted_errors:
            base_score -= error_penalty
        
        # Nested condition with misleading short-circuit
        is_performer = (productivity > bonus_threshold) or (errors < 5 and False)
        if is_performer:
            base_score += attendance_bonus

        def evaluate_performance(p, e, a):
            score = p - (e * 4)
            if a >= 95:
                score *= 1.2
            elif a >= 80:
                score *= 1.1
            else:
                score *= 0.95
            return int(score)

        final_score = evaluate_performance(productivity, errors, attendance)
        
        # Dead code path (distractor)
        if False:
            final_score += sum(temp_offsets) // total_entries
            backup_log = f"Rechecking {name}..."
            print(backup_log)

        aggregated_scores.append(final_score)

    # Final aggregation not used — distractor
    avg_score = sum(aggregated_scores) / len(aggregated_scores)
    max_score = max(aggregated_scores)
    min_score = min(aggregated_scores)

    # But we only care about the last final_score
    return final_score

# Input data
employee_records = [
    {'name': 'Alice Johnson', 'productivity': 92, 'errors': 6, 'attendance': 88},
    {'name': 'Bob Smith', 'productivity': 78, 'errors': 12, 'attendance': 94},
    {'name': 'Charlie Lee', 'productivity': 96, 'errors': 4, 'attendance': 96}
]

result = analyze_employee_data(employee_records)
print(f"Target result: {result}")