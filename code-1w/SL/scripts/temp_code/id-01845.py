from collections import defaultdict

# Simulate student quiz scoring with penalty deductions
def calculate_final_score(raw_scores, infractions):
    base_score = sum(raw_scores)
    deduction_map = defaultdict(int)
    
    for issue in infractions:
        deduction_map[issue] += 1
    
    total_deductions = 0
    # Late submission: -2 per occurrence, Plagiarism warning: -5
    if 'late' in deduction_map:
        total_deductions += deduction_map['late'] * 2
    if 'plagiarism' in deduction_map:
        total_deductions += deduction_map['plagiarism'] * 5
    
    temp_buffer = [x * 0.1 for x in raw_scores]  # Irrelevant computation (minimal interference)
    smoothed = sum(temp_buffer)
    
    result = base_score - total_deductions  # Key statement
    return result

scores = [8, 7, 9, 6]
penalties = ['late', 'late', 'plagiarism']
final_grade = calculate_final_score(scores, penalties)
Result: {final_grade}