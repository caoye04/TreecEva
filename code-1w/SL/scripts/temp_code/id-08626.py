def compute_efficiency():
    raw_output = 450
    max_capacity = 500
    downtime_events = 3
    maintenance_factor = 0.98
    
    # Calculate utilization rate
    utilization_rate = (raw_output / max_capacity) * 100
    
    # Simulate minor system degradation
    adjusted_rate = utilization_rate * maintenance_factor
    
    # Normalize output to a 0-120 scale
    normalized_output = round(adjusted_rate * 1.2, 2)
    
    # Cap efficiency score at 100%
    efficiency_score = min(normalized_output, 100)
    
    # Irrelevant string processing (distractor for intervention level)
    status_msg = f'System efficiency: {efficiency_score:.1f}%'    
    status_msg_upper = status_msg.upper()
    warning_flag = 'CRITICAL' in status_msg_upper
    
    return efficiency_score

result = compute_efficiency()
print(f'Result: {result}')