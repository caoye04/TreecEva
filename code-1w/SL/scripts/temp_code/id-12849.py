def evaluate_performance(log_entries, standard):
    base_score = 0
    penalty_adjustment = 0
    temp_flags = []
    
    # Process each log entry for compliance and accuracy
    for entry in log_entries:
        if 'error' in entry['type']:
            penalty_adjustment -= 1
        elif 'warning' in entry['type']:
            temp_flags.append(entry['code'])
        else:
            base_score += entry['value']

    # Irrelevant string processing - distractor
    formatted_codes = [f"CHK-{code:03d}" for code in temp_flags]
    status_summary = "; ".join(formatted_codes).upper()
    summary_length = len(status_summary)

    # Bitwise validation against benchmark (relevant)
    valid_bits = 0
    for val in standard:
        if val & 1 == 1:  # count odd numbers as valid bits
            valid_bits += 1

    # Set operation to filter redundant flags (semi-relevant)
    unique_flags = len(set(temp_flags))

    # Final scoring logic - only base_score and valid_bits matter
    stability_factor = 1 if unique_flags > 2 else 0.8
    final_score = int((base_score + valid_bits) * stability_factor)

    # Dead code path - misleading
    if summary_length > 100:
        final_score += 10  # never reached

    return final_score


# Input data
assessment_log = [
    {'type': 'info', 'value': 15, 'code': 101},
    {'type': 'warning', 'value': 0, 'code': 205},
    {'type': 'info', 'value': 8, 'code': 102},
    {'type': 'error', 'value': -5, 'code': 999},
    {'type': 'info', 'value': 12, 'code': 103},
    {'type': 'warning', 'value': 0, 'code': 205},
    {'type': 'info', 'value': 7, 'code': 104}
]

benchmark_set = [3, 8, 12, 15, 21, 22, 27]

# Execution point
final_score = evaluate_performance(assessment_log, benchmark_set)
print(f"Result: {final_score}")