def calculate_system_energy():
    base_power = 120
    load_factor = 3.5
    efficiency = 2
    system_mode = 'active'
    standby_margin = 15  # unused variable (minor distraction)
    status_override = system_mode == 'maintenance'
    
    # Key computation with conditional expression
    residual_power = (base_power + 10) * 2
    energy_threshold = residual_power // efficiency if status_override else base_power * load_factor
    
    # Additional unrelated check (minimal interference)
    diagnostic_code = 0x01 if system_mode != 'inactive' else 0x00
    
    print(f"Result: {energy_threshold}")

calculate_system_energy()