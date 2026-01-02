def process_results(records, threshold):
    # Irrelevant helper: computes average but not used in final logic
    avg_lambda = lambda data: sum(data) / len(data) if data else 0
    all_averages = [avg_lambda(list(record.values())) for record in records]

    # Distractor: complex filtering that doesn't impact final result
    valid_keys = set()
    for record in records:
        for k, v in record.items():
            if v > threshold * 0.8:
                valid_keys.add(k)

    # Real logic begins: count how many passed in core subjects
    core_subjects = ['math', 'physics']
    passed_count = 0
    bonus_awarded = False

    for record in records:
        # Check if student passed both core subjects
        core_scores = [record.get(subj, 0) for subj in core_subjects]
        if all(score >= threshold for score in core_scores):
            passed_count += 1

        # Bonus condition: hidden rule (only one student with art > 95)
        if record.get('art', 0) > 95:
            bonus_awarded = True  # Only first qualifying record matters
            break  # Early exit: short-circuit evaluation pattern

    # Intermediate irrelevant computation
    phantom_score = sum([len(r) * 2 for r in records if len(r) > 3]) // (len(records) or 1)

    # Final scoring logic
    base_score = passed_count * 25
    extra_bonus = 15 if bonus_awarded else 0
    adjustment = len(valid_keys) - len(core_subjects)  # Minor tweak based on earlier set

    final_score = base_score + extra_bonus + adjustment

    # Dead code path - never executed due to logic above
    if len(all_averages) > 100:
        final_score *= 2

    return final_score

# Input data
assessments = [
    {'math': 88, 'physics': 92, 'chemistry': 76, 'art': 64},
    {'math': 95, 'physics': 85, 'biology': 88, 'art': 96},  # This one triggers art > 95
    {'math': 70, 'physics': 65, 'history': 80, 'art': 77}
]
passing_threshold = 85

# Execution point of interest
final_score = process_results(assessments, passing_threshold)
print(f"Result: {final_score}")