def analyze_student_data(records):
    total_points = 0
    bonus_eligibility = []
    penalty_tracker = {}

    for record in records:
        student_id = record['id']
        scores = record['scores']
        attendance = record['attendance']

        # Irrelevant aggregation (distractor)
        avg_score = sum(scores) / len(scores)
        if avg_score >= 80:
            bonus_eligibility.append(student_id)

        # Real computation begins
        passed_count = sum(1 for s in scores if s >= 60)
        high_performer = passed_count == len(scores) and avg_score > 75

        # Track penalties for perfect scorers (mostly unused)
        perfect_score = all(s == 100 for s in scores)
        if perfect_score:
            penalty_tracker[student_id] = 0  # Dead code path

        # Core logic disguised among distractions
        base_points = len([s for s in scores if s > 70])
        adjustment = (attendance // 10) * 2
        total_points += base_points + adjustment

    # Unused helper (distractor)
    def apply_curve(value):
        return round(value * 1.1, 2)

    # Semi-relevant transformation
    scaled_total = total_points * 3

    # Mapping metrics with lambda (required feature)
    metric_map = {
        'raw': total_points,
        'scaled': scaled_total,
        'bonus_candidates': len(bonus_eligibility),
        'penalty_cases': len(penalty_tracker)
    }

    # Another distractor function
    validate_entry = lambda x: isinstance(x, dict) and 'id' in x

    # Key statement where answer is determined
    final_score = evaluate_performance(metric_map, lambda x: x > 75)

    print(f"Target result: {final_score}")


def evaluate_performance(metrics, threshold_func):
    count = 0
    # Mix of relevant and irrelevant checks
    for key, value in metrics.items():
        if 'scaled' in key and threshold_func(value):
            count += value // 25  # Contributes meaningfully
        elif key == 'bonus_candidates' and value > 0:
            count += 1  # Minor contribution
        elif key == 'penalty_cases':  # This branch does nothing due to data
            count -= value
    return count

# Setup input data
student_records = [
    {'id': 'S001', 'scores': [85, 90, 78, 92], 'attendance': 95},
    {'id': 'S002', 'scores': [60, 72, 80, 88], 'attendance': 88},
    {'id': 'S003', 'scores': [95, 87, 90, 93], 'attendance': 100},
]

# Execute main logic
analyze_student_data(student_records)