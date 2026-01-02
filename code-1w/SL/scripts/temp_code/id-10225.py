def evaluate_performance(log, thresh):
    # Irrelevant preprocessing: reverse and slice (distractor)
    reversed_log = log[::-1]
    sliced_log = [x for x in reversed_log if x > 0.5]  # Not used later

    # Relevant transformation: normalize values
    normalized = [round(x / sum(log), 4) for x in log]

    # State tracking with conditional logic
    above_threshold = 0
    cumulative_deviation = 0.0
    for val in normalized:
        if val >= thresh:
            above_threshold += 1
        deviation = abs(val - thresh)
        cumulative_deviation += deviation

    # Secondary loop for counting consecutive high performers (semi-relevant)
    consecutive_high = 0
    max_consecutive = 0
    for val in log:
        if val > 0.75:
            consecutive_high += 1
        else:
            if consecutive_high > max_consecutive:
                max_consecutive = consecutive_high
            consecutive_high = 0
    if consecutive_high > max_consecutive:
        max_consecutive = consecutive_high

    # Final score computation – only this matters
    base_score = above_threshold * 100
    penalty = int(cumulative_deviation * 50)
    bonus = max_consecutive * 10
    final_score = base_score - penalty + bonus  # Key assignment

    # Dead code path (distractor)
    if final_score < 0:
        final_score = 0
    elif final_score > 1000:
        temp = final_score // 2  # Unused variable
        final_score = 999

    return final_score

# Main execution
accuracy_log = [0.82, 0.91, 0.67, 0.88, 0.73, 0.90, 0.65]
threshold = 0.75

# Misleading auxiliary calculation
average_accuracy = sum(accuracy_log) / len(accuracy_log)
scaled_avg = round(average_accuracy * 100, 2)
dummy_list = [i**2 for i in range(len(accuracy_log))]  # Unused list comprehension

final_score = evaluate_performance(accuracy_log, threshold)
print(f"Result: {final_score}")