def process_metrics():
    base_performance = 85
    overhead_cost = 12
    calibration_factor = 0.9
    
    # Calculate raw efficiency
    raw_efficiency = (base_performance - overhead_cost) * calibration_factor
    
    # Adjustment function using lambda
    apply_bonus = lambda x: x * 1.1 if x > 70 else x * 1.05
    
    # Apply dynamic bonus
    adjusted_efficiency = apply_bonus(raw_efficiency)
    
    # Simulate minor environmental penalty
    temp_scaling = 1.0
    for hour in range(1, 5):
        if hour == 3:
            temp_scaling = 0.98
    
    efficiency_score = adjusted_efficiency * temp_scaling
    
    # Final adjustment step
    def final_adjustment():
        nonlocal efficiency_score
        safety_margin = 0.99
        efficiency_score = int(efficiency_score * safety_margin)
    
    final_adjustment()
    
    print(f"Result: {efficiency_score}")

process_metrics()