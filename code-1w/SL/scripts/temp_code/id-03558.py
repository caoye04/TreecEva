def compute_system_state(hour, temperature, mode):
    critical_hours = {7, 8, 9, 17, 18, 19}
    base_threshold = 22.5
    buffer_zone = 3.7

    is_peak_hour = hour in critical_hours
    is_active = mode == "ACTIVE" and temperature < base_threshold + buffer_zone
    
    temperature_setpoint = base_threshold if is_peak_hour else base_threshold - 1.5
    backup_level = 20.0 if temperature > 25 else 18.5

    energy_threshold = temperature_setpoint if is_active else backup_level
    
    # Irrelevant diagnostic log (minor distraction)
    system_status = "NORMAL" if energy_threshold >= 19 else "LOW"
    
    return energy_threshold

# Main execution
hour_of_day = 8
current_temp = 24.0
operation_mode = "ACTIVE"

result = compute_system_state(hour_of_day, current_temp, operation_mode)
print(f"Target result: {result}")