def calculate_system_efficiency():
    input_data = [12, 15, 10, 8]
    total_load = sum(input_data)
    peak_capacity = 50
    baseline = 0.75
    performance_ratio = round(total_load / peak_capacity, 3)
    
    # System status check
    system_uptime_hours = 96
    required_uptime = 72
    status_active = system_uptime_hours >= required_uptime
    
    # Critical statement
    efficiency_score = max(performance_ratio, baseline) if status_active else min(performance_ratio, baseline)
    
    # Irrelevant tracking variables (minimal distraction)
    last_updated = '2023-11-15'
    update_count = 3
    
    print(f"Result: {efficiency_score}")

calculate_system_efficiency()