def calculate_performance():
    raw_points = 845
    bonus_multiplier = 1.2
    base_penalty = 30
    
    # Compute initial performance metrics
    scaled_points = int(raw_points * bonus_multiplier)
    level_threshold = 1000
    
    # Determine tier and apply tier-based adjustments
    if scaled_points >= level_threshold:
        base_bonus = 50
    else:
        base_bonus = 20
    
    final_base = scaled_points + base_bonus
    
    # Irrelevant metric (distractor)
    compliance_rate = 0.97
    audit_flag = False
    
    # Penalty logic based on historical data slice
    recent_violations = [5, 0, 3, 2, 1, 0, 4]
    active_period = recent_violations[2:5]  # Slice: middle segment
    total_active = sum(active_period)
    
    penalty_adjustment = -total_active * 2
    adjusted_score = final_base + penalty_adjustment
    
    # Additional unused tracking variables (minor interference)
    max_violation = max(recent_violations)
    avg_violation = total_active / len(active_period)
    
    print(f"Result: {adjusted_score}")

calculate_performance()