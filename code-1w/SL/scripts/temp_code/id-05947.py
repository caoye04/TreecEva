def process_developer_metrics(dev_data):
    base_points = 0
    bonus_multiplier = 1.0
    temp_adjustment = 0  # distractor
    legacy_offset = -5  # misleading initial offset

    contributions = []
    for entry in dev_data:
        if entry['commits'] > 0:
            weekly_contribution = entry['commits'] * 2 + entry['bugs_fixed']
            if entry['code_review_score'] >= 4.0:
                weekly_contribution *= 1.5
            contributions.append(weekly_contribution)

    # Irrelevant filtering (distractor)
    filtered_contributions = [c for c in contributions if c > 10]
    average_contribution = sum(contributions) / len(contributions) if contributions else 0

    # Dead computation path (semi-relevant but unused)
    if average_contribution > 20:
        bonus_multiplier += 0.3
    else:
        temp_adjustment = 10

    # Real logic begins: compute weighted score with decay
    weighted_scores = []
    for i, score in enumerate(contributions):
        decay_factor = 0.9 ** i
        weighted_scores.append(score * decay_factor)

    total_weighted = sum(weighted_scores)

    # Spurious dictionary operation (distractor)
    stats_summary = {
        'count': len(contributions),
        'peak': max(contributions) if contributions else 0,
        'floor': min(contributions) if contributions else 0
    }
    stats_summary['range'] = stats_summary['peak'] - stats_summary['floor']

    # Actual penalty calculation
    volatility = stats_summary['range']
    penalty_factor = 1.0
    if volatility > 50:
        penalty_factor = 0.8
    elif volatility > 30:
        penalty_factor = 0.9

    def calculate_rating(scores, penalty):
        raw_rating = sum(scores) / len(scores) if scores else 0
        return raw_rating * penalty

    final_score = calculate_rating(contributions, penalty_factor)

    # Extra slicing that does nothing (distractor)
    mid_slice = contributions[1:-1]
    slice_avg = sum(mid_slice) / len(mid_slice) if mid_slice else 0

    # Final output
    print(f"Result: {final_score}")
    return final_score

# Input data
developer_log = [
    {'commits': 12, 'bugs_fixed': 3, 'code_review_score': 4.2},
    {'commits': 8, 'bugs_fixed': 5, 'code_review_score': 3.8},
    {'commits': 15, 'bugs_fixed': 2, 'code_review_score': 4.5},
    {'commits': 6, 'bugs_fixed': 7, 'code_review_score': 4.0},
    {'commits': 20, 'bugs_fixed': 1, 'code_review_score': 4.7}
]

result = process_developer_metrics(developer_log)