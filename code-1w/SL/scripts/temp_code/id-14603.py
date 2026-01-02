from itertools import compress, count

# Simulate student test responses and grading logic
def evaluate_performance(marks, thresholds):
    # Irrelevant transformation: shuffle order (but we don't use shuffled)
    shuffled = [x * 0.95 for x in marks if x > 70]  # distractor computation

    # Track cumulative performance above threshold
    counter = count(1)
    passed_zones = []
    temp_buffer = []

    for mark in marks:
        zone_id = next(counter)
        if mark >= thresholds['pass']:
            passed_zones.append(zone_id)
            temp_buffer.append(mark * 1.1)  # bonus consideration (not used)

    # Secondary logic: check for excellence clusters
    excellence_runs = 0
    run_length = 0
    for mark in marks:
        if mark >= thresholds['excellence']:
            run_length += 1
        else:
            if run_length >= 2:
                excellence_runs += 1
            run_length = 0
    if run_length >= 2:
        excellence_runs += 1

    # Bonus score only applies if at least 2 excellence runs
    dynamic_bonus = 5 if excellence_runs >= 2 else 2

    # Base score: average of marks above 60, floored
    relevant_marks = [m for m in marks if m > 60]
    base_score = sum(relevant_marks) // len(relevant_marks) if relevant_marks else 0

    # Apply bonus based on passed zones
    zone_bonus = len(passed_zones) * 3

    # Distractor: unused statistical measure
    variance_proxy = sum((m - base_score) ** 2 for m in relevant_marks) / len(relevant_marks) if relevant_marks else 0

    # Final calculation
    final_score = base_score + zone_bonus + dynamic_bonus

    # Dead code path - never executed due to logic
    if False and len(temp_buffer) > 10:
        final_score *= 1.1

    return final_score

# Input data
marks = [68, 72, 85, 90, 58, 73, 88, 91, 64, 77]
thresholds = {'pass': 70, 'excellence': 85}

# Execute and print result
target_result = evaluate_performance(marks, thresholds)
print(f"Result: {target_result}")