def evaluate_students():
    student_records = [
        {'name': 'Alice', 'score': 85, 'active': True},
        {'name': 'Bob', 'score': 72, 'active': True},
        {'name': 'Charlie', 'score': 90, 'active': False},
        {'name': 'Diana', 'score': 78, 'active': True},
        {'name': 'Eve', 'score': 95, 'active': True}
    ]

    passing_threshold = 75
    scaling_factor = 3
    adjustment = -5

    # Extract names of students with scores above threshold and who are active
    passed_set = {s['name'] for s in student_records if s['score'] >= passing_threshold and s['active']}
    bonus_names = {'Alice', 'Eve', 'Frank'}  # Some external bonus qualifiers

    # Only count those who both passed and are in bonus group
    passing_names = passed_set & bonus_names

    final_score = len(passing_names) * scaling_factor + adjustment

    # Irrelevant string manipulation (minimal distraction)
    status_report = " | ".join(sorted(passing_names))
    summary = f"Final Report: {status_report.upper()}"

    print(f"Result: {final_score}")

evaluate_students()