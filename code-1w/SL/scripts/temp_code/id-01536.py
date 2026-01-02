def evaluate_performance(attendance, results):
    # Mapping performance levels to score multipliers
    performance_scale = {'excellent': 1.5, 'good': 1.2, 'average': 1.0, 'poor': 0.7}
    attendance_bonus = {True: 5, False: 0}

    base_score = sum(results.values())
    avg_score = base_score / len(results)

    # Determine performance category
    if avg_score >= 90:
        category = 'excellent'
    elif avg_score >= 75:
        category = 'good'
    elif avg_score >= 60:
        category = 'average'
    else:
        category = 'poor'

    # Apply multiplier based on performance
    scaled_score = base_score * performance_scale[category]

    # Add bonus for perfect attendance
    perfect_attendance = all(attendance)
    final_score = scaled_score + attendance_bonus[perfect_attendance]

    # Irrelevant distraction: unused variable
    max_possible = 100 * len(results)

    return int(final_score)

# Input data
exam_results = {'math': 88, 'science': 92, 'english': 85, 'history': 78}
attendance = [True, True, True, True]  # Full attendance

final_score = evaluate_performance(attendance, exam_results)
print(f"Result: {final_score}")