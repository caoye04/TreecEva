def calculate_weighted_score(answers, key):
    # Calculate student score with weighted questions
    base_points = 0
    penalty = 0
    bonus_threshold = 3
    
    # Track question statistics (not used in final calculation)
    question_stats = {}
    for i, (student, correct) in enumerate(zip(answers, key)):
        question_stats[i] = {'student': student, 'correct': correct}
    
    # Process each answer with its weight
    weights = [1, 2, 1, 3, 1, 2, 2]  # Question weights
    correct_count = 0
    incorrect_answers = []
    
    # Compare answers with key and calculate points
    for i, (student, correct) in enumerate(zip(answers, key)):
        weight = weights[i] if i < len(weights) else 1
        # Check if answer matches key
        if student.lower() == correct.lower():
            base_points += weight
            correct_count += 1
        else:
            incorrect_answers.append(i+1)  # Store question number for reporting
    
    # Calculate time efficiency bonus (not used in final calculation)
    time_bonus = 5 if len(answers) > 5 else 0
    
    # Apply bonus for good performance
    bonus = 2 if correct_count >= bonus_threshold else 0
    
    # Apply penalty for specific wrong answer patterns
    if 3 in incorrect_answers and 5 in incorrect_answers:
        penalty = 1
    
    # Generate feedback string (not used in calculation)
    feedback = f"Correct: {correct_count}, Incorrect: {len(incorrect_answers)}"
    
    # Calculate final weighted score
    final_score = base_points + bonus - penalty
    
    # For debugging only (not affecting result)
    debug_info = {
        'base': base_points,
        'bonus': bonus,
        'penalty': penalty
    }
    
    return final_score

# Student test data
student_answers = ['A', 'C', 'B', 'A', 'D', 'B', 'A']
answer_key = ['A', 'B', 'B', 'A', 'C', 'B', 'D']

# Calculate the student's score
final_score = calculate_weighted_score(student_answers, answer_key)

# Store additional stats (not affecting result)
submission_time = "10:45 AM"
class_average = 8.2

print(f"Result: {final_score}")