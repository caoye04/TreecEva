def analyze_system_stability(readings):
    total_power = 0
    temp_offset = 0
    cycle_count = 0
    fluctuation_log = []
    equilibrium_score = 0
    
    # Preprocess readings with offset correction
    corrected_readings = [r + 1.5 for r in readings]
    
    for i, reading in enumerate(corrected_readings):
        if i % 3 == 0:
            temp_offset += reading * 0.1
        
        power_level = int(reading ** 2) % 17
        total_power += power_level
        
        if power_level > 10:
            fluctuation_log.append((i, power_level))
            cycle_count += 1
        elif len(fluctuation_log) > 0 and fluctuation_log[-1][1] > 12:
            cycle_count -= 1  # Compensate overactivity

    # Simulate feedback loop
    feedback_strength = 0
    for idx, fluc in fluctuation_log:
        feedback_strength += idx // (fluc + 1)
    
    # Irrelevant string processing (distractor)
    status_msg = "System nominal" if cycle_count > 3 else "Alert mode"
    status_code = ''.join([chr(ord(c) + 1) for c in status_msg])
    debug_info = status_code.upper().replace(" ", "_")
    
    # Distractor dictionary operations
    system_state = {"power": total_power, "cycles": cycle_count, "temp": temp_offset}
    system_state.update({"debug": debug_info})
    system_state["timestamp"] = 12345
    
    # Core computation path
    base_metric = sum([x for x in corrected_readings if x < 10])
    adjustment_factor = len(fluctuation_log) - feedback_strength
    final_tally = base_metric + total_power - adjustment_factor
    
    # Key statement
    equilibrium_score = final_tally // (cycle_count + 1)
    
    print(f'Result: {equilibrium_score}')

# Input data
sensor_data = [2.1, 5.3, 8.7, 3.2, 9.1, 6.4, 4.8, 7.2]
analyze_system_stability(sensor_data)