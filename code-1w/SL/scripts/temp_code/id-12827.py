def calculate_energy_settings(is_high_demand, temperature_celsius):
    base_load = 150
    peak_multiplier = 2.3
    off_peak_multiplier = 0.65
    load_buffer = 27

    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    is_hot = temperature_fahrenheit > 75

    is_peak = is_high_demand and is_hot
    
    # Key assignment with conditional expression
    energy_threshold = load_level if is_peak else base_load * off_peak_multiplier
    
    # Irrelevant tracking variable (minor distraction)
    status_log = "Peak" if is_peak else "Off-Peak"
    
    # Simulate load level only when in peak mode
    if is_peak:
        load_level = base_load * peak_multiplier + load_buffer
    else:
        load_level = base_load * off_peak_multiplier

    return energy_threshold

# Main execution
result = calculate_energy_settings(True, 28)
print(f"Result: {result}")