def calculate_final_score(students):
    passing_threshold = 50
    bonus_factor = 1.1
    
    # Extract scores of students who passed, apply bonus, and filter again
    passed_scores = [min(s * bonus_factor, 100) for s in students if s >= passing_threshold]
    
    # Calculate average; if no one passed, return 0
    avg_score = sum(passed_scores) / len(passed_scores) if passed_scores else 0
    
    # Apply curve: add extra points if class average is below 75
    curve = 5 if avg_score < 75 else 0
    curved_avg = avg_score + curve
    
    # Final adjustment using conditional expression
    final_score = int(curved_avg if curved_avg > 60 else 60)
    return final_score

# List of student scores
students = [45, 70, 82, 38, 91, 47, 65]

# Compute final score
target_result = calculate_final_score(students)
print(f"Result: {target_result}")