def analyze_student_performance():
    # Simulated student assessment data
    assessments = {
        'quiz1': 85, 'quiz2': 90, 'midterm': 78, 'project': 92, 'final_exam': 88
    }

    # Weight distribution (some are red herrings)
    weights = {
        'quiz1': 0.1, 'quiz2': 0.1, 'midterm': 0.2, 'project': 0.25, 
        'final_exam': 0.3, 'participation': 0.05  # participation weight unused
    }

    # Extraneous data structures for distraction
    grade_boundaries = [90, 80, 70, 60]
    letter_grades = ['A', 'B', 'C', 'D', 'F']
    bonus_awarded = set()
    dropped_quizzes = []

    # Simulate some irrelevant logic
    if assessments['quiz1'] > assessments['quiz2']:
        bonus_awarded.add('quiz1')
    else:
        dropped_quizzes.append('quiz2')

    # Unused intermediate calculations
    average_quiz_score = (assessments['quiz1'] + assessments['quiz2']) / 2
    max_score = max(assessments.values())
    min_score = min(assessments.values())
    score_range = max_score - min_score  # not used

    # Distractor: complex but unused transformation
    normalized_scores = {}
    for k, v in assessments.items():
        normalized_scores[k] = round((v - 50) / 50, 2)  # arbitrary scaling

    # Actual computation happens here — only uses subset of weights
    def aggregate_performance(assessments, weights):
        total = 0.0
        effective_weight_sum = 0.0

        # Only apply weights to existing assessments
        for key in assessments:
            if key in weights:
                total += assessments[key] * weights[key]
                effective_weight_sum += weights[key]
        
        # Normalize by actual applied weights
        if effective_weight_sum > 0:
            total /= effective_weight_sum

        # Additional logic that looks important but doesn't affect final_score
        ceiling_adjustment = 100 - total
        if ceiling_adjustment < 5:
            total += 2.0  # minor boost

        return round(total, 4)

    # Irrelevant list accumulation
    all_keys = []
    for key in assessments.keys():
        all_keys.append(key.upper())
    all_keys.sort(reverse=True)

    # Key execution point
    final_score = aggregate_performance(assessments, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")
    
    return final_score

# Execute function
analyze_student_performance()