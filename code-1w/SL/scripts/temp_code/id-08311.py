from collections import Counter

def calculate_final_score():
    # Simulate student test responses and answer key
    student_responses = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']
    answer_key = ['A', 'B', 'C', 'D', 'E', 'B', 'C', 'D', 'A', 'E']
    
    # Count correct answers
    correct_count = sum(1 for i in range(len(answer_key)) if student_responses[i] == answer_key[i])
    
    # Apply scoring rules: +4 for each correct, -1 for incorrect
    raw_score = correct_count * 4
    
    # Count distribution of answers for analysis (irrelevant to score but adds mild interference)
    response_freq = Counter(student_responses)
    dominant_answer = response_freq.most_common(1)[0][1]  # Most frequent count
    
    # Incorrect attempts (not used in final calculation - mild distractor)
    incorrect_count = len(answer_key) - correct_count
    
    # Final normalized score with small adjustment based on consistency
    if dominant_answer >= 3:
        raw_score += 1  # Bonus for consistent answering pattern
    
    return raw_score

# Main execution
final_score = calculate_final_score()
print(f"Result: {final_score}")