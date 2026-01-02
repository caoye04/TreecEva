def calculate_rating(entries, importance):
    total = 0
    base_offset = len(entries) * 2
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    normalized = [x / sum(importance) for x in importance]
    scaling_factor = sum(normalized)  # Always 1.0, but included to distract

    # Core logic with meaningful computation
    for i, (val, weight) in enumerate(zip(entries, importance)):
        adjusted = val * weight
        if i % 2 == 0:
            adjusted += 1  # bonus for even indices
        temp_result.append(adjusted)
    
    # Secondary processing with red herring variables
    outlier_count = 0
    for x in temp_result:
        if x > 50:  # unlikely threshold, never triggered
            outlier_count += 1

    # Actual aggregation
    aggregate = sum(temp_result)
    penalty = 0
    for idx in range(len(temp_result)):
        if idx + 1 < len(temp_result) and temp_result[idx] > temp_result[idx + 1]:
            penalty += 1

    final_rating = aggregate - penalty
    debug_info = {'count': len(temp_result), 'offset': base_offset}  # unused

    # Final transformation
    final_score = int((final_rating + base_offset) // 1.5)
    return final_score

# Main data
assessments = [85, 90, 78, 88]
weights = [0.4, 0.3, 0.2, 0.1]

# Auxiliary irrelevant calculations (distraction)
shadow_weights = [w ** 2 for w in weights]
squared_sum = sum(shadow_weights)
placeholder = [abs(x - 80) for x in assessments if x < 85]

# Key execution point
total_validations = len(placeholder)
calibration = sum(placeholder) if placeholder else 0
final_score = calculate_rating(assessments, weights)

print(f"Result: {final_score}")