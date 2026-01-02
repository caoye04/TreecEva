def process_results(grades, thresholds):
    total_students = len(grades)
    passing_threshold = thresholds[0]
    distinction_threshold = thresholds[1]

    # Irrelevant pre-processing (distractor)
    normalized = [round((g - 50) / 50 * 10 + 5, 2) for g in grades]
    noise = sum([n ** 0.5 for n in normalized if n > 4])

    # Track relevant metrics
    passed_count = 0
    distinction_count = 0
    weighted_sum = 0.0

    for i, grade in enumerate(grades):
        if grade >= passing_threshold:
            passed_count += 1
            weighted_sum += grade * 0.85
            if grade >= distinction_threshold:
                distinction_count += 1

    # Use of zip and enumerate (required features)
    adjustments = []
    for idx, (g, n) in enumerate(zip(grades, normalized)):
        if idx % 3 == 0:
            adjustments.append(g * (n / 100))
        else:
            adjustments.append(0)

    adjustment_total = sum(adjustments)

    # Secondary logic path that doesn't affect final result (dead branch)
    if len(grades) > 1000:
        scaling_factor = 1.2
    else:
        scaling_factor = 1.0  # Not used below

    # Core computation
    base_score = passed_count * 10 + distinction_count * 25
    bonus = int(adjustment_total * 0.5) if adjustment_total > 50 else 0
    final_score = base_score + bonus - int(noise // 10)

    return final_score

# Input data
grades = [78, 85, 92, 67, 88, 91, 73, 85, 95, 80, 77, 89, 90, 82, 87]
thresholds = [75, 90]

# Key execution point
final_score = process_results(grades, thresholds)
print(f"Target result: {final_score}")