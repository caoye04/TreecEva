def calculate_student_performance(scores_dict):
    total_sum = 0
    valid_count = 0
    processed_scores = []
    
    # Process each student's score
    for student, score_data in scores_dict.items():
        base_score = score_data.get('exam', 0)
        bonus = score_data.get('bonus', 0)
        is_valid = score_data.get('valid', True)
        
        # Distractor calculation that doesn't affect final result
        temp_adjustment = (base_score * 2) - bonus
        
        if is_valid and base_score >= 0:
            adjusted_score = base_score + bonus
            processed_scores.append(adjusted_score)
            total_sum += adjusted_score
            valid_count += 1
        
        # Unused intermediate variable
        potential_max = max(base_score, bonus) if base_score > 0 else 0
    
    # Calculate average using only valid scores
    adjusted_sum = total_sum + 10  # Small adjustment
    final_score = adjusted_sum // valid_count if valid_count > 0 else -1
    
    # Print result for verification
    print(f"Result: {final_score}")
    return final_score

# Test data
student_scores = {
    'alice': {'exam': 85, 'bonus': 5, 'valid': True},
    'bob': {'exam': 92, 'bonus': 8, 'valid': True},
    'charlie': {'exam': 78, 'bonus': 0, 'valid': False},
    'diana': {'exam': 88, 'bonus': 3, 'valid': True}
}

result = calculate_student_performance(student_scores)