def calculate_final_score(data):
    base_score = data['written_exam'] * 0.6
    bonus_points = 0
    
    if data['interview_passed']:
        bonus_points += data['interview_score'] * 0.2
    
    if data['coding_challenge_solved']:
        bonus_points += 15
    
    total_experience = sum(data['years_of_experience'].values())
    experience_bonus = total_experience * 2
    
    final_score = base_score + bonus_points + experience_bonus
    return final_score

exam_data = {
    'written_exam': 85,
    'interview_passed': True,
    'interview_score': 70,
    'coding_challenge_solved': True,
    'years_of_experience': {
        'python': 3,
        'java': 2,
        'javascript': 1
    }
}

final_score = calculate_final_score(exam_data)
print(f"Result: {final_score}")