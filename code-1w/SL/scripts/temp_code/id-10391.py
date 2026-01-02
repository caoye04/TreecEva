def analyze_feedback(survey_data):
    feedback_set = set()
    temp_stats = []
    outlier_count = 0

    for idx, entry in enumerate(survey_data):
        if len(entry['comments']) > 50:
            feedback_set.add('detailed')
        elif 'bug' in entry['comments']:
            feedback_set.add('technical')

        rating = entry['rating']
        if rating < 2:
            outlier_count += 1
            if outlier_count > 1:
                temp_stats.append(rating * 1.5)
        else:
            temp_stats.append(rating)

    if len(feedback_set) == 0:
        feedback_set.add('neutral')

    return feedback_set, temp_stats


def compute_trend(values):
    trend = 0
    for i in range(1, len(values)):
        trend += values[i] - values[i-1]
    return abs(trend)


def evaluate_performance(tags, scores):
    base_score = sum(scores) % 100
    multiplier = 1

    if 'detailed' in tags:
        multiplier += 0.5
    if 'technical' in tags:
        multiplier += 0.3

    adjustment = 0
    for s in scores:
        if s > 4:
            adjustment += s / 4

    # Distractor: unused calculation
    noise = 0
    for a, b in zip(scores, scores[1:]):
        noise += (a - b) ** 2

    final_score = int((base_score * multiplier) + adjustment)
    return final_score

# Simulated input data
survey_input = [
    {'rating': 5, 'comments': 'Great product with excellent features'},
    {'rating': 1, 'comments': 'Found a critical bug in setup'},
    {'rating': 4, 'comments': 'Good, but needs better documentation'},
    {'rating': 5, 'comments': 'Outstanding experience so far'}
]

# Core processing steps
feedback_tags, rating_list = analyze_feedback(survey_input)
smoothed_ratings = [r for r in rating_list if r >= 2]
if len(smoothed_ratings) == 0:
    smoothed_ratings = [3]

# Compute trend (unused distractor)
trend_value = compute_trend(rating_list)

# Key statement
final_score = evaluate_performance(feedback_tags, rating_list)
print(f"Result: {final_score}")