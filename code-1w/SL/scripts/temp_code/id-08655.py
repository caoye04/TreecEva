def calculate_performance_rating():
    base_points = 85
    bonus_multiplier = 1.2
    penalty_rate = 0.85
    
    # Simulate various performance metrics
    attendance_days = 220
    max_days = 260
    attendance_ratio = attendance_days / max_days
    
    # Irrelevant metric - distraction
    average_temperature = 22.5  # Office climate control data, unused
    compliance_checks = [True, True, False, True]
    passed_compliance = all(compliance_checks)
    
    # Additional distracting computation
    feedback_scores = [4.2, 4.5, 3.8, 4.0]
    avg_feedback = sum(feedback_scores) / len(feedback_scores)
    feedback_bonus = 5 if avg_feedback > 4.0 else 0
    
    # Core logic begins
    performance_tier = 'A' if base_points >= 80 else 'B'
    
    # Multiple conditional branches with side distractions
    adjustment_factor = 1.0
    if performance_tier == 'A':
        adjustment_factor *= bonus_multiplier
        if attendance_ratio > 0.8:
            adjustment_factor *= 1.1
            extra_award_points = 10  # Not used directly
        else:
            adjustment_factor *= 0.95
    else:
        adjustment_factor *= penalty_rate

    # Distracting dictionary operations
    metadata_log = {
        'run_id': 'PERF_2024_001',
        'final_adjustment': adjustment_factor,
        'timestamp': '2024-05-20',
        'debug_flag': False
    }
    
    # More irrelevant state tracking
    audit_trail = []
    audit_trail.append('started')
    audit_trail.append('base_assessed')
    # Unused list accumulation

    # Key calculation chain
    raw_score = base_points * adjustment_factor
    if passed_compliance:
        raw_score += feedback_bonus
    
    # Final tier correction using dictionary mapping
    tier_correction = {'A': 5, 'B': -2}
    correction_value = tier_correction.get(performance_tier, 0)
    final_score = int(raw_score + correction_value)
    
    # Dead code path - never executed due to fixed condition
    if False:
        emergency_override = 999
        final_score = emergency_override

    return final_score

# Execution point
final_score = calculate_performance_rating()
print(f"Result: {final_score}")