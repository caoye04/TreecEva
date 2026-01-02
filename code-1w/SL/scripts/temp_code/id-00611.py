def calculate_performance_rating():
    # Employee performance data
    base_scores = [85, 90, 78, 92, 88]
    attendance_rate = 0.94
    peer_review_multiplier = 1.05
    
    # Irrelevant metrics (distractors)
    days_off = 3
    office_temperature = 21.5  # Celsius, not used
    coffee_consumed = 5  # cups per week, irrelevant
    
    # Step 1: Compute average performance score
    avg_base = sum(base_scores) / len(base_scores)
    
    # Step 2: Apply attendance adjustment (conditional logic)
    if attendance_rate >= 0.9:
        attendance_bonus = 5
    else:
        attendance_bonus = 2
    
    adjusted_score = avg_base + attendance_bonus
    
    # Step 3: Apply peer review multiplier
    enhanced_score = adjusted_score * peer_review_multiplier
    
    # Step 4: Bonus for consistent high performers (using enumerate)
    consistency_bonus = 0
    for i, score in enumerate(base_scores):
        if score >= 90:
            consistency_bonus += 1.5 if i % 2 == 0 else 0.5  # Extra bonus on even indices
    
    # Step 5: Penalty for low outliers using min filter
    low_performer_penalty = 0
    for score in base_scores:
        if score < 80:
            low_performer_penalty += 2
    
    # Step 6: Calculate final composite using dictionary-based weight map
    weights = {'base': 0.6, 'bonus': 0.2, 'consistency': 0.15, 'penalty': -0.1}
    raw_contributions = {
        'base': enhanced_score,
        'bonus': attendance_bonus,
        'consistency': consistency_bonus,
        'penalty': low_performer_penalty
    }
    
    # Final weighted aggregation
    final_score = sum(raw_contributions[key] * weight for key, weight in weights.items())
    
    # Red herring computation (unused)
    hypothetical_savings = days_off * 8 * 30  # Unused financial estimate
    
    return round(final_score, 2)

# Main execution
result = calculate_performance_rating()
print(f"Result: {result}")