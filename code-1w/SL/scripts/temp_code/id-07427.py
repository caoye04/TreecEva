def analyze_system_metrics():
    raw_readings = [12, 15, 22, 8, 33, 41, 19]
    base_threshold = 18
    
    # Compute derived metrics
    high_load = [x for x in raw_readings if x > base_threshold]
    peak_count = len(high_load)
    average_load = sum(raw_readings) / len(raw_readings)
    
    # Simulate system state flags
    overload_alert = peak_count > 3
    stability_window = average_load < 25.0
    
    # Additional intermediate variables (some with low interference)
    temp_buffer = [x * 2 for x in high_load]  # Irrelevant processing
    buffer_size = len(temp_buffer)
    
    # Core logic determining final state
    cycle_check = stability_window
    bit_analysis = overload_alert
    filtered_data = bool(peak_count)
    
    threshold_flag = filtered_data and (bit_analysis ^ cycle_check)
    
    print(f"Result: {threshold_flag}")

analyze_system_metrics()