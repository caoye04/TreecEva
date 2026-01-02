from collections import defaultdict

# Simulate student assessment tracker with multiple performance metrics
def analyze_student_progress():
    assessments = [
        {'quiz': 85, 'project': 90, 'exam': 78},
        {'quiz': 88, 'project': 85, 'exam': 82},
        {'quiz': 90, 'project': 88, 'exam': 85},
        {'quiz': 80, 'project': 92, 'exam': 80}
    ]

    # Weight distribution for final evaluation (normalized later)
    raw_weights = [0.2, 0.3, 0.5]
    total_weight = sum(raw_weights)
    weights = [w / total_weight for w in raw_weights]  # Normalize to ensure sum=1

    # Track derived statistics (some used, some not)
    stats = defaultdict(int)
    avg_scores = {}
    max_deviation = 0
    adjustment_factor = 0.95

    # Compute per-category averages
    categories = ['quiz', 'project', 'exam']
    for i, cat in enumerate(categories):
        cat_total = sum(assessment[cat] for assessment in assessments)
        avg_scores[cat] = cat_total / len(assessments)
        stats[f'{cat}_sum'] = cat_total

    # Calculate variance-like measure for stability analysis (not directly used)
    for assessment in assessments:
        deviation = abs(assessment['exam'] - avg_scores['exam'])
        if deviation > max_deviation:
            max_deviation = deviation

    # Apply adjustment due to exam difficulty drift (simulated)
    adjusted_exam_avg = avg_scores['exam'] * adjustment_factor
    stats['adjusted_exam_avg'] = adjusted_exam_avg

    # Irrelevant computation: simulate peer comparison offset
    peer_offsets = []
    for i in range(len(assessments)):
        offset = (assessments[i]['project'] - assessments[i]['quiz']) * 0.1
        peer_offsets.append(offset)
    smoothness_score = sum(peer_offsets) / len(peer_offsets) if peer_offsets else 0

    # Focus on composite score aggregation
    def aggregate_performance(assessments, weights):
        weighted_sum = 0.0
        normalization_constant = len(assessments)

        # Precompute category indices for clarity
        quiz_idx, project_idx, exam_idx = 0, 1, 2

        # Aggregate each student's weighted score
        student_composites = []
        for record in assessments:
            # Extract scores in fixed order
            scores = [record['quiz'], record['project'], record['exam']]
            student_score = 0
            for j, w in enumerate(weights):
                student_score += scores[j] * w
            student_composites.append(student_score)

        # Final score is the average of weighted composites
        aggregate = sum(student_composites) / normalization_constant

        # Apply hidden floor boost if average is borderline
        floor_threshold = 82.0
        boost_applied = 0.0
        if aggregate < floor_threshold:
            boost_applied = floor_threshold - aggregate
            aggregate = floor_threshold

        # Record unused metric
        stats['boost_amount'] = boost_applied

        return round(aggregate, 4)

    # Execute key computation
    final_score = aggregate_performance(assessments, weights)

    # Dead code: slice analysis of peer offsets (not used)
    if len(peer_offsets) > 2:
        mid_slice = peer_offsets[1:-1]
        stats['mid_slice_avg'] = sum(mid_slice) / len(mid_slice)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Run function
analyze_student_progress()