def calculate_system_capacity():
    base_load = 987
    temperature_factor = 23.5
    calibration_data = 'TX-78 Calibration Sequence'
    
    # Extract correction from string using conditional expression
    offset = 3 if 'TX-78' in calibration_data else 5
    
    adjusted_base = base_load + (temperature_factor * 4) - offset
    
    # Simulate efficiency adjustment
    efficiency_factor = 1.75 if adjusted_base > 1000 else 1.5
    
    # Key computation step
    final_capacity = adjusted_base // efficiency_factor
    
    # Irrelevant tracking variable (minor distraction)
    status_flag = 'OPTIMAL' if final_capacity > 600 else 'STANDBY'
    
    print(f"Result: {final_capacity}")

# Execute function
calculate_system_capacity()