def calculate_travel_metrics():
    initial_distance = 250
    scale_factor = 0.75
    
    # Simulate distance reduction
    temp_adjustment = 50
    remaining_distance = initial_distance - temp_adjustment
    
    # Apply scaling
    final_distance = remaining_distance * scale_factor
    
    # Distractor variables (minimal for intervention 5)
    unused_var = 100
    placeholder = "tracking"
    
    print(f"Result: {final_distance}")
    return final_distance

calculate_travel_metrics()