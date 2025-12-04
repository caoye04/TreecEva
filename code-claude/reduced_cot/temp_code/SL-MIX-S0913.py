# Student submission scoring system
def calculate_student_score(submissions):
    # Process each submission
    points = []
    valid_submissions = []
    total_chars = 0
    
    for i, submission in enumerate(submissions):
        # Skip empty submissions
        if not submission:
            continue
            
        # Count characters for analytics
        total_chars += len(submission)
        
        # Calculate points based on length and case
        uppercase_count = sum(1 for c in submission if c.isupper())
        point_value = len(submission) + (uppercase_count * 0.5)
        
        # Only consider valid submissions (non-empty)
        valid_submissions.append(submission)
        points.append(point_value)
    
    # Calculate average score if there are valid submissions
    if valid_submissions:
        score = sum(points) / len(valid_submissions)
        # Apply bonus for consistent submissions
        bonus_factor = 1.0 if len(valid_submissions) == len(submissions) else 0.9
        adjusted_score = score * bonus_factor
        return score
    else:
        return 0

# Test with sample submissions
student_submissions = ["Hello", "Python", "CODING", ""]
result = calculate_student_score(student_submissions)
print(f"Result: {result}")