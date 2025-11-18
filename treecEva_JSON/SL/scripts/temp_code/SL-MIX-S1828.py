import statistics

def calculate_iqr_outliers(data):
    sorted_data = sorted(data)
    q1 = statistics.median(sorted_data[:len(sorted_data)//2])
    q3 = statistics.median(sorted_data[len(sorted_data)//2:])
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

feature_ratings = {
    'ui_design': [8, 9, 7, 10, 6, 8, 9, 2, 8, 9],
    'performance': [7, 8, 6, 9, 7, 8, 10, 7, 8, 7],
    'security': [9, 10, 8, 9, 9, 10, 8, 9, 1, 9]
}

filtered_features = {k: calculate_iqr_outliers(v) for k, v in feature_ratings.items()}
feature_variances = {k: statistics.variance(v) for k, v in filtered_features.items() if len(v) > 1}
lowest_variance_feature = min(feature_variances, key=feature_variances.get)
consistency_scores = {k: len(v) * (1 / feature_variances[k]) for k, v in filtered_features.items() if k in feature_variances}
sorted_scores = dict(sorted(consistency_scores.items(), key=lambda item: item[1], reverse=True))
ranked_features = list(sorted_scores.keys())
final_consistency_score = int(sorted_scores[lowest_variance_feature]) if lowest_variance_feature in sorted_scores else 0
print(f'Result: {final_consistency_score}')