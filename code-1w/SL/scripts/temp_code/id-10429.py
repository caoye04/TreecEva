def analyze_student_performance():
    # Simulated student assessment data
    assessments = [
        {'quiz': 85, 'midterm': 78, 'project': 90, 'attendance': 95},
        {'quiz': 92, 'midterm': 88, 'project': 83, 'attendance': 100},
        {'quiz': 76, 'midterm': 81, 'project': 79, 'attendance': 88}
    ]

    # Weight mapping for score aggregation
    weight_map = {
        'quiz': 0.1,
        'midterm': 0.3,
        'project': 0.4,
        'attendance': 0.2
    }

    # Auxiliary function to compute weighted score
    def compute_weighted_score(record, weights):
        total = 0.0
        for key in record:
            if key in weights:
                total += record[key] * weights[key]
        return round(total, 2)

    # Function to filter high performers (used but not directly contributing to final answer)
    def is_high_performer(record):
        return record['quiz'] > 80 and record['project'] > 85

    # Misleading intermediate: average quiz scores (not used in final logic)
    avg_quiz = sum(a['quiz'] for a in assessments) / len(assessments)
    temp_offset = avg_quiz * 0.05  # Distractor computation

    # Simulate historical baseline drift (irrelevant)
    baseline_drift = 0.0
    for i in range(2):
        baseline_drift += 0.1 * (i + 1)

    # Track count of students exceeding thresholds (semi-relevant but not critical)
    high_performer_count = 0
    performance_tracker = []
    for student in assessments:
        weighted = compute_weighted_score(student, weight_map)
        performance_tracker.append(weighted)
        if is_high_performer(student):
            high_performer_count += 1

    # Secondary structure: normalize scores against max (distractor)
    max_perf = max(performance_tracker)
    normalized_scores = [score / max_perf for score in performance_tracker]

    # Introduce redundant dictionary operation (set intersection - irrelevant)
    common_keys = set(assessments[0].keys())
    for a in assessments[1:]:
        common_keys &= set(a.keys())

    # Conditional expression to adjust threshold based on performer count (misleading)
    adjustment = 1.0 if high_performer_count >= 2 else 0.95

    # Actual core logic: aggregate all raw midterm scores with fixed bonus
    raw_midterm_total = sum(a['midterm'] for a in assessments)
    bonus_eligibility = len([a for a in assessments if a['project'] > 80])
    bonus_points = bonus_eligibility * 3.5

    # Final aggregation function (key logic)
    def aggregate_performance(records, weights):
        base_aggregate = 0
        for r in records:
            base_aggregate += r['quiz'] * weights['quiz']
            base_aggregate += r['midterm'] * weights['midterm']
            base_aggregate += r['project'] * weights['project']
        # Attendance only adds bonus if condition met (short-circuit logic)
        for r in records:
            if r['attendance'] > 90 and adjustment > 0.98:
                base_aggregate += weights['attendance'] * r['attendance'] * 0.5
        return int(base_aggregate + bonus_points)

    final_score = aggregate_performance(assessments, weight_map)
    print(f"Result: {final_score}")

analyze_student_performance()