def calculate_grade(correct, total):
    """Calculate percentage grade"""
    return (correct / total) * 100

def calculate_scores(answers):
    correct_answers = {'Q1': 'B', 'Q2': 'A', 'Q3': 'D', 'Q4': 'C', 'Q5': 'A'}
    possible_points = 20
    
    # Transform answers to uppercase for consistency
    normalized = {q: a.upper() for q, a in answers.items()}
    
    # Count correct answers
    correct_count = sum(1 for q, a in normalized.items() 
                      if q in correct_answers and a == correct_answers[q])
    
    # Apply scoring formula
    raw_score = correct_count * 4
    
    # Apply curve adjustment
    curve_adjustment = lambda score: min(score + 5, possible_points)
    final_result = curve_adjustment(raw_score)
    
    return final_result

# Student's quiz submission
student_answers = {
    'Q1': 'b',  # Correct (case insensitive)
    'Q2': 'C',  # Incorrect
    'Q3': 'D',  # Correct
    'Q4': 'B',  # Incorrect
    'Q5': 'a'   # Correct
}

# Calculate the student's score
final_score = calculate_scores(student_answers)
print(f"Result: {final_score}")