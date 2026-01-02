def analyze_student_performance():
    student_scores = [85, 90, 78, 92, 88, 76, 95, 84]
    subject_weights = [0.2, 0.25, 0.15, 0.1, 0.3]
    average_score = sum(student_scores) / len(student_scores)
    
    # Normalize scores relative to average
    normalized_offsets = [score - average_score for score in student_scores]
    
    # Identify high-performing students (above average)
    high_performers = [i for i, offset in enumerate(normalized_offsets) if offset > 0]
    
    # Extract scores for high performers using indexing
    filtered_scores = [student_scores[i] for i in high_performers]
    
    # Apply weight transformation (irrelevant to final result but adds context)
    weighted_total = sum(w * 100 for w in subject_weights)  # Dummy calculation
    
    result = sum(filtered_scores)
    print(f"Target result: {result}")

analyze_student_performance()