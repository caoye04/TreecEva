def calculate_final_score(records, penalties):
    base_scores = {k: len(v) for k, v in records.items()}
    
    # Irrelevant distraction: counting total characters in keys (not used in final logic)
    total_key_length = sum(len(key) for key in records.keys())
    
    adjusted_scores = {}
    for key, values in records.items():
        unique_count = len(set(values))
        if unique_count > 2:
            adjusted_scores[key] = base_scores[key] * 1.5
        else:
            adjusted_scores[key] = base_scores[key]
    
    raw_total = sum(adjusted_scores.values())
    
    deduction = 0
    for category, penalty in penalties.items():
        if category in records and len(records[category]) > 0:
            deduction += penalty

    result = raw_total - deduction
    return int(result)

# Main data
sample_data = {
    'event_A': [101, 102, 103, 101],
    'event_B': [205, 206],
    'event_C': [301, 302, 303, 304, 305]
}

penalty_chart = {
    'event_A': 5,
    'event_B': 3,
    'event_X': 10  # Irrelevant penalty (event_X not in data)
}

# Computation entry point
final_score = calculate_final_score(sample_data, penalty_chart)
print(f"Result: {final_score}")