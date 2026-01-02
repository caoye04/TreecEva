def evaluate_performance(records):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    internal_sum = 0
    temp_result = 0
    final_score = 0

    # Irrelevant string processing - distractor
    status_labels = ['pass', 'fail', 'review', 'pending']
    formatted_statuses = [label.upper().replace('E', '3') for label in status_labels]
    dummy_concat = ''.join(formatted_statuses)
    hash_value = len(dummy_concat) * 3.14

    # Actual logic begins: process assessment scores
    valid_scores = []
    for record in records:
        score_str = record.get('score', '0')
        if isinstance(score_str, str) and score_str.isdigit():
            numeric_score = int(score_str)
            if numeric_score >= 0 and numeric_score <= 100:
                valid_scores.append(numeric_score)

    # Sorting relevant data - meaningful operation
    valid_scores.sort(reverse=True)

    # Apply top-weighting logic
    weighted_sum = 0.0
    decay_factor = 1.0
    for i, s in enumerate(valid_scores):
        if i % 5 == 0 and i != 0:
            decay_factor *= 0.8
        weighted_sum += s * decay_factor
        decay_factor = max(decay_factor, 0.6)  # prevent decay below 0.6

    # Bonus application logic
    above_threshold = [v for v in valid_scores if v >= bonus_threshold]
    bonus_awarded = len(above_threshold) >= 3

    # Secondary irrelevant computation - red herring
    placeholder_array = [0] * 10
    for idx in range(len(placeholder_array)):
        placeholder_array[idx] = (idx * 2 + 1) * 0.5
    aggregate_noise = sum(x for x in placeholder_array if x > 3)

    # Final calculation using correct path
    base_score = weighted_sum / len(valid_scores) if valid_scores else 0
    if bonus_awarded:
        base_score *= base_multiplier
    else:
        base_score *= penalty_factor

    # More distractions: unused intermediate variables
    outlier_count = sum(1 for v in valid_scores if v < 40)
    average_length = len(records) / 2 if records else 0
    temp_flag = False

    final_score = int(round(base_score))
    return final_score

# Input data setup
assessments = [
    {'id': 'A1', 'score': '92', 'type': 'math'},
    {'id': 'A2', 'score': '87', 'type': 'logic'},
    {'id': 'A3', 'score': '90', 'type': 'cs'},
    {'id': 'A4', 'score': 'invalid', 'type': 'eng'},
    {'id': 'A5', 'score': '89', 'type': 'puzz'},
    {'id': 'A6', 'score': '78', 'type': 'arith'},
    {'id': 'A7', 'score': '95', 'type': 'meta'},
    {'id': 'A8', 'score': '86', 'type': 'func'}
]

final_score = evaluate_performance(assessments)
print(f"Result: {final_score}")