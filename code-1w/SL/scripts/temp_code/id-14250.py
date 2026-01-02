def analyze_system_performance():
    base_loads = [120, 135, 140, 128, 150, 160, 155, 170, 180, 175]
    temp_offset = 5
    scaling_factor = 1.1
    adjusted_loads = [load * scaling_factor for load in base_loads]
    
    # Simulate sliding window analysis over peak usage period
    window_start = 3
    window_end = 8
    efficiency_factor = 0.9
    peak_capacity = max(adjusted_loads[window_start:window_end]) * efficiency_factor
    
    # Irrelevant diagnostic check (minor distraction)
    avg_temp = sum([22, 23, 21, 24, 25]) / 5
    status_flag = avg_temp > 20
    
    # Final result output
    print(f"Result: {peak_capacity}")

analyze_system_performance()