def calculate_performance_rating():
    base_scores = [85, 90, 78, 92, 88]
    adjustments = [5, -3, 8, -5, 2]
    adjusted_points = [base_scores[i] + adjustments[i] for i in range(len(base_scores))]
    
    # Determine performance tier using conditional expression
    avg_score = sum(adjusted_points) / len(adjusted_points)
    performance_tier = 'High' if avg_score >= 85 else 'Medium' if avg_score >= 75 else 'Low'
    
    # Irrelevant metric (distractor)
    max_single_gain = max(adjustments)
    
    # Bonus logic based on tier and slicing last three results
    recent_performance = adjusted_points[-3:]
    strong_count = len([x for x in recent_performance if x >= 85])
    
    base_bonus = 10 if performance_tier == 'High' else 5
    extra_incentive = 7 if strong_count >= 2 else 0
    final_bonus = base_bonus + extra_incentive
    
    total_score = final_bonus + sum(adjusted_points)
    print(f"Result: {total_score}")

calculate_performance_rating()