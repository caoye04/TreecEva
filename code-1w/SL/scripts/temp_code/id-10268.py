def calculate_student_performance(scores, threshold=50):
    # Normalize scores using lambda and enumerate
    normalized = [score ** 0.5 * 10 for score in scores]
    
    # Identify passing indices (for potential use)
    passing_indices = {i for i, val in enumerate(scores) if val >= threshold}
    
    # Apply bonus to normalized scores based on position
    adjusted = []
    for idx, val in enumerate(normalized):
        if idx % 2 == 0:
            adjusted.append(val + 5)
        else:
            adjusted.append(val + 2)
    
    # Filter scores above a dynamic threshold
    dynamic_threshold = sum(adjusted) / len(adjusted)
    filtered_scores = [val for val in adjusted if val > dynamic_threshold]
    
    # Final aggregation
    total_score = sum(filtered_scores)
    
    # Irrelevant utility: string processing distraction
    labels = ['S' + str(i) for i in range(len(scores))]
    label_map = dict(zip(labels, scores))
    
    # Output result
    print(f"Result: {total_score}")
    return total_score

# Input data
exam_scores = [45, 70, 60, 30, 80]
result = calculate_student_performance(exam_scores)