def monitor_system(temp):
    base_threshold = 70
    adjust_sensitivity = lambda x: 1.2 if x > 80 else 0.9
    temp_factor = temp / base_threshold
    
    # Irrelevant logging variable (minor distraction)
    system_log_entry = f'Temp reading: {temp}'
    
    energy_threshold = int(base_threshold * adjust_sensitivity(temp) * (temp_factor > 1))
    
    # Conditional override based on safety protocol
    if temp > 82:
        energy_threshold = int(energy_threshold * 1.1)
    
    return energy_threshold

# Execute
final_diagnostic = monitor_system(85)
print(f"Result: {final_diagnostic}")