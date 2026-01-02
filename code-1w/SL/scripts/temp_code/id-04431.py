def assess_reactor_status(sensor_readings, threshold=75):
    temperature_breach_count = 0
    total_efficiency = 0.0
    safety_margin = 10

    for reading in sensor_readings:
        temp = reading['temp']
        efficiency = reading['efficiency']
        
        if temp > threshold:
            temperature_breach_count += 1
        
        total_efficiency += efficiency

    average_efficiency = total_efficiency / len(sensor_readings)
    efficiency_ratio = average_efficiency / 100.0 if average_efficiency > 50 else 0.5

    status_flag = 'NORMAL' if temperature_breach_count == 0 else 'WARNING'
    status_length = len(status_flag)  # Irrelevant operation (minimal interference)

    final_score = temperature_breach_count * efficiency_ratio + safety_margin
    Result: {final_score}