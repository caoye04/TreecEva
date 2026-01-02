def evaluate_performance(hours_worked, tasks_completed):
    base_rate = 25
    hourly_pay = hours_worked * base_rate
    task_incentive = tasks_completed * 15
    
    # Calculate raw performance score
    raw_score = hourly_pay + task_incentive
    
    # Apply experience multiplier (senior staff get 1.2x)
    experience_level = 'senior'
    multiplier = 1.2 if experience_level == 'senior' else 1.0
    adjusted_score = raw_score * multiplier
    
    # Determine bonus eligibility
    bonus_eligible = tasks_completed >= 10 and hours_worked >= 40
    performance_bonus = 200 if bonus_eligible else 0
    
    # Miscellaneous calculation (irrelevant to final result)
    avg_task_time = hours_worked / tasks_completed if tasks_completed > 0 else 0
    
    # Final adjustments based on team outcome
    team_success = True
    final_adjustment = adjusted_score + (50 if team_success else 0)
    
    # Compute total score
    total_score = final_adjustment + performance_bonus
    
    # Print result for verification
    print(f"Result: {total_score}")

# Execute function with sample input
evaluate_performance(45, 12)