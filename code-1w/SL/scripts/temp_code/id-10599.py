def calculate_performance(records, limits):
    # Initialize tracking variables
    passing_count = 0
    total_weight = 0.0
    bonus_applied = False
    temp_result = []

    # Irrelevant pre-processing: normalize names (not used later)
    normalized_names = [record['name'].strip().lower() for record in records]
    ignored_sum = sum(len(name) for name in normalized_names)

    # Filter and assess performance against thresholds
    for record in records:
        score = record['score']
        level = record['level']
        weight = 1 + (level * 0.1)

        # Apply dynamic adjustment based on level
        adjusted_score = score * weight
        
        # Check if passes threshold
        if adjusted_score >= limits[level]:
            passing_count += 1
            temp_result.append(adjusted_score)

        total_weight += weight

    # Secondary validation using lambda filter
    valid_results = list(filter(lambda x: x > 0, temp_result))  # Redundant, all are >0

    # Compute average of valid adjusted scores
    average_passing = sum(valid_results) / len(valid_results) if valid_results else 0

    # Bonus logic based on passing ratio
    ratio_passed = passing_count / len(records) if records else 0
    if ratio_passed >= 0.75:
        bonus_factor = 1.2
        bonus_applied = True
    else:
        bonus_factor = 1.0

    # Final score calculation
    base_final = average_passing * total_weight
    final_score = base_final * bonus_factor

    # Dead code branch: never executed due to logic above
    if bonus_applied and False:
        final_score += 100  # unreachable

    return final_score


# Input data
assessments = [
    {'name': 'Alice', 'score': 85, 'level': 2},
    {'name': 'Bob',   'score': 90, 'level': 3},
    {'name': 'Charlie', 'score': 78, 'level': 1},
    {'name': 'Diana', 'score': 92, 'level': 3}
]

thresholds = {1: 75, 2: 80, 3: 85}

# Execution point
final_score = calculate_performance(assessments, thresholds)
print(f"Target result: {final_score}")