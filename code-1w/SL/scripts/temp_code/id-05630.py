def analyze_performance(records):
    base_offset = 17
    temp_results = []
    for i, record in enumerate(records):
        if len(record) < 3:
            continue
        raw_score = record[1] * 2.5 + base_offset
        adjustment = (record[2] ** 2) % 4
        adjusted = raw_score - adjustment
        temp_results.append(adjusted)

    # Irrelevant aggregation
    total_sum = sum(temp_results)
    avg_temp = total_sum / len(temp_results) if temp_results else 0
    outlier_count = sum(1 for x in temp_results if abs(x - avg_temp) > 15)

    return temp_results


def filter_eligible(candidates, thresholds):
    valid_entries = []
    for idx, (score, tier) in enumerate(zip(candidates, thresholds)):
        if tier < 1 or score <= 0:
            continue
        normalized = score / (tier + 1)
        bonus = 5 if normalized > 8 else 0
        capped = min(normalized + bonus, 20)
        valid_entries.append(capped)

    # Dead code path - never used
    if len(valid_entries) > 100:
        scaling_factor = 0.95
        valid_entries = [x * scaling_factor for x in valid_entries]

    return valid_entries


def calculate_weights(values):
    weights = []
    for v in values:
        w = (v ** 0.5) * 3.1
        noise = (v % 7) * 0.01
        weights.append(w + noise)
    return weights


def compute_ranking(points_list, penalty_log):
    cumulative = 0
    weighted_points = calculate_weights(points_list)

    # Distractor: irrelevant transformation
    transformed = [abs(x - 10) ** 1.1 for x in points_list if x != 5]
    shadow_total = sum(transformed) % 1000

    for i, pt in enumerate(weighted_points):
        if i >= len(penalty_log):
            break
        penalty = penalty_log[i] * 1.8
        effect = pt - penalty
        if effect < 0:
            effect = effect * 0.5  # partial carryover
        cumulative += effect

        # Early exit red herring
        if cumulative > 500:
            cumulative = 500
            break

    # Key logic step: apply final modifier based on parity and size
    modifier = -2 if int(cumulative) % 2 == 0 else 3
    final_adjustment = cumulative + modifier

    # Decoy assignment
    dummy_result = [final_adjustment * 0.1 for _ in range(5)]

    return int(final_adjustment)

# Main execution flow
raw_data = [
    [1, 12, 3],
    [2, 15, 1],
    [3, 8, 2],
    [4, 20, 0],
    [5, 10, 4]
]

scores = analyze_performance(raw_data)

thresholds = [2, 1, 3, 0, 2]
eligible_scores = filter_eligible(scores, thresholds)

penalties = [2, 1, 4, 0, 3]

final_score = compute_ranking(eligible_scores, penalties)

# Output result
print(f"Result: {final_score}")