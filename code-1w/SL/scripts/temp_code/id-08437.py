def analyze_student_performance():
    # Simulated student assessment data
    assessments = [
        {'subject': 'math', 'score': 85, 'attempts': 2},
        {'subject': 'physics', 'score': 78, 'attempts': 3},
        {'subject': 'chemistry', 'score': 92, 'attempts': 1},
        {'subject': 'biology', 'score': 88, 'attempts': 2}
    ]

    # Subjective difficulty weighting (external bias)
    difficulty_map = {
        'math': 1.2,
        'physics': 1.4,
        'chemistry': 1.1,
        'biology': 1.0
    }

    # Irrelevant transformation: convert to uppercase subjects (unused)
    upper_subjects = [subj['subject'].upper() for subj in assessments]

    # Misleading intermediate: average raw score without weighting
    raw_average = sum([a['score'] for a in assessments]) / len(assessments)

    # Simulate adjustment factor based on attempt fatigue (not used directly)
    fatigue_adjustments = []
    for a in assessments:
        if a['attempts'] > 2:
            fatigue_adjustments.append(a['score'] * 0.95)
        else:
            fatigue_adjustments.append(a['score'])

    # Dummy dictionary for distraction
    performance_flags = {}
    for a in assessments:
        if a['score'] >= 90:
            performance_flags[a['subject']] = 'excellent'
        elif a['score'] >= 80:
            performance_flags[a['subject']] = 'strong'
        else:
            performance_flags[a['subject']] = 'improvable'

    # Unused statistical computation: median-like slicing
    sorted_scores = sorted([a['score'] for a in assessments])
    mid_index = len(sorted_scores) // 2
    pseudo_median = (sorted_scores[mid_index] + sorted_scores[~mid_index]) / 2  # ~i = -i-1

    # Actual core logic: weighted performance aggregation
    def aggregate_performance(records, weights):
        total_weighted = 0.0
        total_weight = 0.0
        for record in records:
            subject = record['subject']
            score = record['score']
            weight = weights.get(subject, 1.0)
            # Boost high-attempt subjects artificially
            attempt_factor = 1 + (record['attempts'] - 1) * 0.05
            adjusted_weight = weight * attempt_factor
            total_weighted += score * adjusted_weight
            total_weight += adjusted_weight
        return int(total_weighted / total_weight)  # Final normalized integer score

    # Compute final score using correct logic path
    final_score = aggregate_performance(assessments, difficulty_map)

    # Print result as required
    print(f"Result: {final_score}")

    # Return unused values to increase cognitive load
    return final_score, raw_average, pseudo_median, upper_subjects

# Execute function
def main():
    result_tuple = analyze_student_performance()
    return result_tuple

main()