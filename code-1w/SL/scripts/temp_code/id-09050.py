def calculate_final_score():
    # Student quiz results
    correct_answers = {1, 2, 4, 5, 7, 9}
    total_questions = 10
    
    # Bonus for consecutive correct answers
    bonus_points = 0
    for i in range(1, total_questions + 1):
        if i in correct_answers and (i-1) in correct_answers:
            bonus_points += 1
    
    base_score = len(correct_answers) * 10
    penalty = 0
    
    # Penalty for skipping two or more consecutive questions
    skipped = set(range(1, total_questions + 1)) - correct_answers
    for i in range(1, total_questions):
        if i in skipped and (i+1) in skipped:
            penalty += 5
            break  # Only first occurrence counts
    
    initial_score = base_score + bonus_points - penalty
    
    # Apply curve: add 5% of current score if below 80
    if initial_score < 80:
        initial_score += initial_score * 0.05
    
    final_score = int(round(initial_score))
    return final_score

result = calculate_final_score()
print(f"Result: {result}")