def calculate_final_score(data, limits):
    temp_result = 0
    base_offset = len(data) * 0.5
    adjustment_factor = 0.0

    # Irrelevant string processing (distractor)
    status_labels = ['valid', 'processed', 'approved']
    label_check = [label.upper() for label in status_labels if 'a' in label]
    dummy_str_op = ''.join(label_check).lower().replace('a', 'X')

    # Real logic begins: filtering and scoring
    valid_entries = [x for x in data if isinstance(x, int) and x > 0]
    filtered_scores = set()
    for val in valid_entries:
        if val > limits['high']:
            filtered_scores.add(val * 1.1)
        elif val > limits['medium']:
            filtered_scores.add(val * 1.3)
        else:
            filtered_scores.add(val * 1.5)

    # Secondary loop with conditional expression (relevant)
    bonus_points = 0
    for score in filtered_scores:
        bonus_points += 10 if score > 150 else 5

    # Use of tuple unpacking (semi-relevant, tracks state)
    (count_high, count_low) = (sum(1 for s in filtered_scores if s >= 150), sum(1 for s in filtered_scores if s < 150))
    
    # Dead code path (distractor)
    if base_offset > 100:
        adjustment_factor = 0.2
    elif base_offset < 0:
        adjustment_factor = -0.1
    else:
        adjustment_factor = 0.0  # Never used meaningfully

    # Core calculation
    raw_total = sum(filtered_scores)
    temp_result = raw_total + bonus_points + (count_high * 7)

    # Final adjustment using conditional expression
    final_modifier = 1.05 if count_high > count_low else 1.0
    return int(temp_result * final_modifier)

# Input setup
data_set = [20, -5, 40, 'ignore', 60, 80, 0, 100, 120]
thresholds = {'low': 30, 'medium': 60, 'high': 90}

# Execution point
final_score = calculate_final_score(data_set, thresholds)
print(f"Result: {final_score}")