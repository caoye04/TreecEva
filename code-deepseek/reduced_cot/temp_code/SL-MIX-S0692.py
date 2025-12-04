def calculate_student_scores():
    student_names = ['Alice', 'Bob', 'Charlie', 'Diana']
    test_scores = [85, 92, 78, 88]
    
    # Calculate weighted scores using enumerate
    weighted_scores = []
    for idx, score in enumerate(test_scores):
        adjusted_score = score + (idx * 2)
        weighted_scores.append(adjusted_score)
    
    # Process scores with conditional expressions
    processed_scores = [score if score >= 80 else score + 5 for score in weighted_scores]
    
    # Calculate final result
    enumerate_scores = [score * 2 for score in processed_scores]
    total_score = sum(enumerate_scores)
    
    print(f"Total score: {total_score}")
    return total_score

calculate_student_scores()