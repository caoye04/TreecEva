def evaluate_performance(feedback, threshold):
    # Simulate complex decision logic for performance rating
    high_count = len([x for x in feedback if x > threshold])
    low_count = len([x for x in feedback if x < threshold - 10])
    mid_count = len(feedback) - high_count - low_count

    # Distractor: irrelevant statistical measures
    mean_val = sum(feedback) / len(feedback) if feedback else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in feedback) / len(feedback) if feedback else 0
    peak_moment = max(feedback, default=0)
    decay_factor = 0.95

    # Complex conditional logic with nested expressions
    adjustment = 0
    if high_count >= 3:
        if mid_count % 2 == 0:
            adjustment += 5
        else:
            adjustment -= 2
    elif low_count > 2:
        adjustment -= 8
        temp_flag = True if sum(1 for x in feedback if x == 0) else False
        if temp_flag:
            adjustment -= 3

    # Bitwise interference (semi-relevant)
    stability_key = (high_count ^ mid_count) & 0xF
    if stability_key > 7:
        adjustment += 1

    # Core calculation - only this matters for final result
    raw_score = (high_count * 10) + (mid_count * 4) - (low_count * 7)
    result_score = raw_score + adjustment

    # More distractions: unused transformations
    normalized = [round((x - mean_val) * decay_factor, 2) for x in feedback]
    outlier_flags = [(i, x > threshold + 5) for i, x in enumerate(feedback)]

    return result_score

# Input data
feedback_sequence = [85, 70, 90, 60, 95, 40, 80]
base_threshold = 75

# Key computation step
result_score = evaluate_performance(feedback_sequence, base_threshold)

print(f"Result: {result_score}")