def analyze_student_performance():
    # Simulated student feedback scores from multiple sources
    quiz_scores = [6, 8, 9, 5, 7]
    project_scores = [10, 7, 8, 9, 6]
    participation_rates = [0.8, 0.6, 0.9, 0.75, 0.82]

    # Aggregating base performance with weighted average
    weighted_avg = []
    for i in range(len(quiz_scores)):
        weighted = (quiz_scores[i] * 0.3) + (project_scores[i] * 0.5) + (participation_rates[i] * 10 * 0.2)
        weighted_avg.append(round(weighted, 2))

    # Misleading intermediate: normalize scores to 0-1 scale (not used later)
    max_weighted = max(weighted_avg)
    normalized_scores = [score / max_weighted for score in weighted_avg]
    temp_sum = sum(normalized_scores)  # Distractor variable

    # Identify high performers using threshold
    high_performers = []
    for score in weighted_avg:
        if score >= 7.5:
            high_performers.append(score)

    # Compute statistical deviations (semi-relevant, used in filtering)
    mean_perf = sum(weighted_avg) / len(weighted_avg)
    variance = sum((x - mean_perf) ** 2 for x in weighted_avg) / len(weighted_avg)
    std_dev = variance ** 0.5

    # Filter feedback set: only those above mean + 0.5σ
    threshold_filter = mean_perf + 0.5 * std_dev
    feedback_set = [s for s in weighted_avg if s > threshold_filter]

    # Auxiliary function to compute performance bands (distractor logic)
    def get_band(score):
        if score >= 9:
            return 'A'
        elif score >= 7:
            return 'B'
        else:
            return 'C'

    band_counts = {'A': 0, 'B': 0, 'C': 0}
    for s in weighted_avg:
        band = get_band(s)
        band_counts[band] += 1

    # Core logic: aggregate performance using lambda-based filter
    aggregate_performance = lambda data, condition: sum(1 for x in data if condition(x))
    final_score = aggregate_performance(feedback_set, lambda x: x > 7)

    # Additional red herring: sorting and reversing unused list
    sorted_feedback = sorted(feedback_set, reverse=True)
    reversed_copy = sorted_feedback[::-1]  # Not used

    # Print result as required
    print(f"Result: {final_score}")

analyze_student_performance()