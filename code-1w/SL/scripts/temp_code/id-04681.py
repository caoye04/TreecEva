def analyze_performance():
    student_records = [
        ('alice', 85, 'A'),
        ('bob', 72, 'C'),
        ('charlie', 90, 'A'),
        ('diana', 68, 'D'),
        ('eve', 95, 'A')
    ]

    # Extract names and convert to uppercase for uniformity
    names = {name.upper() for name, _, _ in student_records}

    # Determine passing students (grade >= 70)
    passing_students = {name for name, score, _ in student_records if score >= 70}
    failing_students = {name for name, score, _ in student_records if score < 70}

    # Compute statistics
    total_students = len(student_records)
    num_passing = len(passing_students)
    num_failing = len(failing_students)

    # Base multiplier derived from ratio of passing to total (floored to integer)
    base_multiplier = int(num_passing / total_students * 10)

    # Create filtered record set of passing students with high distinction (score >= 85)
    high_distinction = {name for name, score, _ in student_records if score >= 85}
    passing_records = passing_students.intersection(high_distinction)

    # Critical statement
    final_score = len(passing_records) * base_multiplier

    print(f"Result: {final_score}")

analyze_performance()