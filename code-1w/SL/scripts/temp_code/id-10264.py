def calculate_final_score(assessments, bonuses):
    base_score = sum(assessments.values())
    bonus_multiplier = len(bonuses) + 1
    
    # Apply domain-specific adjustments
    adjusted_scores = []
    for subject, score in assessments.items():
        if 'math' in subject.lower():
            score *= 1.2
        elif 'science' in subject.lower():
            score *= 1.15
        adjusted_scores.append(score)
    
    total_adjusted = sum(adjusted_scores)
    final_score = total_adjusted * bonus_multiplier
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = 100 * len(assessments)
    
    return int(final_score)

# Input data
assessments = {
    'Mathematics': 85,
    'Physics': 90,
    'Chemistry': 87,
    'Literature': 78
}
bonuses = ['research', 'leadership']

final_score = calculate_final_score(assessments, bonuses)
print(f"Result: {final_score}")