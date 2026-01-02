def process_results(data, threshold):
    # Irrelevant pre-processing: case conversion and string manipulation
    categories = {item.lower().capitalize() for item in data.keys()}
    normalized_data = {k.lower(): v for k, v in data.items()}

    # Distractor: unused helper function
    def analyze_trend(values):
        return sum(1 for i in range(1, len(values)) if values[i] > values[i-1])

    # Semi-relevant transformation using lambda
    adjuster = lambda x: x * 1.1 if x < threshold else x * 0.95
    adjusted = [adjuster(score) for score in normalized_data['performance']]

    # Tracking state across multiple steps
    running_total = 0
    count = 0
    penalty_applied = False

    for val in adjusted:
        if val > threshold * 1.05:
            running_total += val
            count += 1
        elif val < threshold * 0.8 and not penalty_applied:
            running_total -= 5  # minor penalty
            penalty_applied = True

    # Additional distraction: dead code path with list shuffling
    temp_sequence = [i for i in range(len(adjusted)) if i % 2 == 0]
    reversed_seq = temp_sequence[::-1]  # never used

    # Core logic: average only above-threshold adjusted scores, then apply fixed bonus
    if count > 0:
        base_result = running_total / count
    else:
        base_result = 0

    # Final computation
    bonus = len(categories) * 2.5
    final_result = base_result + bonus

    # Key output variable
    return int(round(final_result))

# Input data
assessment_data = {
    "Performance": [78, 85, 90, 67, 92],
    "Behavior": [4, 3, 5, 4],
    "Attendance": [95, 98, 90]
}
passing_threshold = 80

# Execution point of interest
final_score = process_results(assessment_data, passing_threshold)
print(f"Result: {final_score}")