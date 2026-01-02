def analyze_student_performance(scores, attendance_records, extra_credit):
    # Irrelevant preprocessing: normalize scores (not actually used)
    normalized = [round((s - min(scores)) / (max(scores) - min(scores)) * 100) for s in scores]

    # Track high performers (distraction)
    high_performers = set()
    for i, s in enumerate(scores):
        if s >= 90:
            high_performers.add(f'student_{i}')

    # Compute base average (relevant)
    avg_score = sum(scores) / len(scores)

    # Attendance penalty calculation (semi-relevant, but only one value used)
    attendance_rate = sum(1 for x in attendance_records if x == 'present') / len(attendance_records)
    penalty = 0
    if attendance_rate < 0.8:
        penalty = 5
    elif attendance_rate < 0.9:
        penalty = 2

    # Extra credit processing with string parsing (mixed relevance)
    parsed_credits = []
    for ec in extra_credit:
        if isinstance(ec, str):
            try:
                parsed_credits.append(float(ec.strip('pts')))
            except:
                parsed_credits.append(0.0)
        else:
            parsed_credits.append(float(ec))
    total_extra = sum(parsed_credits)

    # Distraction: unused function definition
    def adjust_for_difficulty(raw, level):
        return raw * (1.1 if level == 'hard' else 0.9)

    # Distraction: dead code path
    if False:
        bonus = 10
        avg_score += bonus

    # Core logic: compute weighted score
    passing_threshold = 60
    if avg_score >= passing_threshold:
        base_grade = 75 + (avg_score - passing_threshold) * 0.5
    else:
        base_grade = avg_score * 0.7

    # Apply penalty and extra credit
    adjusted_grade = base_grade - penalty + total_extra

    # Final adjustment using tuple unpacking (relevant)
    multiplier_tuple = (1.05, 1.0)  # 5% boost if >85%
    boost_multiplier, _ = multiplier_tuple if adjusted_grade > 85 else (_, 1.0)
    final_score = round(adjusted_grade * boost_multiplier, 2)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
student_scores = [88, 92, 76, 94, 85]
attendance = ['present', 'absent', 'present', 'present', 'present', 'late']
extra_pts = ["5pts", "2.5pts", 0, "1.5pts"]

# Execute
final_score = analyze_student_performance(student_scores, attendance, extra_pts)