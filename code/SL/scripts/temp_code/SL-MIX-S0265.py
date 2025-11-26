import itertools

def analyze_quiz_results():
    student_responses = ['A', 'B', 'C', 'A', 'D', 'B', 'C', 'A']
    correct_answers = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
    
    # Calculate base scores (distractor - not used in final answer)
    base_scores = []
    for i, (resp, ans) in enumerate(zip(student_responses, correct_answers)):
        if resp == ans:
            base_scores.append(10)
        else:
            base_scores.append(0)
    
    # Find consecutive correct patterns using itertools
    consecutive_correct = []
    for key, group in itertools.groupby(zip(student_responses, correct_answers), lambda x: x[0] == x[1]):
        if key:
            consecutive_correct.append(len(list(group)))
    
    # Calculate bonus points for streaks (relevant)
    bonus_points = sum(streak * 2 for streak in consecutive_correct if streak > 1)
    
    # Main scoring calculation
    scores = []
    for resp, ans in zip(student_responses, correct_answers):
        if resp == ans:
            scores.append(5)
        else:
            scores.append(-1)
    
    # Distractor calculation (appears relevant but not used)
    total_questions = len(student_responses)
    percent_correct = sum(1 for resp, ans in zip(student_responses, correct_answers) if resp == ans) / total_questions * 100
    
    # Final result
    final_score = sum(scores) + bonus_points
    print(f"Target result: {final_score}")

analyze_quiz_results()