def analyze_performance(marks, thresholds):
    # Irrelevant transformation
    normalized = [round((m - min(marks)) / (max(marks) - min(marks)) * 100) for m in marks]
    above_threshold = [m for m in marks if m >= thresholds['passing']]
    distinction_count = len([m for m in marks if m >= thresholds['distinction']])

    # Distractor: complex but unused structure
    grade_map = {range(90, 101): 'A', range(80, 90): 'B', range(70, 80): 'C'}
    distribution = {grade: 0 for grade in 'ABCDF'}

    # Real logic begins
    avg_mark = sum(marks) / len(marks)
    passed_count = len(above_threshold)
    weight_factor = 1.5 if passed_count > 3 else 1.0

    # Conditional expression with set operation
    bonus = 10 if set(thresholds.keys()) & {'distinction', 'honor'} else 5

    # Intermediate irrelevant computation
    median_guess = sorted(marks)[len(marks)//2]
    stability_score = max(marks) - min(marks)

    # Core calculation
    base_score = avg_mark * weight_factor
    adjustment = (distinction_count * 7.5) + bonus
    
    # Final determination
    final_score = base_score + adjustment
    return int(final_score)

# Main execution
exam_marks = [78, 85, 92, 67, 88]
config = {
    'passing': 70,
    'distinction': 85,
    'honor': 95
}

# Unused variables to increase interference
ranking = [i for i, _ in enumerate(sorted(exam_marks, reverse=True))]
scaled_data = {idx: round(val * 1.1) for idx, val in enumerate(exam_marks)}

interim_result = sum([x**2 for x in exam_marks if x > 80]) // len(exam_marks)

final_score = analyze_performance(exam_marks, config)

print(f"Target result: {final_score}")