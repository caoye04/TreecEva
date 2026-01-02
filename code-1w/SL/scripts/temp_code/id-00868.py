def calculate_rating(contribs, penalties):
    base_score = sum([v * 1.5 for v in contribs.values() if v > 2])
    adjustment = 0
    
    # Irrelevant tracking variables (distractors)
    total_entries = len(contribs)
    outlier_count = 0
    temp_buffer = []
    
    for key, value in contribs.items():
        if value < 1:
            outlier_count += 1
            temp_buffer.append(key)

    # Real logic: apply penalties from map only for high contributors
    filtered_keys = [k for k in contribs.keys() if contribs[k] >= 3]
    penalty_sum = 0
    for k in filtered_keys:
        if k in penalties:
            penalty_sum += penalties[k]

    # Misleading intermediate calculation (not used)
    hypothetical_max = len(filtered_keys) * 10
    scaling_factor = 1.0 if hypothetical_max == 0 else base_score / hypothetical_max

    # Actual score computation
    raw_score = base_score - penalty_sum
    
    # Conditional expression (required feature)
    final_score = raw_score if raw_score > 0 else 0.0
    
    # Slicing operation on sorted keys (required feature)
    sorted_contribs = sorted(contribs.keys())
    recent_focus = sorted_contribs[-3:]  # Last three alphabetically

    # Dictionary-based weight mapping (required feature)
    weights = {k: 1.2 for k in recent_focus}
    boost = sum(weights.values()) * 0.1  # Minor irrelevant addition

    # Dead code path (distractor)
    if len(temp_buffer) > 100:
        adjustment += 5

    return int(final_score + boost)  # Final cast to integer

# Main data setup
contributions = {
    'analysis': 4,
    'testing': 5,
    'design': 3,
    'docs': 1,
    'planning': 6,
    'review': 2
}

penalty_map = {
    'analysis': 2,
    'planning': 4,
    'design': 1
}

# Key execution point
final_score = calculate_rating(contributions, penalty_map)

# Output result as required
print(f"Result: {final_score}")