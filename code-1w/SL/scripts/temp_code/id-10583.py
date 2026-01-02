def calculate_final_score():
    # Initial scores from different assessment components
    quiz_scores = {85, 90, 78, 92}
    project_scores = {88, 90, 85, 95}
    
    # Common scores across both assessments (intersection)
    common_scores = quiz_scores & project_scores
    
    # Bonus points for consistent performance
    bonus = len(common_scores) * 3
    
    # Case conversion used in logging (irrelevant to computation - mild distractor)
    status = "PASS".lower()
    
    # Compute base score as average of all unique scores
    all_unique_scores = quiz_scores | project_scores
    base_average = sum(all_unique_scores) / len(all_unique_scores)
    
    # Apply bonus only if student has at least one perfect score
    has_perfect = 100 in all_unique_scores or 95 in all_unique_scores
    extra_credit = 5 if has_perfect else 0
    
    # Final calculation
    final_score = base_average + bonus + extra_credit
    
    # Early return not needed; proceed to end
    return final_score

# Execute and print result
result = calculate_final_score()
print(f"Result: {result}")