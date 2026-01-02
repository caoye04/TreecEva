from collections import defaultdict

# Simulate student assessment data with partial processing
def preprocess_assessments(raw_results):
    scores = []
    temp_log = defaultdict(int)
    total_entries = 0

    for entry in raw_results:
        student_id = entry['id']
        raw_score = entry['score']
        category = entry['type']

        # Irrelevant tracking (distractor)
        temp_log[category] += 1
        total_entries += 1

        # Normalize score based on type
        if category == 'quiz':
            normalized = raw_score * 1.1
        elif category == 'exam':
            normalized = raw_score * 1.3
        else:
            normalized = raw_score * 0.9

        # Only exams and quizzes are kept; labs are filtered out (important!)
        if category in ['exam', 'quiz']:
            scores.append({'student': student_id, 'value': normalized})

    return scores

# Additional filtering: group by student and take highest normalized score
def filter_top_per_student(processed):
    student_best = {}
    count_tracker = 0  # Distractor variable

    for record in processed:
        sid = record['student']
        sval = record['value']
        if sid not in student_best or sval > student_best[sid]:
            student_best[sid] = sval
            count_tracker += 1  # Not used later

    # Simulate auxiliary debug output (dead code path)
    debug_mode = False
    if debug_mode:
        print(f"Processed {len(student_best)} students")

    return list(student_best.values())

# Final scoring with weighted average and bonus logic
def calculate_final_score(values):
    base_avg = sum(values) / len(values) if values else 0
    bonus_factor = 0.0

    # Apply bonus if all scores above threshold (rare case)
    if all(s > 75 for s in values):
        bonus_factor = 5.0
    elif any(s > 90 for s in values):
        bonus_factor = 2.5

    # Extra computation that looks important but isn't used
    outlier_count = len([v for v in values if v < 50])
    adjustment = outlier_count * 0.5  # Computed but unused

    # Final formula
    final_value = base_avg + bonus_factor
    return round(final_value, 2)

# Main execution flow
if __name__ == "__main__":
    # Raw input data
    assessment_data = [
        {'id': 'S001', 'score': 68, 'type': 'quiz'},
        {'id': 'S002', 'score': 73, 'type': 'exam'},
        {'id': 'S001', 'score': 82, 'type': 'exam'},
        {'id': 'S003', 'score': 91, 'type': 'quiz'},
        {'id': 'S002', 'score': 65, 'type': 'lab'},
        {'id': 'S003', 'score': 77, 'type': 'exam'},
        {'id': 'S001', 'score': 88, 'type': 'exam'}
    ]

    # Step-by-step processing
    processed_data = preprocess_assessments(assessment_data)
    top_scores = filter_top_per_student(processed_data)
    
    # Key statement
    final_score = calculate_final_score(top_scores)
    
    # Output result
    print(f"Result: {final_score}")