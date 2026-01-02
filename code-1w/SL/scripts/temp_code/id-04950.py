def process_student_data(records):
    # Irrelevant preprocessing: count total records and log lengths
    record_count = len(records)
    name_lengths = [len(record[0]) for record in records]
    avg_name_length = sum(name_lengths) / record_count if record_count else 0

    # Extract marks and compute weighted scores (some distraction here)
    weights = [0.2, 0.3, 0.5]
    weighted_sums = []
    for r in records:
        student_marks = r[1]
        weighted = sum([marks * weight for marks, weight in zip(student_marks, weights)])
        weighted_sums.append(weighted)

    # Distractor: normalize scores unnecessarily
    max_weighted = max(weighted_sums) if weighted_sums else 1
    normalized_scores = [ws / max_weighted for ws in weighted_sums]

    # Real logic begins: identify passing students based on threshold per subject
    marks = [record[1] for record in records]
    thresholds = [60, 65, 70]

    def calculate_total(marks_list, required):
        passed_count = 0
        for student in marks_list:
            # Check if all subjects meet threshold
            passed = True
            for i in range(len(required)):
                if student[i] < required[i]:
                    passed = False
                    break
            if passed:
                passed_count += 1

        # Bonus logic: add entropy-like penalty for score variance
        all_flat = [mark for s in marks_list for mark in s]
        mean_val = sum(all_flat) / len(all_flat)
        variance = sum((x - mean_val) ** 2 for x in all_flat) / len(all_flat)
        penalty = int(variance // 10)  # Only affects final by small margin

        # Use lambda to filter high performers (distraction but semi-relevant)
        is_high = lambda x: all(score >= 85 for score in x)
        high_performers = [s for s in marks_list if is_high(s)]
        bonus = len(high_performers) * 2

        return passed_count * 10 + bonus - penalty

    # Unused helper function (dead code path - distractor)
    def unused_diagnostic(data):
        return [sum(d) / len(d) for d in data]

    # Key statement
    final_score = calculate_total(marks, thresholds)

    # Extra irrelevant accumulation
    total_chars_processed = sum(len(r[0]) for r in records)
    _ = [total_chars_processed for _ in range(2)]  # dummy list comp

    print(f"Result: {final_score}")
    return final_score

# Input data
student_records = [
    ("Alice", [78, 85, 60]),
    ("Bob", [55, 70, 75]),
    ("Charlie", [90, 88, 86]),
    ("Diana", [62, 68, 71]),
    ("Eve", [92, 94, 89])
]

# Execute
process_student_data(student_records)