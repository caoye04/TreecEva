def process_ratings(data, importance):
    base_score = 0
    adjustment_factor = 0.0
    temp_sum = 0  # irrelevant accumulator
    temp_count = 0  # misleading counter

    for category, entries in data.items():
        category_total = sum(entries)
        category_len = len(entries)
        if category_len == 0:
            continue
        category_avg = category_total / category_len

        # Irrelevant statistical distraction
        squared_diffs = [(x - category_avg) ** 2 for x in entries]
        variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
        std_deviation = variance ** 0.5  # unused but plausible calculation

        weight = importance.get(category, 1.0)
        contribution = category_avg * weight
        base_score += contribution

        # Dead code path (never reached due to logic above)
        if False and variance > 100:
            adjustment_factor += 0.1

    # Additional distraction: lambda-based filtering (not actually used)
    outlier_filter = lambda x: x > 3.0 and x < 9.0
    filtered_data = [v for v in data.get('performance', []) if outlier_filter(v)]
    dummy_metric = len(filtered_data) * 0.1 if filtered_data else 0  # semi-relevant but unused

    # Real computation path
    multiplier = len(data) * 0.5
    final_score = base_score * multiplier

    # Slicing distraction on string representation of numbers
    str_scores = ''.join([str(int(s)) for s in data.get('performance', [0])])
    shadow_value = int(str_scores[1:]) if len(str_scores) > 1 else 0  # irrelevant

    return final_score

# Main execution
user_data = {
    'performance': [8, 7, 9, 6],
    'behavior': [5, 6, 5],
    'innovation': [9, 8, 10, 7, 8]
}

weights = {
    'performance': 1.2,
    'behavior': 0.8,
    'innovation': 1.5
}

interim_result = 0
for k in user_data:
    interim_result += len(user_data[k])

final_score = process_ratings(user_data, weights)
print(f"Result: {final_score}")