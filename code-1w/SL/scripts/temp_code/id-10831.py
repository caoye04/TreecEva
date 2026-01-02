def process_sensor_data():
    raw_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
    offset = 0.5
    
    corrected_readings = []
    for reading in raw_readings:
        corrected = reading + offset
        corrected_readings.append(round(corrected, 1))
    
    sorted_readings = sorted(corrected_readings)
    filtered_readings = [temp for temp in sorted_readings if temp > 24.0]
    
    adjusted_readings = []
    for val in filtered_readings:
        adjusted_readings.append(val * 1.05)
    
    correction_factor = 1.1
    final_temperature = adjusted_readings[-1] * correction_factor
    
    # Irrelevant logging (minimal interference)
    log_entry = f"Processed {len(raw_readings)} readings"
    log_entry.upper()  # unused operation
    
    return final_temperature

result = process_sensor_data()
print(f"Result: {result}")