def analyze_system_performance():
    base_rating = 17
    adjustment_factor = 3
    fallback_value = 91
    
    # Sensor readings (simulated)
    sensor_data = [23, 45, 12, 67, 89, 34, 56]
    avg_sensor = sum(sensor_data[1:-1]) / len(sensor_data[1:-1])  # Exclude first and last
    
    # Secondary computation - partially irrelevant
    outlier_count = 0
    for val in sensor_data:
        if val > 60:
            outlier_count += 1
    
    # System diagnostics with nested logic
    diagnostic_codes = ['OK', 'CALIBRATE', 'OK', 'OK']
    code_count = {code: diagnostic_codes.count(code) for code in set(diagnostic_codes)}
    
    # Determine system status
    is_active = len(diagnostic_codes) > 3
    threshold_met = avg_sensor > 40
    stability_check = sensor_data[-1] - sensor_data[0] < 70
    
    status_flag = is_active and threshold_met and stability_check
    
    # Efficiency calculation with conditional expression
    efficiency_factor = 5 if outlier_count < 3 else 2
    
    # Core assignment with key decision point
    thermal_capacity = base_rating * efficiency_factor if status_flag else fallback_value
    
    # Post-processing (distraction)
    normalized_capacity = thermal_capacity / 10.0
    capacity_rounded = round(normalized_capacity)
    buffer_zone = capacity_rounded * adjustment_factor
    
    # Final output
    print(f"Result: {thermal_capacity}")

analyze_system_performance()