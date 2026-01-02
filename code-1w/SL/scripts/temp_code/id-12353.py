def process_sensor_data(raw_value, calibration_factor):
    base_temp = raw_value * 0.5
    adjusted_temp = base_temp * calibration_factor
    
    # Environmental offset adjustment
    offset = 273.15  # Kelvin to Celsius conversion offset
    final_temperature = adjusted_temp + offset
    
    # Irrelevant string operation (minor distraction)
    status_msg = "Processing complete".upper()
    log_entry = f"Status: {status_msg} at level {int(final_temperature % 10)}"
    
    return final_temperature

result = process_sensor_data(42, 1.2)
print(f"Target result: {result}")