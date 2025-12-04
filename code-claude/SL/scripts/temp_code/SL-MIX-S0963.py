def calculate_student_performance(grades, weights, bonus_criteria=None):
    # Initialize variables
    total_score = 0
    max_possible = 100
    passing_threshold = 60
    
    # Calculate weighted average of grades
    for grade, weight in zip(grades, weights):
        total_score += grade * weight
    
    # Calculate potential improvement points (not used in final calculation)
    potential_improvement = max_possible - total_score
    improvement_factor = lambda x: x * 0.1 if x > 0 else 0
    potential_bonus = improvement_factor(potential_improvement)
    
    # Determine bonus multiplier based on criteria
    bonus_multiplier = 1.0
    if bonus_criteria:
        # Check if all grades are above passing threshold
        all_passing = all(grade >= passing_threshold for grade in grades)
        
        # Check if average grade is in top tier
        top_tier = total_score >= 85
        
        # Track participation metrics (distraction)
        participation_points = sum([5 if grade > 75 else 0 for grade in grades])
        
        # Apply bonus based on criteria
        bonus_multiplier = 1.15 if all_passing and top_tier else 1.0
        
        # Additional adjustment that doesn't affect the final result
        adjusted_factor = bonus_multiplier + 0.05 if participation_points > 10 else bonus_multiplier
        bonus_multiplier = bonus_multiplier  # Unchanged
    
    # Apply penalty for missing weights (distraction)
    missing_weights = 1.0 - sum(weights)
    penalty = 0.05 * missing_weights if missing_weights > 0 else 0
    
    # Calculate effective score with bonus
    effective_score = total_score * bonus_multiplier
    
    # Apply a conditional adjustment based on threshold (not used)
    threshold_adjustment = 5 if total_score < 70 else -3 if total_score > 90 else 0
    
    # Create a tuple with various metrics (distraction)
    performance_metrics = (total_score, effective_score, potential_improvement)
    
    return effective_score

# Test data
grades = [87, 92, 78, 95]
weights = [0.25, 0.30, 0.15, 0.30]
bonus_criteria = True

# Calculate the student's performance
result = calculate_student_performance(grades, weights, bonus_criteria)
print(f"Result: {result}")