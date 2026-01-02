def compute_score_adjustment():
    raw_scores = [85, 92, 78, 63, 54, 96, 88, 70]
    passing_threshold = 75
    
    # Calculate adjusted base scores using set operations to remove borderline cases
    borderline_set = {70, 71, 72, 73, 74, 75}
    cleaned_scores = [score for score in raw_scores if score not in borderline_set]
    
    # Separate passing and failing grades
    passing_grades = {s for s in cleaned_scores if s > passing_threshold}
    failing_grades = {s for s in cleaned_scores if s <= passing_threshold}
    
    # Minor distraction: unused statistic
    average_passing = sum(passing_grades) / len(passing_grades) if passing_grades else 0
    
    # Key computation step
    final_score = max(passing_grades) - min(failing_grades)
    
    # Output result
    print(f"Result: {final_score}")
    
    return final_score

result = compute_score_adjustment()