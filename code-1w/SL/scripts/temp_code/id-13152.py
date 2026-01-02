def analyze_performance(records):
    base_multiplier = 1.5
    adjustment_factor = 0.8
    temp_results = []
    cumulative_offset = 0

    for i, record in enumerate(records):
        raw_value = len(record['name']) * base_multiplier
        if i % 2 == 0:
            raw_value += adjustment_factor * 2
        else:
            raw_value -= adjustment_factor

        # Irrelevant string processing (distractor)
        formatted_name = record['name'].upper().replace('A', 'X')
        char_count = sum(1 for c in formatted_name if c.isalpha())

        normalized = raw_value / (record['level'] + 1)
        temp_results.append(normalized)

        # Dead code path (distractor)
        if len(formatted_name) > 100:
            cumulative_offset += 999

    return temp_results


def calculate_ranking(points_list, penalty_log):
    ranking_weights = [0.9, 1.1, 1.0, 0.8]
    total_points = sum(points_list)
    applied_corrections = []

    for idx, (pt, w) in enumerate(zip(points_list, ranking_weights)):
        corrected = pt * w
        if idx in penalty_log:
            corrected -= 0.5
        applied_corrections.append(corrected)

    # Use of enumerate and zip together (required feature)
    final_adjustment = 0
    for index, value in enumerate(applied_corrections):
        if index % 2 == 1:
            final_adjustment += value * 0.1

    # Auxiliary computation that doesn't affect result (distractor)
    outlier_check = [x for x in applied_corrections if x > 5]
    stability_metric = len(outlier_check) * 0.01

    return int(sum(applied_corrections) + final_adjustment)

# Main execution block
records_data = [
    {'name': 'AlphaTeam', 'level': 2},
    {'name': 'BravoSquad', 'level': 3},
    {'name': 'GammaUnit', 'level': 1},
    {'name': 'DeltaCell', 'level': 4}
]

penalty_indices = {1, 3}

# Step 1: Analyze performance to get intermediate points
intermediate_scores = analyze_performance(records_data)

# Step 2: Transform data using string method distractor
hashed_keys = [r['name'].split('a')[0].lower() for r in records_data]
dummy_map = {k: i for i, k in enumerate(hashed_keys)}

# Step 3: Calculate final score (key statement)
final_score = calculate_ranking(intermediate_scores, penalty_indices)

print(f"Target result: {final_score}")