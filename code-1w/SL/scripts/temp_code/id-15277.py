def analyze_performance(logs, importance_weights):
    total_entries = len(logs)
    cumulative = 0
    adjustments = 0
    temp_buffer = []

    # Preprocess: normalize weights (irrelevant to final result but adds distraction)
    weight_sum = sum(importance_weights)
    normalized_weights = [w / weight_sum for w in importance_weights]

    # Secondary metric tracking (distractor computation)
    outlier_count = 0
    for entry in logs:
        if entry[1] > 90:
            outlier_count += 1

    # Core logic: weighted score based on feedback categories
    category_tally = {'usability': [], 'performance': [], 'design': []}
    for idx, (category, score) in enumerate(logs):
        if category in category_tally:
            category_tally[category].append(score * importance_weights[idx % len(importance_weights)])

    # Misleading aggregation path (dead-end calculation)
    avg_by_category = {}
    for cat, scores in category_tally.items():
        if scores:
            avg_by_category[cat] = sum(scores) / len(scores)
            adjustments += len(scores) * 0.1  # Minor adjustment (not used later)

    # Actual key computation path
    flat_scores = []
    for i, (cat, score) in enumerate(logs):
        weight = importance_weights[i % len(importance_weights)]
        weighted_score = score * weight
        flat_scores.append(weighted_score)

    # Use of zip and enumerate (required Python features)
    for i, (orig, weighted) in enumerate(zip(logs, flat_scores)):
        temp_buffer.append((i, orig[0], weighted))

    # Final aggregation
    raw_total = sum(flat_scores)
    divisor = len(flat_scores) if flat_scores else 1
    final_score = raw_total / divisor

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_logs = [
    ('usability', 85),
    ('performance', 78),
    ('design', 92),
    ('performance', 81),
    ('usability', 88),
    ('design', 84)
]
weights = [0.4, 0.6, 0.5]

# Execution point
final_score = analyze_performance(feedback_logs, weights)