def process_results(grades, thresholds):
    weighted_sum = 0
    total_weight = 0
    adjustment_factor = 0.95
    
    # Irrelevant string processing (distractor)
    subject_labels = ['Math', 'Physics', 'Chemistry', 'Biology', 'Literature']
    labeled_grades = {s: g for s, g in zip(subject_labels, grades)}
    grade_descriptions = []
    for label, score in labeled_grades.items():
        desc = f'{label}: {"Pass" if score >= 60 else "Fail"}'
        grade_descriptions.append(desc)
    
    # Misleading intermediate calculation (dead computation)
    avg_without_weight = sum(grades) / len(grades)
    temp_deviation = [abs(g - avg_without_weight) for g in grades]
    max_dev = max(temp_deviation)
    
    # Actual weighted logic with threshold masking
    masked_weights = []
    for i, thresh in enumerate(thresholds):
        weight = 1.0
        if grades[i] < thresh:
            weight = 0.7  # Penalty for not meeting threshold
        if i % 2 == 0:
            weight *= 1.1  # Slight bonus for even-indexed subjects
        masked_weights.append(weight)
    
    # Core accumulation logic
    for j, grade in enumerate(grades):
        contribution = grade * masked_weights[j]
        weighted_sum += contribution
        total_weight += masked_weights[j]
    
    normalized_result = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Final adjustment using distractor variable (but only once)
    final_score = normalized_result * adjustment_factor
    
    # Print result as required
    print(f'Result: {final_score}')
    return final_score

# Input data
grades = [88, 72, 91, 64, 77]
threshholds = [80, 70, 85, 60, 75]  # Note intentional typo to test attention

# Execution
final_score = process_results(grades, threshholds)