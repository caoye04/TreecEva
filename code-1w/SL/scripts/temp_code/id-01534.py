def calculate_final_score(raw_scores, bonus_threshold=85):
    adjusted_scores = [score * 1.1 for score in raw_scores if score >= 70]
    bonus_eligible = len([s for s in raw_scores if s >= bonus_threshold])
    
    # Conditional expression for performance tier
    performance_tier = 'A' if bonus_eligible >= 3 else 'B'
    
    base_score = sum(adjusted_scores) / len(adjusted_scores) if adjusted_scores else 0
    
    # Apply bonus based on eligibility using conditional expression
    bonus = 5.0 if bonus_eligible >= 2 else 2.5
    
    # Final score computation
    final_score = base_score + bonus
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = max(raw_scores) * 1.5 if raw_scores else 0
    
    return final_score

# Input data
student_scores = [88, 92, 76, 85, 90]

# Compute result
target_result = calculate_final_score(student_scores)
print(f"Result: {target_result}")