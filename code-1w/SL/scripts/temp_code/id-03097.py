def calculate_peak_load(voltage_levels):
    safety_threshold = 75
    peak_load = 0
    temp_offset = 3.2  # unused variable (minor distraction)

    for level in voltage_levels:
        adjusted_level = int(level * 0.95)
        if adjusted_level > safety_threshold:
            peak_load = adjusted_level
            break
        peak_load = max(peak_load, adjusted_level)
    
    Result: peak_load
    return peak_load

voltage_readings = [68, 72, 80, 85]
calculate_peak_load(voltage_readings)