def evaluate_performance(log, feedback_list):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_count = 0

    # Track attendance patterns
    present_days = log.count('P')
    absent_days = log.count('A')
    late_days = log.count('L')
    total_days = len(log)

    # Irrelevant health metrics (distractor)
    hydration_levels = [0.8 + i * 0.02 for i in range(5)]
    average_hydration = sum(hydration_levels) / len(hydration_levels)
    stress_index = (absent_days * 2 + late_days) - present_days // 10

    # Performance scoring logic
    if present_days >= 20:
        base_score += 40
    if late_days < 3:
        base_score += 15
    if absent_days == 0:
        bonus_multiplier *= 1.2

    # Feedback sentiment analysis (uses string methods)
    positive_keywords = ['excellent', 'good', 'improved', 'reliable']
    negative_keywords = ['late', 'missed', 'poor', 'warning']

    positive_hits = 0
    negative_hits = 0

    for feedback in feedback_list:
        feedback_lower = feedback.lower()
        for word in positive_keywords:
            if word in feedback_lower:
                positive_hits += 1
        for word in negative_keywords:
            if word in feedback_lower:
                negative_hits += 1

    # Distractor: unused summary stats
    feedback_length_sum = sum(len(f) for f in feedback_list)
    avg_feedback_length = feedback_length_sum / len(feedback_list) if feedback_list else 0
    flagged_reviews = [f for f in feedback_list if 'URGENT' in f]

    # Apply feedback impact
    base_score += positive_hits * 5
    base_score -= negative_hits * 8

    # Hidden rule: perfect attendance with strong feedback gets extra boost
    if absent_days == 0 and positive_hits >= 3:
        bonus_multiplier *= 1.25

    # Final calculation
    final_score = base_score * bonus_multiplier

    # More distractions: unused performance tiers
    performance_tier = ""
    if final_score > 90:
        performance_tier = "Outstanding"
    elif final_score > 70:
        performance_tier = "Strong"
    elif final_score > 50:
        performance_tier = "Adequate"
    else:
        performance_tier = "Needs Improvement"

    compliance_rate = (present_days + late_days * 0.5) / total_days if total_days > 0 else 0
    adjustment_factor = round(compliance_rate * 100, 2)

    return int(final_score)

# Input data
attendance_log = "PPPLPAPPPLPPPLPPPAPPPPLPP"
feedback_strings = [
    "Employee showed excellent initiative this month.",
    "Minor issues with punctuality, but overall good performance.",
    "Improved reliability and consistent attendance.",
    "Late submission noted in week 3 - please address.",
    "Excellent teamwork and communication skills."
]

# Execution
final_score = evaluate_performance(attendance_log, feedback_strings)
print(f"Result: {final_score}")