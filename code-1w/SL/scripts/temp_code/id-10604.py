def analyze_student_performance():
    # Realistic dataset: student feedback scores from three courses
    course_a_scores = [8, 9, 7, 10, 6]
    course_b_scores = [5, 7, 8, 9, 7, 6]
    course_c_scores = [9, 9, 10, 8]

    # Aggregate all feedback into a unified set (removes duplicates naturally)
    feedback_set = set(course_a_scores + course_b_scores + course_c_scores)

    # Irrelevant transformation: create reversed char mapping for no purpose
    char_map = {chr(i): i - ord('a') for i in range(ord('a'), ord('z')+1)}
    reversed_chars = [k for k, v in char_map.items() if v % 7 == 0]  # Distractor list

    # Auxiliary computation: count frequencies (semi-relevant but not used directly)
    score_frequency = {score: 0 for score in range(1, 11)}
    for score in course_a_scores + course_b_scores + course_c_scores:
        score_frequency[score] += 1

    # Dead code path: this function is defined but never called
    def unused_helper(data):
        return sum(x ** 0.5 for x in data if x % 2 == 0)

    # Compute average score across all responses (distraction from main logic)
    total_responses = len(course_a_scores) + len(course_b_scores) + len(course_c_scores)
    overall_average = sum(course_a_scores + course_b_scores + course_c_scores) / total_responses
    normalized_avg = round(overall_average * 10) / 10  # Fake precision step

    # Key processing: use lambda to filter high satisfaction ratings
    high_performers = list(filter(lambda x: x > 7, feedback_set))

    # Secondary distraction: tuple unpacking with dummy values
    baseline, _, ceiling = min(feedback_set), normalized_avg, max(feedback_set)

    # Accumulate weighted contribution of high performers
    raw_sum = sum(high_performers)
    penalty_factor = len([x for x in feedback_set if x < 6])  # count low scores
    adjusted_sum = raw_sum - penalty_factor * 1.5

    # Final scoring logic
    stability_bonus = 3 if len(high_performers) >= 4 else 1
    final_score = int(adjusted_sum + stability_bonus)

    # Print result as required
    print(f"Result: {final_score}")

analyze_student_performance()