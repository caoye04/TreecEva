def calculate_performance_rating():
    base_points = 85
    bonus_multiplier = 1.2
    penalty_rate = 0.85
    
    # Simulated weekly performance metrics
    weekly_scores = [78, 92, base_points, 88, 76]
    recent_trend = sum(1 for score in weekly_scores if score >= 80)
    
    # Calculate adjusted average with conditional boost
    raw_average = sum(weekly_scores) / len(weekly_scores)
    performance_boost = 5 if raw_average >= 85 else 0
    adjusted_average = raw_average + performance_boost
    
    # Distractor: Unused calculation for alternate metric
    hypothetical_max = (max(weekly_scores) * 1.1) // 1  # Floor after 10% increase
    decay_factor = 0.95
    deprecated_metric = hypothetical_max * decay_factor  # Not used
    
    # Attendance and punctuality factors (semi-relevant)
    attendance_rate = 0.93
    on_time_rate = 0.87
    compliance_score = (attendance_rate + on_time_rate) / 2
    
    # Apply non-linear adjustment based on consistency
    score_variance = sum((s - raw_average) ** 2 for s in weekly_scores) / len(weekly_scores)
    stability_bonus = 10 * (1 - min(score_variance / 100, 0.5))
    
    # Complex eligibility check using set operations
    eligible_categories = {'performance', 'attendance', 'punctuality'}
    met_criteria = {crit for crit in eligible_categories if globals().get(crit + '_rate', 0) > 0.85}
    category_bonus = 7 if len(met_criteria) >= 2 else 0
    
    # Final computation chain
    base_with_bonus = adjusted_average + stability_bonus + category_bonus
    applied_multiplier = base_with_bonus * bonus_multiplier
    final_deduction = applied_multiplier * (1 - penalty_rate)
    final_score = int(applied_multiplier - final_deduction)
    
    # Red herring: Bitwise manipulation of irrelevant counter
    debug_flag = 0b10101
    mask = 0b11111
    scrambled = debug_flag ^ mask  # XOR operation not affecting result
    inverted = ~scrambled & mask  # More unused logic
    
    return final_score

# Main execution
result = calculate_performance_rating()
print(f"Result: {result}")