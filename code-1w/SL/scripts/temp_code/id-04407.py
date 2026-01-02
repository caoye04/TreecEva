from itertools import groupby

# Simulate user feedback analysis for a coding education platform
def analyze_feedback_complex(users):
    raw_scores = []
    temp_aggregates = []
    noise_counter = 0  # Distractor: tracks irrelevant metric

    for user in users:
        session_data = user['sessions']
        consistency_bonus = 0
        total_submissions = 0
        failed_attempts = 0

        # Process each user's coding session history
        for session in session_data:
            total_submissions += session['attempts']
            if session['success']:
                failed_attempts += max(0, session['attempts'] - 1)

        # Compute basic performance ratio
        success_ratio = (total_submissions - failed_attempts) / total_submissions if total_submissions else 0

        # Apply conditional bonus logic
        if success_ratio > 0.7:
            consistency_bonus = 10
        elif success_ratio > 0.5:
            consistency_bonus = 5

        # Base score with bonus
        base_score = success_ratio * 100 + consistency_bonus
        raw_scores.append(base_score)

        # Distractor computation: simulate noise tracking
        for _ in range(int(base_score % 3)):
            noise_counter += 1  # Irrelevant accumulation

        temp_aggregates.append(noise_counter * 0.1)  # Semi-relevant but unused later

    # Sort and group scores by integer part (simulating cohort analysis)
    raw_scores.sort()
    grouped = groupby(raw_scores, key=lambda x: int(x))
    grouped_counts = {k: len(list(g)) for k, g in grouped}

    # Secondary distractor: analyze distribution skew
    skew_metric = 0
    for k, count in grouped_counts.items():
        if count > 1:
            skew_metric += k * 0.05

    # Final transformation using lambda to filter and scale
    filtered_scores = list(filter(lambda x: x >= 60 or x < 40, raw_scores))
    adjusted_scores = [s + skew_metric for s in filtered_scores]

    # Critical result computation
    final_score = sum(adjusted_scores) / len(adjusted_scores) if adjusted_scores else 0

    return final_score

# Generate synthetic input data
feedback_list = [
    {
        'user_id': f'U{i}',
        'sessions': [
            {'attempts': 3 + (i*j) % 5, 'success': (i*j) % 4 != 0} for j in range(1, 4)
        ]
    } for i in range(1, 8)
]

# Add auxiliary distractor structure
aux_data = [{'meta': x % 2, 'flag': False} for x in range(len(feedback_list)*2)]
duplicate_filter = lambda x: x['meta'] == 1
count_filtered = len(list(filter(duplicate_filter, aux_data)))

# Execute main logic
temp_result = analyze_feedback_complex(feedback_list)
final_score = temp_result + (count_filtered * 0.01)  # Minor adjustment from distractor

print(f"Result: {final_score}")