def analyze_performance(records):
    base_multiplier = 1.5
    bonus_threshold = 85
    penalty_factor = 0.9
    temp_adjustment = 0
    total_points = 0
    valid_entries = 0
    outlier_count = 0

    # Irrelevant statistical tracking
    mean_placeholder = 0
    variance_proxy = 0
    running_squares = 0

    for record in records:
        raw_score = record['score']
        if raw_score < 0:
            outlier_count += 1
            continue
        if raw_score > bonus_threshold:
            temp_adjustment += 2.5
        else:
            temp_adjustment -= 0.5

        total_points += raw_score
        valid_entries += 1

        # Dead computation - not used later
        running_squares += raw_score * raw_score

    if valid_entries > 0:
        mean_placeholder = total_points / valid_entries
        variance_proxy = (running_squares / valid_entries) - (mean_placeholder ** 2)

    efficiency_ratio = (total_points / (valid_entries or 1)) * base_multiplier
    return efficiency_ratio, temp_adjustment

# Unused helper function (distractor)
def validate_input(data):
    return all('id' in item and 'score' in item for item in data)

rank = [1, 2, 3, 4]
points_log = [
    {'id': 101, 'score': 90},
    {'id': 102, 'score': 78},
    {'id': 103, 'score': 95},
    {'id': 104, 'score': 67},
    {'id': 105, 'score': -1},  # invalid
]

# Auxiliary transformation using lambda
transform = lambda x: [i * 1.1 for i in x if i % 2 == 1]
corrected_ranks = transform(rank)

# Secondary analysis with red herring variables
baseline, adjustment = analyze_performance(points_log)

# Simulate weighting factors (some irrelevant)
dynamic_weights = [1.0, 0.8, 1.2, 0.9]
weight_influence = sum([w * 0.1 for w in dynamic_weights])  # unused

# Core logic embedded among distractions
aggregate = sum(point['score'] for point in points_log if point['score'] > 0)
penalty_applied = aggregate * 0.95 if len(points_log) - len([p for p in points_log if p['score'] < 0]) > 3 else aggregate

scaling_factor = len(corrected_ranks) * 1.5
interim_result = penalty_applied * scaling_factor * (baseline / 100)

# Final calculation
compute_bonus = lambda x, y: x + y * 2
projected = compute_bonus(interim_result, adjustment)

final_score = int(projected // 3)  # key statement
print(f"Result: {final_score}")