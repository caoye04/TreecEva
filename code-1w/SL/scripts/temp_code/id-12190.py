def calculate_final_score(performances, multiplier):
    # Normalize performance scores using min-max scaling
    min_perf = min(performances)
    max_perf = max(performances)
    range_perf = max_perf - min_perf if max_perf != min_perf else 1
    normalized = [(p - min_perf) / range_perf for p in performances]

    # Apply multiplier and round to 2 decimal places
    adjusted = [round(score * multiplier, 2) for score in normalized]

    # Boost top performers using lambda-based thresholding
    is_high_performer = lambda x: x >= 0.75
    boosted = [score * 1.2 if is_high_performer(score) else score for score in adjusted]

    # Aggregate final score using weighted average (recent entries weighted more)
    weights = [i + 1 for i in range(len(boosted))]
    weighted_sum = sum(score * weight for score, weight in zip(boosted, weights))
    total_weight = sum(weights)
    aggregate = weighted_sum / total_weight if total_weight != 0 else 0

    # Irrelevant distractor: process duplicate indices (not used in result)
    unique_scores = set(adjusted)
    duplicate_check = [x for x in adjusted if adjusted.count(x) > 1]
    suppression_factor = len(duplicate_check) * 0.01  # Unused distraction

    # More distraction: sorting with no impact
    sorted_weakly = sorted(boosted, reverse=False)
    temp_result = sum(sorted_weakly[::2])  # Partial slice sum - unused

    # Final transformation
    return round(aggregate * 100, 2)

# Main execution
rankings = [88, 54, 72, 91, 67, 83]
adjustment_factor = 2.5
baseline_offset = 17.3  # Distractor variable
intermediate_avg = sum(rankings) / len(rankings)  # Unused computation
filtered_ranks = [r for r in rankings if r > 60]  # Not used later
size_indicator = len(filtered_ranks) * 2  # Dead code path

# Key statement
final_score = calculate_final_score(rankings, adjustment_factor)
print(f"Result: {final_score}")