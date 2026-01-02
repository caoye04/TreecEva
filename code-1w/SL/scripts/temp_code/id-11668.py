def calculate_performance_rating():
    base_points = 85
    bonus_multiplier = 1.2
    penalty_factor = 0.9
    
    # Simulate various performance metrics
    attendance_rate = 0.97
    project_count = 5
    avg_feedback_score = 4.6
    
    # Distractor: irrelevant calculation for team performance
    team_avg = (base_points * 0.6) + (avg_feedback_score * 10)
    team_bonus = team_avg * 0.05 if team_avg > 75 else 0
    
    # Individual contribution score (semi-relevant)
    individual_score = base_points
    if project_count >= 3:
        individual_score += 10
    if attendance_rate > 0.95:
        individual_score += 5
    
    # Conditional expression for efficiency tier
    efficiency_tier = 'high' if avg_feedback_score >= 4.5 else 'standard'
    efficiency_bonus = 8 if efficiency_tier == 'high' else 3
    
    # Apply multiplier and penalty based on review outcome
    review_passed = True
    adjustment_factor = bonus_multiplier if review_passed else penalty_factor
    
    # Accumulate final score through multiple steps
    raw_score = individual_score + efficiency_bonus
    adjusted_score = raw_score * adjustment_factor
    
    # More distractors: unused department-level stats
    dept_target = 90
    compliance_checks = 12
    failed_checks = 1
    compliance_rate = (compliance_checks - failed_checks) / compliance_checks
    dept_penalty = 5 if compliance_rate < 0.8 else 0  # Never applied
    
    # Final aggregation with rounding
    final_score = round(adjusted_score + team_bonus, 2)
    
    # Additional red herring: logging unrelated summary
    summary_code = f"PERF-{int(base_points)}-TEAM"
    debug_flag = len(summary_code) > 10
    
    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Result: {target_result}")