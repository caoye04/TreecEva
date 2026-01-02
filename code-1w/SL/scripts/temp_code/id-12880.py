def evaluate_performance(feedback, multiplier):
    # Normalize feedback scores and apply weight
    normalized = {}
    total_weight = 0
    temp_sum = 0

    for key, score in feedback.items():
        if score < 0:
            adjusted = abs(score) * 0.5
        elif score > 8:
            adjusted = score * 1.2
        else:
            adjusted = score

        weight = len(key) % 3 + 1
        temp_sum += adjusted * weight
        total_weight += weight
        normalized[key] = adjusted

    if total_weight == 0:
        return 0

    weighted_avg = temp_sum / total_weight

    # Secondary processing: count high performers
    high_performers = 0
    for val in feedback.values():
        if val >= 9:
            high_performers += 1

    bonus = 0
    if high_performers >= 2:
        bonus = 5
    elif high_performers == 1:
        bonus = 2

    # Dummy tracking variables (distraction)
    review_count = len(feedback)
    max_possible = review_count * 10
    efficiency_ratio = (weighted_avg / 10.0) if max_possible > 0 else 0

    # Unused intermediate calculations (red herring)
    squared_deviation = 0
    for val in feedback.values():
        squared_deviation += (val - weighted_avg) ** 2

    # Final calculation with multiplier and bonus
    raw_result = weighted_avg * multiplier
    final_value = raw_result + bonus

    # This function call doesn't affect anything (dead path)
    def log_debug():
        print("Debug: No side effects")
    log_debug()  # Irrelevant function call

    return final_value

# Main execution
base_multiplier = 3
feedback_data = {
    "review_a": 7,
    "review_b": 9,
    "review_c": 6,
    "review_d": 10,
    "review_e": 4
}

intermediate_total = sum(len(k) for k in feedback_data.keys())
count_above_seven = sum(1 for v in feedback_data.values() if v > 7)  # distractor
auxiliary_flag = count_above_seven > 2  # misleading boolean

final_score = evaluate_performance(feedback_data, base_multiplier)
print(f"Result: {final_score}")