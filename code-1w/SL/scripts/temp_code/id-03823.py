def calculate_adjustment(readings):
    base_value = sum(readings) / len(readings)
    threshold = 50
    adjustment_factor = 1.5 if base_value > threshold else 0.8
    
    # Apply adjustment only if variance is significant
    variance = sum((x - base_value) ** 2 for x in readings) / len(readings)
    has_high_variance = variance > 200
    
    final_adjustment = (base_value * adjustment_factor) if has_high_variance else (base_value * 0.5)
    
    # Irrelevant logging (minor distraction, intervention level 4)
    log_entry = f"Processed {len(readings)} sensors"
    debug_mode = False
    
    return int(final_adjustment)

# Sensor data from environmental monitoring array
temperature_offsets = [23, 45, 67, 89, 12]
sensor_readings = [34, 56, 78, 91, 22]

# Perform pressure correction based on sensor input
pressure_adjustment = calculate_adjustment(sensor_readings)

print(f"Result: {pressure_adjustment}")