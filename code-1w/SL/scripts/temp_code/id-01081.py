def preprocess_data(raw):
    # Irrelevant transformation (distractor)
    cleaned = [x * 0.95 for x in raw if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    return normalized

def calculate_entropy(values):
    # Semi-relevant calculation (not used in final answer)
    import math
    entropy = 0.0
    total = sum(values)
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

def calculate_final_score(records, importance):
    # Core logic begins
    totals = {}
    for key in records:
        category_sum = 0
        for val in records[key]:
            category_sum += val * importance.get(key, 1.0)
        totals[key] = category_sum

    # Intermediate aggregation (some distraction)
    temp_offsets = {k: len(v) * 0.1 for k, v in records.items()}
    adjusted = {k: totals[k] + temp_offsets[k] for k in totals}

    # Key computation step
    base_score = sum(totals.values())
    penalty = 0
    for k, v in totals.items():
        if v < 5:
            penalty += 2
    
    # Final score with distractor influence removed
    final_score = int(base_score - penalty)  # Only this matters

    # Dead code branch (distractor)
    if False:
        backup = sum(adjusted.values())
        final_score = int(backup)

    return final_score

# Main execution
raw_input = [10, -5, 15, 0, 20]
dummy_processed = preprocess_data(raw_input)

# Real input data structure
student_data = {
    'math': [8, 7, 9],
    'science': [6, 6],
    'literature': [5, 4, 5, 6],
    'history': [7]
}

weights = {
    'math': 1.5,
    'science': 1.3,
    'literature': 1.0,
    'history': 1.1
}

# Additional irrelevant dictionary operations (distractors)
stats = {
    'count': sum(len(v) for v in student_data.values()),
    'max_len': max(len(v) for v in student_data.values()),
    'range_check': max(max(v) for v in student_data.values()) - min(min(v) for v in student_data.values())
}

entropy_value = calculate_entropy([len(v) for v in student_data.values()])  # Unused

final_score = calculate_final_score(student_data, weights)

print(f"Result: {final_score}")