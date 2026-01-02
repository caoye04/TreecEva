def calculate_final_score(data, thresholds):
    # Irrelevant pre-processing: normalize names (not used in scoring)
    normalized_names = [name.strip().lower().title() for name in data.get('participants', [])]
    
    # Extract relevant metrics
    performance_log = data.get('performance', [])
    base_scores = [entry['score'] for entry in performance_log if entry['active']]
    
    # Misleading computation: average with no impact
    total_sum = sum(base_scores)
    average_score = total_sum / len(base_scores) if base_scores else 0
    adjusted_avg = average_score * 1.1  # Distractor adjustment

    # Threshold filtering - actual logic starts here
    passing_scores = []
    for s in base_scores:
        if s >= thresholds['min_passing']:
            if s <= thresholds['max_outlier']:
                passing_scores.append(s)
            else:
                # Apply cap instead of excluding completely
                passing_scores.append(thresholds['max_outlier'])

    # Bonus logic based on count (hidden rule)
    bonus = 0
    if len(passing_scores) > 4:
        bonus = 5
    elif len(passing_scores) == 3:
        bonus = 2

    # Aggregate score using min, max, and bonus
    if not passing_scores:
        aggregate = 0
    else:
        aggregate = (min(passing_scores) + max(passing_scores)) / 2
    
    # Final composition
    raw_final = aggregate + bonus
    
    # Red herring: unused transformation
    scaled_final = round(raw_final * 1.05, 2)
    validation_checksum = sum([len(str(x)) for x in thresholds.values()])

    final_score = int(raw_final)  # This is the actual output
    return final_score

# Input data structure
experiment_data = {
    'participants': [' alice ', 'BOB', 'Charlie ', 'Diana'],
    'performance': [
        {'score': 65, 'active': True},
        {'score': 70, 'active': True},
        {'score': 58, 'active': False},  # inactive
        {'score': 80, 'active': True},
        {'score': 95, 'active': True},
        {'score': 45, 'active': True},
        {'score': 77, 'active': True}
    ]
}

thresholds_config = {
    'min_passing': 60,
    'max_outlier': 90,
    'buffer_zone': 5,
    'scale_factor': 1.5
}

# Execution point
final_score = calculate_final_score(experiment_data, thresholds_config)
print(f"Result: {final_score}")